from email.policy import default
from odoo import fields,models,api


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _inherit="mail.thread"
    _description ="this model is used for hospital management"
    
    name = fields.Char(required=True)
    apointment_date = fields.Date(string="Apointment Date")
    state = fields.Selection([('draft','Draft'),('in_progress','Progress'),('done','Done'),('close','Closed')],default="draft")
    blood_group = fields.Selection([('A+','A+VE'),('B+','B+VE'),('O-','O-ve')],string="Blood Group",tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True)
    gender_two = fields.Selection([('male','Male'),('female','Female')],string="Gender") 
    link = fields.Char('HOSPITAL LINK', default='https://babymhospital.org/')
    password = fields.Char(string="PASSWORD" ,size=10)
    message=fields.Char(string="Message")
    email=fields.Char(string="Email")
    schedule = fields.Integer(string="auto increment number")
    
    def action_sent_gmail(self):
        self.ensure_one()
        mail_template=self.env.ref('bi_different_views.hospital_patient_email_template')
        mail_template.send_mail(self.id,force_send=True)
        
    def action_show_ribon(self):
        self.write({'state':'close'})
         
    @api.model       
    def action_cron_job(self):
        records = self.env['hospital.patient'].search([])
        for record in records:
            if record.schedule:
                record.schedule += 1
                      
        for record in records:
            if record.email:
                mail_template=self.env.ref('bi_different_views.hospital_patient_email_template')
                mail_template.send_mail(record.id,force_send=True)
        for record in records:
            if record.gender:
                record.gender_two = record.gender