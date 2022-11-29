from odoo import fields, models, api
from passlib.pwd import _sequence_types
from tempfile import _name_sequence


class Affaire(models.Model):
    _inherit = "crm.lead"
    
    
    affaire = fields.Char(string='Affaire', required=True, copy=False, states={'draft': [('readonly', False)]}, index=True, readonly=True, default=('New'))
    
    @api.model
    def create(self, vals):
        if vals.get('affaire') == 'New':
            vals['affaire'] = self.env['ir.sequence'].next_by_code('num.affaire') or _('New')
            res = super(Affaire, self).create(vals)
            return res