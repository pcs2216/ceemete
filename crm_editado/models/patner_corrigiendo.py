# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_partner(models.Model):
    _inherit = 'res.partner'

    x_cmt_medioseentero = fields.Selection(
        string='Medio por el cual se enteró de nosotros',
        selection=[(1, 'Prospección'), (2, 'Referido'),
                   (3, 'Mailing/Social Media'), (5, 'Evento'), (6, 'Otro')]
    )
    x_cmt_otromedio = fields.Char(
        string='Otro medio por el cual se enteró: ',
    )

    x_cmt_eventoseentero = fields.Many2one('x_evento_promocion',
                                          string='Evento en el cual se enteró: ',
                                          ondelete='set null',
                                          )
    x_cmt_prospeccion = fields.Many2one('x.model.prospeccion',
                                          string='Tipo de prospección',
                                          ondelete='set null',
                                          )                                    
