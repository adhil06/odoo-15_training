import base64
import io
from odoo import models 


class CustomerReportXlsx(models.AbstractModel):
    _name = 'report.bi_excel_report.report_customer_excel_report_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
    
           
           
        partner = data['partner_id']
        date_fr =data['date_from']
        date_t=data['date_to']
        sheet = workbook.add_worksheet('sales')  
        bold = workbook.add_format({'bold':True})
        sheet.set_column('B:B',13)
        sheet.set_column('C:C',13)
        sheet.set_column('D:D',12)
        sheet.set_column('E:E',11)
        sheet.set_column('F:F',15)
        sheet.set_column('G:G',10)
        merge_format2=workbook.add_format({"bold":True,"color":"black"})
        sheet.merge_range("A2:B2",f"from date:{date_fr}",merge_format2)
        merge_format3=workbook.add_format({"bold":True,"color":"black"})
        sheet.merge_range("C2:D2",f"to date:{date_t}",merge_format3)
        col=0
            
        domain = []
        if partner:
           domain+=[('partner_id','=',partner)] 
        if date_fr:
            domain+=[('date_order','>=',date_fr)] 
        if date_t:
            domain+=[('date_order','<=',date_t)] 
        #we can also directly give condition inside search like .search([('partner_id','=',partner),('date_order','>=',date_fr),('date_order','<=',date_t)])
        sale_orders=self.env['sale.order'].search(domain)
               
        merge_format1=workbook.add_format({"align":"center","bold":True,"color":"black"})
        sheet.merge_range("A1:G1",f"SALE EXCEL SHEET -BassamInfoTech",merge_format1)
        heading_format = workbook.add_format({'bold': True, 'color': 'gray'})
        sheet.write(3,0,'ID',heading_format)
        sheet.write(3,1,'CUSTOMER',heading_format)
        sheet.write(3,2,'PRODUCT',heading_format)
        sheet.write(3,3,'ORDER DATE',heading_format)
        sheet.write(3,4,'QUANDITY',heading_format)
        sheet.write(3,5,'UNIT PRICE',heading_format)
        sheet.write(3,6,'TAX',heading_format)
        sheet.write(3,7,'SUBTOTAL',heading_format)
        row=4
        for sale_order in sale_orders:
            row=row+1
            sheet.write(row,col,sale_order.name)
            sheet.write(row,col+1,sale_order.partner_id.name)
            format2 = workbook.add_format({'num_format': 'dd/mm/yy'})
            sheet.write(row,col+3,sale_order.date_order,format2)
            for line in sale_order.order_line:
                sheet.write(row,col+2,line.product_id.name)
                sheet.write(row,col+4,line.product_uom_qty)
                sheet.write(row,col+5,line.price_unit)
                temp = row
                for tax in line.tax_id:
                    sheet.write(row,col+6,tax.name)
                    temp=temp+1
                sheet.write(row,col+7,line.price_subtotal)
                row=row+1
            sheet.write(row,col+6,'total')
            sheet.write(row,col+7,sale_order.amount_total)   
               
               
    
               
                