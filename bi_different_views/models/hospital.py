from odoo import fields,models


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description ="this model is used for different views"
    
    name = fields.Char(required=True)
    apointment_date = fields.Date(string="Apointment Date")
    blood_group = fields.Selection([('A+','A+VE'),('B+','B+VE'),('O-','O-ve')],string="Blood Group")
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")
    link = fields.Char(string="sign up")
    link = fields.Char('HOSPITAL LINK', default='https://babymhospital.org/')
    password = fields.Char(string="PASSWORD" ,size=10)
    message=fields.Char(string="Message")
    email=fields.Char(string="Email")
    
    def action_sent_email(self):
        if self.email:
            self.email=self.message