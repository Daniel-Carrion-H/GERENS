# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    _inherit = "res.partner"

    birthdate_date = fields.Date("Birthdate")
    age = fields.Integer(readonly=True, compute="_compute_age")
      
    gender = fields.Selection(
        [("0", "Masculino"), ("1", "Femenino"), ("3", "Otro")],string="Genero"
    )
    
    #empresa_actual = fields.Char(string='Actual Empresa')
    #empresa_anterior = fields.Char(string='Anterior Empresa')
    nationality_id = fields.Many2one("res.country", "Nationality")
    #nivel = fields.Selection( ("I","I"),("II","II"),("III","III"),("IV","IV"),("V","V")])
    origen_registro = fields.Selection(
        [("803","Ateneo"),("818","Banner Log"),("608","Base de Datos"),("607","Campana Anterior"),("747","Charla"),
         ("662","Desayuno"),("194","El Comercio"),("196","Email de Entrada"),("678","Extemin 2013"),(" 842","Extemin 2017"),
         ("636","Facebook"),("713","Feria"),("738","Google"),("797","Landing Page"),("787","Linkedin"),("296","Llamada de entrada"),
         ("737","Mailing"),("635","Migracion"),("737","Mailing"),("635","Migracion"),("625","Noticias Gestion"),("298","Referido"),
         ("298","Referido"),("739","Registro de descarga"),("687","Revista"),("297","SEACE"),("618","Telemarketing"),("619","Visita a GERENS"),
         ("733","Visita a mina"),("880","Wassap"),("195","Web")]
    )
    email_gerens = fields.Char()
    empresa_id= fields.Many2one("empresa","empresa")
    pais_empresa= fields.Char(related="empresa_id.paisempresa")
    convenio = fields.Boolean(related="empresa_id.convenio")
    universidad_id = fields.Many2one('universidad')
    cargo_id= fields.Many2one('cargo')
    #slide_channel_partner_id= fields.Many2one('slide_channel_partner')
    slide_channel_ids = fields.Many2many(
        'slide.channel', 
        string='Cursos', groups="website_slides.group_website_slides_officer",readonly=True)
    
    
    @api.depends("birthdate_date")
    def _compute_age(self):
        for record in self:
            age = 0
            if record.birthdate_date:
                age = relativedelta(fields.Date.today(), record.birthdate_date).years
            record.age = age