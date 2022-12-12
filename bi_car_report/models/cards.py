from odoo import models,fields,api

class carCard_cust(models.Model):
    _inherit = "sale.order"

    def print_card(self):
        return self.env.ref('bi_car_report.car_report_pdf').report_action(self)
