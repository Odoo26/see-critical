from odoo import models, fields

class Sites(models.Model):
    _name = 'sites.sites'

    name = fields.Char(string="Nom du site")
    types = fields.Many2one(comodel_name='types.sites',string='Type de materiel')
    adresse = fields.Char(string="Adresse")
    commune = fields.Char(string="commune")
    num_dept = fields.Integer("N° Département")
    code_postal = fields.Integer("Code Postal")