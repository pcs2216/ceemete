# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import timedelta


class x_cmt_partner_totalinvoiced_2(models.Model):
    _inherit = 'res.partner'

    x_duracion_23 = fields.Float(
        digits=(6, 2), help="Duration in days", compute="_set_duration_2",
        store=True,
    )

    @api.depends('x_ultimaCompra')
    def _set_duration_2(self):
        for r in self:
            if r.x_ultimaCompra:

                start_date = fields.Datetime.from_string(r.x_ultimaCompra)
                end_aux = fields.Date.today()
                end_date = fields.Datetime.from_string(end_aux)
                r.x_duracion_23 = ((end_date - start_date).days + 1)
