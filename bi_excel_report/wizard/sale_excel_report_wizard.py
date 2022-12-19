from odoo import fields,models
 
 
class SaleExcelReportWizard(models.TransientModel):
    _name="sale.excel.report.wizard"
    _description ="Sale excel report wizard"

    name = fields.Char(string="Name",required=True)

    def submit(self):
        return
    
