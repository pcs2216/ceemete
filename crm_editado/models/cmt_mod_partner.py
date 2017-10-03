# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_partner(models.Model):
    _inherit = 'res.partner'

    x_cmt_validarSospechoso = fields.Boolean(
        string='Perfil Sospechoso')
    x_cmt_validarPerfil = fields.Boolean(
        string='Perfil Validado')
