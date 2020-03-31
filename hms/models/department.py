from odoo import models, fields

class Department (models.Model):
    _name="hms.department"
    _rec_name="Name"

    Name = fields.Char()
    Capacity = fields.Integer()
    Is_opened= fields.Boolean()
    patients_ids = fields.One2many('hms.patient','department_id')
    # Patients = fields.Integer(compute='get_patients')
    # doctors_ids = fields.One2many('hms.doctors','department_id')

    # def get_patients(self):
    #     self.Patients=self.env['hms.patient'].search_count([('department_id','=',self.id)])