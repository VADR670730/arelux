# -*- coding: utf-8 -*-
from openerp import api, models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
        
    ar_qt_activity_type = fields.Selection(
        [
            ('todocesped', 'Todocesped'),
            ('arelux', 'Arelux'),
            ('evert', 'Evert'),                    
        ],
        size=15, 
        string='Tipo de actividad'
    )
    ar_qt_customer_type = fields.Selection(
        [
            ('particular', 'Particular'),
            ('profesional', 'Profesional'),        
        ],        
        string='Tipo de cliente',
    )
    
    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the partner is changed:
        - Pricelist
        - Payment term
        - Invoice address
        - Delivery address
        """
        if not self.partner_id:
            self.update({
                'partner_invoice_id': False,
                'partner_shipping_id': False,
                'payment_term_id': False,
                'fiscal_position_id': False,
            })
            return

        addr = self.partner_id.address_get(['delivery', 'invoice'])
        values = {
            'pricelist_id': self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False,
            'payment_term_id': self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
            'partner_invoice_id': addr['invoice'],
            'partner_shipping_id': addr['delivery'],
            'note': self.with_context(lang=self.partner_id.lang).env.user.company_id.sale_note,
        }
        
        if self.opportunity_id.id==0:
            values['ar_qt_activity_type'] = self.partner_id.ar_qt_activity_type or False
            values['ar_qt_customer_type'] = self.partner_id.ar_qt_customer_type or False
        else:
            values['ar_qt_activity_type'] = self.opportunity_id.ar_qt_activity_type or False
            values['ar_qt_customer_type'] = self.opportunity_id.ar_qt_customer_type or False            

        if self.partner_id.user_id.id>0:
            if self.opportunity_id.id==0:
                values['user_id'] = self.partner_id.user_id.id
            else:
                values['user_id'] = self.opportunity_id.user_id.id
        
        if self.opportunity_id.id>0:
            values['team_id'] = self.opportunity_id.team_id.id
                    
        self.update(values)                                                               