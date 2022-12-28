from odoo import fields,models,api


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
    schedule = fields.Integer(string="auto increment number")
    
    def action_sent_gmail(self):
        self.ensure_one()
        mail_template=self.env.ref('bi_different_views.hospital_patient_email_template')
        mail_template.send_mail(self.id,force_send=True)
         
    @api.model       
    def action_cron_job(self):
        records = self.env['hospital.patient'].search([])
        for record in records:
            if record.schedule:
                record.schedule += 1
                
        for record in records:
            if record.email:
               self.action_sent_gmail()