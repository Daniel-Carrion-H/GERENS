import re
import logging
from odoo import api, fields, models
from odoo.osv import expression
from odoo.exceptions import UserError
from psycopg2 import IntegrityError
from odoo.tools.translate import _
_logger = logging.getLogger(__name__)

class Universidad(models.Model):
    _name = 'universidad'
    _description = 'Universidad'
    _order = 'name'
    
    name = fields.Char(
        string='Universidad', required=True
    )
    tipouniv= fields.Selection([("1","Publico"),("2","Privado")],string='Tipo')
    univperu = fields.Boolean(string="Universidad Nacional", default=True)
    
    @api.model
    def create(self, vals):
        return super(Universidad,self).create(vals)

    def write(self, vals):
        return super(Universidad,self).write(vals)
    
    @api.onchange('name')
    def _onchage_name(self):
        self.name= self.name.upper() if self.name else False