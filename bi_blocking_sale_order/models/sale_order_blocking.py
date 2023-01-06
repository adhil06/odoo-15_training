from odoo import fields,models


class SaleOrderBlocking(models.TransientModel):
    _inherit="res.config.settings"
    
    day_count = fields.Integer(string="No of Days",config_parameter='bi_blocking_sale_order.day_count')