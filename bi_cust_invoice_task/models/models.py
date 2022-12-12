# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    manager_remarks = fields.Char(string="Manager Remarks")
    director_remarks = fields.Char(string="Director Remarks")

    def create(self,vals):
        res = super(AccountMove, self).create(vals)
        if self.user_has_groups('group_sales_custom_manager'):
            
        return res

    def write(self,vals):
        res = super(AccountMove, self).write(vals)
        if res.type == 'out_invoice':
            if res.partner_id.manager_remarks:
                res.manager_remarks = res.partner_id.manager_remarks
            if res.partner_id.director_remarks:
                res.director_remarks = res.partner_id.director_remarks
        return res

