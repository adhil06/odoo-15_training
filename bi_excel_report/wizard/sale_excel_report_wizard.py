from odoo import fields,models
 
 
class SaleExcelReportWizard(models.TransientModel):
    _name="sale.excel.report.wizard"
    _description ="Sale excel report wizard"

    name = fields.Many2one(comodel_name="res.partner",string="Name",required=True)
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_print_excel_report(self):
        data = {
                # 'model': self._name,
                # 'ids': self.ids,
            }
        return self.env.ref('bi_excel_report.customer_excel_report_xlsx').report_action(self, data=data, config=False)
