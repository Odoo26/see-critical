from odoo import models, fields
class Types(models.Model):
    _name = 'types.sites'

    name = fields.Char(string="Type de materiel")