from odoo import fields,models,api


class MaterialTransferLines(models.Model):
    _name="material.lines"
    _description="one two many lines of material transfer"
    
    product_name_id =fields.Many2one('product.product',string="Product")
    quantity = fields.Integer(string="Quantity")
    available_qty = fields.Integer(string="Available Quatity")
    transfered_qty= fields.Integer(string="Transfer Quandity")
    main_connection_id = fields.Many2one('material.transfer',string="Lines")
    
    @api.onchange('product_name_id')
    def onchange_product_name_id(self):
        self.available_qty=self.product_name_id.with_context({'location':self.main_connection_id.source_location_id.id}).qty_available
        
    