from odoo import fields,models
 
 
class excelReportCreation(models.Model):
    _inherit = 'sale.order'

    is_player = fields.Boolean(string="Player")

    

