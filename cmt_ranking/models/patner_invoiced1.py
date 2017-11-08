# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_cmt_partner_totalinvoiced1(models.Model):
    _inherit = 'res.partner'
    
    
    x_ultimaCompra = fields.Date(
        string='Última Compra', readonly=True, compute='_compute_ultima_compra', 
        
        
    )
   

    @api.one
    @api.depends('invoice_ids')
    def _compute_ultima_compra(self):
        for rcrd in self:
            if len(self.invoice_ids) > 0:
                rcrd['x_ultimaCompra'] = self.invoice_ids[0].date_invoice
            else :
                rcrd['x_ultimaCompra'] = False
            
