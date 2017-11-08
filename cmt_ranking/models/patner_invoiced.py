# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_partner_totalinvoiced(models.Model):
    _inherit = 'res.partner'

    x_cliente_ranking = fields.Many2one(
        'cliente.ranking', 'Ranking M2O',
        required=True,
        store=True,
        default=lambda self: self.env['cliente.ranking'].search(
            [('x_name', '=', 'Montos')]),
        readonly=True,
    )
    x_cmt_rankingCliente = fields.Char(
        string='Ranking del  Cliente',
        compute='_compute_total_invoiced_inherit', store=True
    )

    

    @api.one
    @api.depends('total_invoiced', 'x_cliente_ranking.x_plata', 'x_cliente_ranking.x_oro', 'x_cliente_ranking.x_platino')
    def _compute_total_invoiced_inherit(self):
        for rcrd in self:
            var = self.total_invoiced / 12
            if (var == 0.0):
                rcrd['x_cmt_rankingCliente'] = 'Ninguno - ' + str(var)
            elif (var > 0.0 and var < rcrd.x_cliente_ranking.x_plata):
                rcrd['x_cmt_rankingCliente'] = 'Comprador - ' + str(var)
            elif (var >= rcrd.x_cliente_ranking.x_plata and var < rcrd.x_cliente_ranking.x_oro):
                rcrd['x_cmt_rankingCliente'] = 'PLATA - ' + str(var)

            elif (var >= rcrd.x_cliente_ranking.x_oro and var < rcrd.x_cliente_ranking.x_platino):
                rcrd['x_cmt_rankingCliente'] = 'ORO - ' + str(var)

            else:
                rcrd['x_cmt_rankingCliente'] = 'PLATINO - ' + str(var)

    
