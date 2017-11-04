# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_ranking_cliente(models.Model):
    _name = 'cliente.ranking'
    _description = 'Definir montos para ranking de clientes'

    currency_id = fields.Many2one(
        'res.currency', 'Moneda',
        required=True,
        store=True,
        default=lambda self: self.env['res.currency'].search(
            [('name', '=', 'MXN')]),
        readonly=True,
    )
    x_name = fields.Char(
        string='Descripccion',
        required=True)

    x_plata = fields.Float(string="Plata")
    x_oro = fields.Float(string="Oro")
    x_platino = fields.Float(string="Platino")
