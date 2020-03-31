from odoo import models, fields

class Doctors (models.Model):
    _name="hms.doctors"
    _rec_name="first_name"

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Binary("Image", help="This field holds the image used as avatar for \
                this contact, limited to 1024x1024px", )
    department_id = fields.Many2one('hms.department')
    patient_id = fields.One2many('hms.patient','doctor_id')