import ssl
from odoo import models,fields,api

        
class SaleProductLine(models.Model):
    _inherit="sale.order.line"
    
    about= fields.Char(string="About",compute="_compute_about")
    # date_lauanch =fields.Integer(string='Launch Date',compute="_compute_date")
    
    @api.depends("product_id")
    def _compute_about(self):
        if self.product_id.about_product:
            self.about=self.product_id.about_product
        else:
            self.about='0'
            
    # @api.compute("launch_year")
    # def _compute_date(self):
    #     if self.product_id.launch_year:
    #         self.date_lauanch=self.product_id.lauch_year
    #     else:
    #         self.date_lauanch=0
    