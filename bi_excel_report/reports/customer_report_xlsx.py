import base64
import io
from odoo import models 


class CustomerReportXlsx(models.AbstractModel):
    _name = 'report.bi_excel_report.report_customer_excel_report_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print("-------------------------------------",data,lines)
        # for obj in partners:
        #     report_customer_excel_report_xls = obj.name
        #     # One sheet by partner
        #     sheet = workbook.add_worksheet(report_customer_excel_report_xls[:31])
        #     bold = workbook.add_format({'bold': True})
        #     sheet.write(0, 0, obj.name, bold)