from odoo import fields,models
 
 
class SaleExcelReportWizard(models.TransientModel):
    _name="sale.excel.report.wizard"
    _description ="Sale excel report wizard"

    name = fields.Many2one(comodel_name="res.partner",string="Customer")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
    

    def action_print_excel_report(self):
        
        data = {
                'partner_id':self.name.id,
                'date_from':self.date_from,
                'date_to':self.date_to
                
            }
        return self.env.ref('bi_excel_report.customer_excel_report_xlsx').report_action(self, data=data, config=False)
