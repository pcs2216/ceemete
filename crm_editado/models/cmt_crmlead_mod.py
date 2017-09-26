# -*- coding: utf-8 -*-
from odoo import  fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'

    x_cmt_statuscliente = fields.Boolean (related='partner_id.x_cmt_validarListaPrecios',default=False,readonly=True)
