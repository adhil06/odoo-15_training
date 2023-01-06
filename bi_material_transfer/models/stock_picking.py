from odoo import fields,models


class StockPicking(models.Model):
    _inherit="stock.picking"
    
    material_transfer_id = fields.Many2one('material.transfer')