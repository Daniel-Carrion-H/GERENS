import re
import logging
from odoo import api, fields, models
from odoo.osv import expression
from odoo.exceptions import UserError
from psycopg2 import IntegrityError
from odoo.tools.translate import _
_logger = logging.getLogger(__name__)

class Cargo(models.Model):
    _name = 'cargo'
    _description = 'Cargo en la empresa'
    _order = 'name'
    
    name = fields.Char(
        string='Cargo Empresa', required=True
    )
       
    @api.model
    def create(self, vals):
        return super(Cargo,self).create(vals)

    def write(self, vals):
        return super(Cargo,self).write(vals)
    
    @api.onchange('name')
    def _onchage_name(self):
        self.name= self.name.upper() if self.name else False