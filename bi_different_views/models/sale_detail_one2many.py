from odoo import fields,models,api


class ProductDetails(models.Model):
    _name="product.details"
    _description = "Poduct details is added to custom model hospitalpatient"
    
    product_name_id = fields.Many2one('product.template',string="Product")
    qty = fields.Float(string="Quandity")
    unit_price = fields.Float(string="Unit Price")
    sub_total = fields.Float(string="Subtotal")
    hospital_connection_id = fields.Many2one('hospital.patient',string="connection")
    
    # @api.depends('hospital_connection_id')
    # def _compute_product_name_id(self):
    #     lines = self.hospital_connection_id.sale_id.order_line
    #     for line in lines:
    #         if line.product_id:
    #             self.product_name_id=line.product_id
    #         else:
    #             self.product_name_id=False
            
    # @api.depends('hospital_connection_id')
    # def _compute_qty(self):
    #     lines = self.hospital_connection_id.sale_id.order_line
    #     for line in lines:
    #         if line.product_uom_qty:
    #             self.qty=line.product_uom_qty
    #         else:
    #             self.qty=0
    
    # @api.depends('hospital_connection_id')
    # def _compute_unit_price(self):
    #     lines = self.hospital_connection_id.sale_id.order_line
    #     for line in lines:
    #         if line.price_unit:
    #             self.unit_price=line.price_unit
    #         else:
    #             self.unit_price=0

    # @api.depends('hospital_connection_id')
    # def _compute_sub_total(self):
    #     lines = self.hospital_connection_id.sale_id.order_line
    #     for line in lines:
    #         if line.price_subtotal:
    #             self.sub_total=line.price_subtotal
    #         else:
    #             self.sub_total=0