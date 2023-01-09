from odoo import models,fields
from odoo.exceptions import UserError
from datetime import datetime,timedelta


class SaleOrder(models.Model):
    _inherit="sale.order"
    new_date = fields.Date(string="NewDate")
    confirm_date = fields.Date(string="Confirm Date")
    #above fields want to declare in xml in sale.order model, fields we use want must to be declared in xml
    
    def action_confirm(self):
        record = self.env['res.config.settings'].search([])
        blocking_day = record.block_day_below
        today = datetime.today()
        self.new_date = today - timedelta(days=blocking_day)
        res=super(SaleOrder,self).action_confirm()
        if self.new_date>=self.confirm_date:
            raise UserError("we cannot confirm sale order")
        return res