from odoo import fields,models


class SubjectDetails(models.Model):
    _name = "subject.details"
    _description = "this model is for subject details"
    _rec_name = 'sub_name'
    
    sub_name = fields.Char(string="Subject Name")
    max_mark = fields.Float(string="Maximum Mark")
    