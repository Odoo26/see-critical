from odoo import models, fields
class Types(models.Model):
    _name = 'type.sites'

    name = fields.Char(string="Type de materiel")