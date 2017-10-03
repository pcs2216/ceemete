# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'

   
    x_cmt_validacion = fields.Char(
        string='Validado',
        compute='_compute_ctm_validado')
    x_cmt_sospechoso = fields.Char(
        string='Validado', compute='_compute_ctm_validado')
    @api.depends('partner_id.x_cmt_validarPerfil', 'partner_id.x_cmt_validarSospechoso')
    @api.one
    def _compute_ctm_validado(self):
        for record in self:
            if record.partner_id.x_cmt_validarPerfil:
                record.x_cmt_validacion = 'Perfil Validado'
            else:
                record.x_cmt_validacion = 'Perfil NO Validado'
            if record.partner_id.x_cmt_validarSospechoso:
                record.x_cmt_sospechoso = 'Perfil Sospechoso'
