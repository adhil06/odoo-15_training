from odoo import fields,models,api,_
from odoo.exceptions import UserError
import xlrd
import base64

class WizardFromImportButton(models.TransientModel):
    _name="wizard.from.import.button"
    _description="wizard from import button"
    
    excel_attachment = fields.Binary("Excel File Attachment",attachment=True)
    active_id = fields.Many2one('sale.order')
    
    def action_import(self):
        for record in self:
            if record.excel_attachment:
                workbook=xlrd.open_workbook(file_contents=base64.decodestring(record.excel_attachment))
                for sheet in workbook.sheets():
                    product_name_col = 0
                    qty_col=1
                    unit_price_col= 2
                    values=[]
                    for row in range(4,sheet.nrows):
                        try:
                            product_id = self.env["product.product"].search(
                                [("default_code", "=", sheet.cell(row, product_name_col).value)]
                            )
                            if not product_id:
                                raise UserError(_("Product not found"))
                            product_qty = False
                            product_qty = sheet.cell(row, qty_col).value
                            unit_price = sheet.cell(row, unit_price_col).value
                            values.append(
                                (
                                    0,
                                    0,
                                    {
                                        "product_id": product_id.id,
                                        "product_uom_qty": product_qty,
                                        "price_unit" : unit_price,
                                    },
                                )
                            )
                        except IndexError:
                            break
                    record.active_id.order_line = False
                    record.active_id.order_line = values