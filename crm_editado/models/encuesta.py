# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_partner_encuesta(models.Model):
    _inherit = 'res.partner'

    """x_cmt_medioseentero = fields.Selection(
        string='Medio por el cual se enteró de nosotros',
        selection=[(1, 'Prospección'), (2, 'Referido'),
                   (3, 'Mailing/Social Media'), (5, 'Evento'), (6, 'Otro')]
    )"""
    x_cmt_compitePor = fields.Selection(
        string='Compite por : ',
        selection=[(1, 'Precio'), (2, 'Servicio'),
                   (3, 'Calidad')]
    )
    x_cmt_nivelVendeProductos = fields.Selection(
        string='¿A qué nivel vende sus productos? . ',
        selection=[(1, 'Regional'), (2, 'Nacional'),
                   (3, 'Exporta')]
    )
    x_cmt_prospeccion = fields.Many2one('x.model.prospeccion',
                                        string='Tipo de prospección',
                                        ondelete='set null',
                                        )
    x_tipoDeClientesAtiendes = fields.Many2one('x_cmt_tiposdeclientesatiende',
                                        string='¿A qué tipo de clientes atiende principalmente? .',
                                        ondelete='set null',
                                        )