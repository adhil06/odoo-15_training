from odoo import models
from odoo.exceptions import UserError


class SuperingSaleModule(models.Model):
    _inherit = "sale.order"
    
    def action_confirm(self):
        res = super(SuperingSaleModule,self).action_confirm()
        if self.amount_total<100:
            raise UserError("We cannot confirm ,unless the total greater than 100")
        return res
