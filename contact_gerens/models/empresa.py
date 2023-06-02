import re
import logging
from odoo import api, fields, models
from odoo.osv import expression
from odoo.exceptions import UserError
from psycopg2 import IntegrityError
from odoo.tools.translate import _
_logger = logging.getLogger(__name__)


class Empresa(models.Model):
    _name = 'empresa'
    _description = 'Empresa'
    _order = 'name'
    
    name = fields.Char(
        string='Nombre Empresa', help = 'Empresa creada', required=True
    )
    convenio= fields.Boolean(default=False)
    code = fields.Integer(string='Codigo Top', size=4)
    paisempresa = fields.Char(
        string='Pais de Empresa',
        required=True,
     
    )
      
    @api.model
    def create(self, vals):
        return super(Empresa,self).create(vals)

    def write(self, vals):
        return super(Empresa,self).write(vals)
    
    "Hacer Mayusuclas"    
    @api.onchange('paisempresa','name')
    def _onchage_name(self):
        self.paisempresa = self.paisempresa.upper() if self.paisempresa else False
        self.name = self.name.upper() if self.name else False