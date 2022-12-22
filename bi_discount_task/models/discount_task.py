from odoo import models,fields,api


class saleOrder_cust(models.Model):
    _inherit = "sale.order"

    discount = fields.Monetary(string="Discount")
    discount_footer =fields.Monetary(string="Discount",compute="_compute_discount")
    
    @api.depends('discount')
    def _compute_discount(self):
        if self.discount:
            self.discount_footer=self.discount
        else:
            self.discount_footer=0
