# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'

    x_cmt_validacion = fields.Char(
        string='Validado',
        compute='_compute_ctm_validado')

    x_cmt_tipoCliente = fields.Many2many(related='partner_id.category_id')

    @api.depends('partner_id.x_cmt_validarPerfil')
    @api.one
    def _compute_ctm_validado(self):
        for record in self:
            if record.partner_id.x_cmt_validarPerfil:
                record.x_cmt_validacion = 'Perfil Validado'
