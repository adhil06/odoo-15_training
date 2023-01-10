import base64
import io
from odoo import models


class ExcelReportFromButton(models.AbstractModel):
    _name="report.bi_sale_order_import.sale_order_excel"
    _inherit="report.report_xlsx.abstract"
    
    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('sales')  
        bold = workbook.add_format({'bold':True})
        sheet.set_column('A:A',20)
        sheet.set_column('B:B',13)
        sheet.set_column('C:C',13)
        
        merge_format1=workbook.add_format({"align":"center","bold":True,"color":"black"})
        sheet.merge_range("A1:G1",f"SALE EXCEL SHEET -BassamInfoTech",merge_format1)
        heading_format = workbook.add_format({'bold': True, 'color': 'gray'})
        sheet.write(3,0,'PRODUCT',heading_format)
        sheet.write(3,1,'QUANDITY',heading_format)
        sheet.write(3,2,'UNIT PRICE',heading_format)