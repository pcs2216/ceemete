# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'

    x_cmt_statusC = fields.Many2one(
        'res.partner', string=u'Status cliente',ondelete='cascade')
