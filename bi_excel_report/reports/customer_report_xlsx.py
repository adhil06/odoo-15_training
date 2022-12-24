import base64
import io
from odoo import models 


class CustomerReportXlsx(models.AbstractModel):
    _name = 'report.bi_excel_report.report_customer_excel_report_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
    
           
            # sheet.write(row,col+4,sale['price_unit'])
            # sheet.write(row,col+5,sale['tax_id'])
            # sheet.write(row,col+6,sale['price_subtotal'])
        partner = data['partner_id']
        sheet = workbook.add_worksheet('sales')  
        bold = workbook.add_format({'bold':True})
        sheet.set_column('B:B',13)
        sheet.set_column('C:C',13)
        sheet.set_column('D:D',10)
        sheet.set_column('E:E',11)
        sheet.set_column('F:F',15)
        sheet.set_column('G:G',10)

        sale_orders=self.env['sale.order'].search([('partner_id','=',partner)])
        # row=0
        col=0
        # sheet.write(row,col,'SALES',bold)
        row=2
        if date_fr:
            
            
        merge_format1=workbook.add_format({"align":"center","bold":True,"color":"black"})
        sheet.merge_range("A1:G1","SALE EXCEL SHEET",merge_format1)
        sheet.write(3,0,'ID',bold)
        sheet.write(3,1,'CUSTOMER',bold)
        sheet.write(3,2,'ORDER DATE',bold)
        sheet.write(3,3,'QUANDITY',bold)
        sheet.write(3,4,'UNIT PRICE',bold)
        sheet.write(3,5,'TAX',bold)
        sheet.write(3,6,'SUBTOTAL',bold)
        row=4
        for sale_order in sale_orders:
            row=row+1
            sheet.write(row,col,sale_order.name)
            sheet.write(row,col+1,sale_order.partner_id.name)
            format2 = workbook.add_format({'num_format': 'dd/mm/yy'})
            sheet.write(row,col+2,sale_order.date_order,format2)
            for line in sale_order.order_line:
                sheet.write(row,col+3,line.product_uom_qty)
                sheet.write(row,col+4,line.price_unit)
                temp = row
                for tax in line.tax_id:
                    sheet.write(row,col+5,tax.name)
                    temp=temp+1
                sheet.write(row,col+6,line.price_subtotal)
                row=row+1
            sheet.write(row,col+6,sale_order.amount_total)   
               
               
    
               
                