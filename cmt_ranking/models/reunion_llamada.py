# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_calendar_llamdas(models.Model):
    _inherit = 'calendar.event'

    
    x_esLlamada = fields.Boolean(
        string='Llamada',
    )
    
    x_statusLlamada = fields.Selection(
        string='Status de Llamada',
        selection=[('1', 'Realizado'), ('2', 'No localizable'),('3','Reagendado'),('4','No Responde')]
    )