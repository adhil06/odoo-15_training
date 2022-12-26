from odoo import fields,models


class ProductTask(models.Model):
    _inherit="product.template"
    
    about_product = fields.Char(string="About Product")
    # launch_year= fields.Integer(string="Launch Year")