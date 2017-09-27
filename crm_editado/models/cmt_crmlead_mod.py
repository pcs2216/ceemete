# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'

    x_cmt_statuscliente = fields.Boolean(
        related='partner_id.x_cmt_validarCuestionario', default=False, readonly=True)
    x_cmt_perfilcliente = fields.Text(
        related='partner_id.x_perfilconfirmado', default=False, readonly=True)
    x_cmt_validacion = fields.Char(
        string='Validado',
        compute='_compute_ctm_validado')

    @api.depends('x_cmt_statuscliente')
    @api.one
    def _compute_ctm_validado(self):
        for record in self:
            if record.x_cmt_statuscliente:
                record.x_cmt_validacion = 'Validado'
            else:
                record.x_cmt_validacion = ' NO Validado'
