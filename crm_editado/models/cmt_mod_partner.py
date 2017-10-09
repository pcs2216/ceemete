# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_partner(models.Model):
    _inherit = 'res.partner'

    x_cmt_validarWebsite = fields.Boolean(
        string='Validar website')
    x_cmt_validarPerfil = fields.Boolean(
        string='Perfil Validado')

    @api.onchange('x_perfilconfirmado')
    def _asignar_lista_precios(self):
        if self.x_perfilconfirmado == 'Proyectista' or self.x_perfilconfirmado == 'Usuario Final':
            self.property_product_pricelist = 3
        elif self.x_perfilconfirmado == 'Distribuidor':
            self.property_product_pricelist = 6
        elif self.x_perfilconfirmado == 'Profesional Tecnico':
            self.property_product_pricelist = 4
        elif self.x_perfilconfirmado == 'Contratista':
            self.property_product_pricelist = 5
        elif self.x_perfilconfirmado == 'Fabricante':
            self.property_product_pricelist = 2
        else:
            self.property_product_pricelist = 1
