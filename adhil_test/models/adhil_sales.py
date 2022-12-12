from odoo import models,fields


class saleOrder_cust(models.Model):
    _inherit = "sale.order"

    is_check = fields.Boolean(string="Paid")
