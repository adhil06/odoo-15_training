from email.policy import default
from odoo import models,fields,_,api
from odoo.exceptions import UserError


class MaterialTransfer(models.Model):
    _name="material.transfer"
    _description ="Material Transfer"
    
    operation_type_id = fields.Many2one(comodel_name="stock.picking.type",string="Operation Type",required=True)
    source_location_id = fields.Many2one(comodel_name="stock.location",string="Source Location",required=True)
    destination_location_id  = fields.Many2one(comodel_name="stock.location",string="Destination Location",required=True)
    date = fields.Date(string="Date")
    material_transfer_lines_ids = fields.One2many('material.lines','main_connection_id',string="lines")
    name= fields.Char(string="Sequence No",readonly=True,required=True,default=lambda self: _('New'))
    record_count = fields.Integer(string="count")
    stock_picking_ids = fields.Many2one('stock.picking') #field inside the buttonbox
    state = fields.Selection([('draft','Draft'),('ready','Ready'),('approve','Approve'),('done',('Done'))],required=True, readonly=True, copy=False,default='draft')
    
    # def get_total_count(self):
    #     self.record_count = self.env['stock.picking'].search_count([('self.transfer','=','self.stock_picking_id')])
        
    @api.model
    def create(self,vals):
        res= super(MaterialTransfer,self).create(vals)
        res.name=self.env['ir.sequence'].next_by_code('material.transfer') or _('New')
        return res
    
    def action_transfer(self):
        lines=self.material_transfer_lines_ids
        if self.source_location_id==self.destination_location_id:
            raise UserError("We cannot transfer from same location!")
        for line in lines:
            line.available_qty-=line.quantity
            line.transfered_qty=line.quantity
            if line.quantity>line.available_qty:
                raise UserError(f"There is no enogh quantity in the {self.source_location_id.display_name}")      
        transfer = self.env['stock.picking'].create({
        'picking_type_id': self.operation_type_id.id,
        'location_id': self.source_location_id.id,
        'location_dest_id' : self.destination_location_id.id,
        'material_transfer_id':self.id, 
        })
        
        for line in lines:
            move=self.env['stock.move'].create({
                'product_id':line.product_name_id.id,
                'name':line.product_name_id.name,
                'product_uom_qty' : line.quantity,
                'quantity_done': line.quantity,
                'product_uom': line.product_name_id.uom_id.id,
                'location_id' : self.source_location_id.id,
                'location_dest_id' : self.destination_location_id.id,
                'picking_id':transfer.id
            })
            move._action_assign() #button not visible (for product reservation)
        self.stock_picking_ids=transfer.id #this line for button box
        transfer.button_validate()
        self.record_count = self.record_count + 1
        self.write({'state':'done'})
        
    def action_view_stock_details(self):
        sample_ids = self.env['stock.picking'].search(['id','=',self.id])
        return {
                    'type': 'ir.actions.act_window',
                    'name': 'Picking',
                    'view_mode': 'list,form',
                    'res_model': 'stock.picking',
                    'domain': [('material_transfer_id', '=', self.id)],
                }
        
    def action_ready(self):
        self.write({'state': 'ready'})
        
    def action_approve(self):
        self.write({'state':'approve'})
    
    def action_draft(self):
        self.write({'state':'draft'})
        
        
        # for line in lines:
        #     transfer['move_ids_without_package'] = [(0,0, {
        #         'product_id':line.product_name_id.id,
        #         'name':line.product_name_id.name,
        #         'product_uom_qty' : line.quantity,
        #         'product_uom': line.product_name_id.uom_id.id,
        #         'location_id' : self.source_location_id.id,
        #         'location_dest_id' : self.destination_location_id.id
        #         })]
        # transfer.action_assign()
        # transfer.button_validate()
                                                    
    # self.env['stock.quant']._update_available_quantity(product_id, order_id.warehouse_id.lot_stock_id, 100)
        
    # def action_set_to_done(self, cr, uid, ids, *args):
    #     move_obj = self.pool.get('stock.move')
    #     self.write(cr, uid, ids, {'state': 'done'})
            
            