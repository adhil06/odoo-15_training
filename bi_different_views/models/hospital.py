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
    custumer_name= fields.Text(string="Customer",compute="_compute_custumer_name")
    order_date = fields.Char(string="Order Date",compute="_compute_order_date")
    payment_terms = fields.Char(string="Payment Terms",compute="_compute_payment_terms")
    product_details_ids = fields.One2many('product.details','hospital_connection_id',string="product lines")
    sale_id = fields.Many2one(comodel_name="sale.order",string="Sale Id")
    
    #sending mail
    def action_sent_gmail(self):
        self.ensure_one()
        mail_template=self.env.ref('bi_different_views.hospital_patient_email_template')
        mail_template.send_mail(self.id,force_send=True)
    
    #function for showing ribbon on form   
    def action_show_ribon(self):
        self.write({'state':'close'})
    
    #schedular cron            
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
    
    #below compute functions are used for getting values from sale.order model to our custom model hospital.patient           
    @api.depends('sale_id')
    def _compute_custumer_name(self):
        if self.sale_id:
            self.custumer_name=self.sale_id.partner_id.name
        else:
            self.custumer_name='0'
            
    @api.depends('sale_id')
    def _compute_order_date(self):
        if self.sale_id:
            self.order_date=self.sale_id.date_order
        else:
            self.order_date='0'
            
    @api.depends('sale_id')
    def  _compute_payment_terms(self):
        if self.sale_id:
            self.payment_terms=self.sale_id.payment_term_id.name
        else:
            self.payment_terms='0'
     
    #below onchance function is used to get the values in the one2many model[sale.order.line] inside selected saleorder  
    
    @api.onchange('sale_id')
    def onchange_sale_id(self):
        lines = self.sale_id.order_line
        for line in lines:
            self.write({6,0,[()] })
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
         
    @api.onchange('sale_id')
    def onchange_sale_id(self):
        lines = self.sale_id.order_line
        for line in lines:
            self.write({
                "product_details_ids": [(0,0, {
                            "product_name_id":line.product_id.id,
                            "qty":line.product_uom_qty,
                            "unit_price":line.price_unit,
                            "sub_total":line.price_subtotal
                        })]
            })
        
    #below code is also correct
    # @api.onchange('sale_id')
    # def onchange_sale_id(self):
    #     lines =[]
    #     for line in self.sale_id.order_line:
    #        self.write({

                    # 'product_details_ids': [(0,0, {
                    #             "product_name_id":line.product_id.id,
                    #             "qty":line.product_uom_qty,
                    #             "unit_price":line.price_unit,
                    #             "sub_total":line.price_subtotal
                    #         })]
    #        })
        