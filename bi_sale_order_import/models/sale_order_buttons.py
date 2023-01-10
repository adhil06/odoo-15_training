from odoo import fields,models,_


class SaleOrder(models.Model):
    _inherit="sale.order"
    
    def action_download_template(self):
        return self.env.ref('bi_sale_order_import.sale_excel_report_xlsx').report_action(self)
    
    def action_import_wizard(self):
        return{
            "name":_("import wizard"),
            "type":"ir.actions.act_window",
            "view_mode":"form",
            "res_model":"wizard.from.import.button",
            "context":{"default_active_id":self.id},
            "target":"new",
        }