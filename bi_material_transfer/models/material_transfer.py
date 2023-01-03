from odoo import models,fields,_,api


class MaterialTransfer(models.Model):
    _name="material.transfer"
    _description ="Material Transfer"
    
    operation_type_id = fields.Many2one(comodel_name="stock.picking.type",string="Operation Type",required=True)
    source_location_id = fields.Many2one(comodel_name="stock.location",string="Source Location",required=True)
    destination_location_id  = fields.Many2one(comodel_name="stock.location",string="Destination Location",required=True)
    date = fields.Date(string="Date")
    material_transfer_lines_ids = fields.One2many('material.lines','main_connection_id',string="lines")
    transfer_sequence= fields.Char(string="Sequence No",readonly=True,required=True,default=lambda self: _('New'))
    
    def action_transfer(self):
        lines=self.material_transfer_lines_ids
        for line in lines:
            line.available_qty-=line.quantity
            line.transfered_qty=line.quantity
        transfer = self.env['stock.picking'].create({
        'picking_type_id': self.operation_type_id.id,
        'location_id': self.source_location_id.id,
        'location_dest_id' : self.destination_location_id.id,
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
        transfer.button_validate()
        
    @api.model
    def create(self,vals):
        res= super(MaterialTransfer,self).create(vals)
        res.transfer_sequence=self.env['ir.sequence'].next_by_code('material.transfer') or _('New')
        return res
        
        
        
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
            
            