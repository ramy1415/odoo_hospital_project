from odoo import models, fields,api
from datetime import datetime,date
import re
from odoo.exceptions import UserError


class ItiPatient (models.Model):
    _name="hms.patient"
    _rec_name="Firstname"

    Firstname=fields.Char()
    Lastname = fields.Char()
    Birthdate = fields.Date()
    History = fields.Html()
    CR_Ratio = fields.Float()
    Blood = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    PCR = fields.Boolean()
    Address = fields.Char()
    Age = fields.Char(compute='get_age')
    image = fields.Binary("Image", help="This field holds the image used as avatar for \
            this contact, limited to 1024x1024px", )
    department_id = fields.Many2one('hms.department')
    department_Capacity = fields.Integer(related='department_id.Capacity')
    doctor_id = fields.Many2many('hms.doctors')
    log_history=fields.One2many('hms.log','patient_id')
    status=fields.Selection([('Undetermined','Undetermined'),('Good','Good'),('Fair','Fair'),('Serious','Serious')],default='Undetermined')
    email=fields.Char()
    customer_id=fields.Many2one('res.partner','Customer Name')
    # customer_name=fields.Char(related='customer_id.name')


    @api.multi
    def write(self,vals):
        if 'status' in vals :
            vals['log_history']=self.log_history.create([{'date': datetime.today(),'description': f"changed status to {vals['status']}",'patient_id':self.id}])
        updated=super(ItiPatient, self).write(vals)
        return updated

    @api.constrains('email')
    def check_email(self):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(regex, self.email) :
            raise UserError("enter a valid email")


    _sql_constraints = [
        ('email_uniqe', 'unique(email)', 'Email id is unique change your custom email id')
    ]


    def get_age(self):
        today = date.today()
        self.Age = today.year - self.Birthdate.year
       # - ((today.month, today.day) < (self.Birthdate.month, self.Birthdate.day))

    def change_state(self,vals):
        self.status = vals['state']

    @api.onchange('Age')
    def on_change_age(self):
        if self.Age > 30:
            self.PCR=True
            return {
                "warning":{
                    "title":"age change",
                    "message":"pcr changed"
                }
        }

