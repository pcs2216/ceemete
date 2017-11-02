# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_tipo_prospeccion(models.Model):
    _name='x.model.prospeccion'

    
    x_name = fields.Char(
        string='Nombre',
    )
    