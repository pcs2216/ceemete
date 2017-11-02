# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_partner_totalinvoiced(models.Model):
    _inherit = 'res.partner'

    x_cmt_tipoCliente = fields.Char(
        string='Ranking del  Cliente',
        compute='_compute_total_invoiced_inherit'
    )


    @api.one
    @api.depends('total_invoiced')
    def _compute_total_invoiced_inherit(self):
        for record in self:
            if (self.total_invoiced == 0.0):
                record['x_cmt_tipoCliente'] = 'Ninguno'
            elif (self.total_invoiced > 0.0 and self.total_invoiced < 10000.0):
                record['x_cmt_tipoCliente'] = 'Comprador'
            elif (self.total_invoiced >= 10000.0 and self.total_invoiced < 25000.0):
                record['x_cmt_tipoCliente'] = 'PLATA'
            elif (self.total_invoiced >= 25000.0 and self.total_invoiced < 50000.0):
                record['x_cmt_tipoCliente'] = 'ORO'
            else:
                record['x_cmt_tipoCliente'] = 'PLATINO'
