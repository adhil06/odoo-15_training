from odoo import fields,models


class StudentDetails(models.Model):
    _name = "student.details"
    _description = "This Model is used for viewing student details"
     
    name = fields.Char(string="Name",required=True)
    age = fields.Integer(string="Age")
    mark = fields.Float(string="Mark")
    dob = fields.Date(string="DOB",required=True,help="date of birth")
    is_player = fields.Boolean(string="Football Player")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    blood_group = fields.Selection([('A+','A+ve'),('B+','B+ve'),('O-','O-ve')],string="Blood Group")
    address = fields.Text(string="ADDRESS")
    hod_id = fields.Many2one(comodel_name="res.partner",string="HOD")
    tag_ids = fields.Many2many(comodel_name="res.partner",string= "Tags")
    subjects_ids = fields.One2many("subject.line.details","student_id",string="Name and Mark Of Subject")
    
class SubjectLineDetails(models.Model):
    _name = "subject.line.details"
    _description = "model for subject details"
    
    sub_name = fields.Many2one("subject.details",string="Subject Name")
    mark = fields.Float(string="Mark")
    student_id = fields.Many2one("student.details",string="Deatails")