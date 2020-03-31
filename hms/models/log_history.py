from odoo import models, fields

class LogHistory (models.Model):
    _name="hms.log"

    created_by = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)
    date = fields.Date()
    description = fields.Char()
    patient_id = fields.Many2one('hms.patient')