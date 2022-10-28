from odoo import models, fields
class Sites(models.Model):
    _name = 'sites.sites'

    name = fields.Char(string="Nom du site")
    type = fields.Char(string="Type de site")
    adresse = fields.Char(string="Adresse")
    commune = fields.Char(string="commune")
    num_dept = fields.Integer("N° Département")
    code_postal = fields.Integer("Code Postal")