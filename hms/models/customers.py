from odoo import models, fields,api
from odoo.exceptions import UserError

class Customers (models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient','related_patient_id')

    @api.multi
    def unlink(self):
        if self.related_patient_id:
            raise UserError("Cant delete this customer")
        else:
            return super().unlink()

    @api.constrains('email')
    def check_email(self):
        if self.env['hms.patient'].search([('email','=',self.email)]) :
            raise UserError("email already exists in patients ")
