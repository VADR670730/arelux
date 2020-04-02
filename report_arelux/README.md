Se modificand las siguientes vistas

### [report_arelux] external_layout_header
Original > https://github.com/odoo/odoo/blob/10.0/addons/report/views/layout_templates.xml#L95

#### Original
```
<?xml version="1.0"?>
<t t-name="report.external_layout_header">
    <div class="header">
        <div class="row">
            <div class="col-xs-3">
                <img t-if="company.logo" t-att-src="'data:image/png;base64,%s' % company.logo" style="max-height: 45px;"/>
            </div>
            <div class="col-xs-9 text-right" style="margin-top:20px;" t-field="company.rml_header1"/>
        </div>
        <div class="row zero_min_height">
            <div class="col-xs-12">
                <div style="border-bottom: 1px solid black;"/>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-6" name="company_address">
                <span t-field="company.partner_id" t-field-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;name&quot;], &quot;no_marker&quot;: true}" style="border-bottom: 1px solid black; display:inline-block;"/>
            </div>
        </div>
    </div>
</t>
```

#### Modificado
```
<?xml version="1.0"?>
<t t-name="report.external_layout_header">
    <div class="header">
        <div class="row">
            <t t-set="ar_qt_activity_type_global" t-value="arelux" ></t>                    
            <t t-if="ar_qt_activity_type_global=='arelux'">                
                <t t-set="custom_color_1" t-value="'#195660'" />
            </t>
            <t t-else="">
                <t t-set="custom_color_1" t-value="'#12575E'" />
            </t>
            <div class='title_bar' t-att-style="'background:'+custom_color_1+';width:100%;height:20px;margin-bottom:10px;'"></div>
            <t t-if="doc_model!='purchase.order'">
                <t t-if="o and 'ar_qt_activity_type' in o">
                    <t t-set="ar_qt_activity_type_global" t-value="o.ar_qt_activity_type"></t>
                </t>                    
                <t t-elif="o and 'partner_id' in o">                                        
                    <t t-set="ar_qt_activity_type_global" t-value="o.partner_id.ar_qt_activity_type"></t>
                </t>
                <t t-if="ar_qt_activity_type_global=='arelux'">                
                    <t t-set="custom_color_1" t-value="'#195660'" />
                </t>
                <t t-else="">
                    <t t-set="custom_color_1" t-value="'#12575E'" />
                </t>
                <div class="col-xs-4">
                     <t t-if="ar_qt_activity_type_global=='todocesped'">
                        <img src="/account_arelux/static/src/img/todocesped_vector.png" style="height: 40px;" />
                    </t>
                    <t t-elif="ar_qt_activity_type_global=='evert'">
                        <img src="/account_arelux/static/src/img/logo_evert.png" style="height: 40px;" />
                    </t>
                    <t t-elif="ar_qt_activity_type_global=='arelux'">
                        <img src="/account_arelux/static/src/img/arelux_top_chemicals.png" style="height: 40px;" />
                    </t>
                    <t t-else="">
                        <img src="/account_arelux/static/src/img/todocesped_vector.png" style="height: 40px;" />
                    </t>
                    <div class='company_data' style="line-height: 15px;font-size: 13px;margin-top: 10px;">
                        <p t-field="company.partner_id.name" style="margin-bottom:0px;" />
                        <p t-field="company.partner_id.vat" style="margin-bottom:0px;" />
                        <p t-field="company.partner_id.street" style="margin-bottom:0px;" />
                        <p style="margin-bottom: 0px;"><span t-field="company.partner_id.zip" /> <span t-field="company.partner_id.city" /></p>
                        <p style="margin-bottom: 0px;">(<span t-field="company.partner_id.state_id" />) <span t-field="company.partner_id.country_id" /></p>
                    </div>
                </div>
                <div class="col-xs-5 col-xs-offset-3" style="text-align:center;">
                    <img src="/account_arelux/static/src/img/arelux_logo.png" style="height:60px;margin-top: 10px;" /><br/>
                    <img src="/account_arelux/static/src/img/logos_empresas_grises.png" style="width: 70%;margin-top: 30px;" />
                </div>
            </t>
            <t t-else="">
                <div class="col-xs-4">
                    <img src="/account_arelux/static/src/img/grupo_arelux.png" style="height: 70px;" /><br/>
                    <img src="/account_arelux/static/src/img/logos_empresas_grises.png" style="width: 100%;margin-top: 20px;" />
                </div>
                <div class="col-xs-5 col-xs-offset-3"></div>
            </t>
        </div>
    </div>
</t>
```

### [report_arelux] external_layout_footer
Original > https://github.com/odoo/odoo/blob/10.0/addons/report/views/layout_templates.xml#L118

#### Original
```
<?xml version="1.0"?>
<t t-name="report.external_layout_footer">
    <div class="footer">
        <div class="text-center" style="border-top: 1px solid black;">
            <ul t-if="not company.custom_footer" class="list-inline">
                <t t-set="company" t-value="company.sudo()"/>
                <li t-if="company.phone">Phone: <span t-field="company.phone"/></li>

                <li t-if="company.fax and company.phone">&amp;bull;</li>
                <li t-if="company.fax">Fax: <span t-field="company.fax"/></li>

                <li t-if="company.email and company.fax or company.email and company.phone">&amp;bull;</li>
                <li t-if="company.email">Email: <span t-field="company.email"/></li>

                <li t-if="company.website and company.email or company.website and company.fax or company.website and company.phone">&amp;bull;</li>
                <li t-if="company.website">Website: <span t-field="company.website"/></li>
            </ul>

            <ul t-if="not company.custom_footer" class="list-inline" name="financial_infos">
                <li t-if="company.vat">TIN: <span t-field="company.vat"/></li>
                <li stle="font-size:9px">Inscrita en el Registro Mercantil de Zaragoza al Tomo 4163, Folio 182, Sección 8, Hoja Z-59796</li>
            </ul>

            <t t-if="company.custom_footer">
                <span t-raw="company.rml_footer"/>
            </t>

            <ul class="list-inline">
                <li>Page:</li>
                <li><span class="page"/></li>
                <li>/</li>
                <li><span class="topage"/></li>
            </ul>
        </div>
    </div>      
</t>
```

#### Modificado
```
<?xml version="1.0"?>
<t t-name="report.external_layout_footer">
    <div class="footer" style="margin-top: 10px;">
        <t t-if="o and 'pack_operation_ids' in o">
            <p style="font-size:10px;">Según RD 728/1998 establece el artículo 18 punto 1 que "El responsable de la entrega del residuo de envase usado para su correcta gestión medioambiental, será el poseedor final". Rogamos se gestionen según normativa vigente Condiciones de venga en www.grupoarelux.com/condiciones-generales-venta/</p>
        </t>
        <t t-if="doc_model=='sale.order'">
            <p style="font-size:10px;font-weight:bold">Te recordamos que el precio de la instalación no está incluido en el presente presupuesto</p>
            <t t-if="o.partner_id.ar_qt_customer_type=='particular'">
                <p style="font-size:10px;">Portes incluidos en entregas a pie de calle.</p>
            </t>
        </t>
        <p style="font-size:10px;">Sus datos son tratados por ARELUX, S.L. para presentarle los servicios solicitados y su facturación, estando legitimados por un contrato. No se cederán datos a terceros, salvo obligación legal. Puedes ejercer sus derechos y solicitar la información completa contactando con info@arelux.com</p>
        <div class="row" style="margin-bottom:10px;">
            <div class="col-xs-3">
                <p style="line-height: 50px;font-weight: bold;color: #e7ad36;font-size: 20px;">Calidad global</p>
            </div>
            <div class="col-xs-8 col-xs-offset-1">
                <t t-if="doc_model=='account.invoice'">
                    <img src="/account_arelux/static/src/img/cesce_mini.jpg" style="height:80px;" />
                </t>
                <img src="/account_arelux/static/src/img/sello_rsa_2017.png" style="height:50px;margin-right: 30px;" />
                <img src="/account_arelux/static/src/img/iso_9001_2015.png" style="height:50px;margin-right: 30px;" />
                <img src="/account_arelux/static/src/img/conformite_europeenn.svg.png" style="height:50px;margin-right: 30px;" />
                <img src="/account_arelux/static/src/img/eco_friendly.png" style="height:50px;" />
            </div>
        </div>
        <div class="row">
            <t t-set="ar_qt_activity_type_global" t-value="arelux" ></t>                    
            <t t-if="o and 'ar_qt_activity_type' in o">
                <t t-set="ar_qt_activity_type_global" t-value="o.ar_qt_activity_type"></t>
            </t>                    
            <t t-elif="o and 'partner_id' in o">                                        
                <t t-set="ar_qt_activity_type_global" t-value="o.partner_id.ar_qt_activity_type"></t>
            </t>
            <t t-if="ar_qt_activity_type_global=='arelux'">                
                <t t-set="custom_color_1" t-value="'#195660'" />
            </t>
            <t t-else="">
                <t t-set="custom_color_1" t-value="'#12575E'" />
            </t>
            <div class="text-center" t-att-style="'background:'+custom_color_1+';color:white;width:100%;font-size:9px;margin-bottom:10px;line-height: 25px;'">
                <ul t-if="not company.custom_footer" class="list-inline" style="list-style-type: none;margin-bottom: 0px;">
                    <t t-set="company" t-value="company.sudo()"/>
                    <li t-if="company.phone">Phone: <span t-field="company.phone"/></li>
                    <!--<li t-if="company.fax and company.phone">&amp;bull;</li>!-->
                    <li t-if="company.fax">Fax: <span t-field="company.fax"/></li>
                    <!--<li t-if="company.email and company.fax or company.email and company.phone">&amp;bull;</li>!-->
                    
                    <t t-if="ar_qt_activity_type_global=='todocesped'">
                        <li t-if="company.email">Email: info@todocesped.es</li>
                    </t>
                    <t t-elif="ar_qt_activity_type_global=='evert'">
                        <li t-if="company.email">Email: info@evert.es</li>
                    </t>
                    <t t-elif="ar_qt_activity_type_global=='arelux'">
                        <li t-if="company.email">Email: info@arelux.com</li>
                    </t>
                    <t t-else="">
                        <li t-if="company.email">Email: info@arelux.com</li>
                    </t>
                    <t t-if="ar_qt_activity_type_global=='todocesped'">
                        <li>www.todocesped.es</li>
                    </t>
                    <t t-elif="ar_qt_activity_type_global=='evert'">
                        <li>www.evert.es</li>
                    </t>
                    <t t-elif="ar_qt_activity_type_global=='arelux'">
                        <li>www.arelux.com</li>
                    </t>
                    <t t-else="">
                        <li>www.arelux.com</li>
                    </t>
                    <li t-if="company.street"><span t-field="company.street"/> <span t-field="company.zip"/> <span t-field="company.city"/></li>
                    <li t-if="company.vat">TIN: <span t-field="company.vat"/></li>
                </ul>
                <t t-if="doc_model=='account.invoice'">
                    <div class="infi_mercantil" style="border-top:1px solid white;">
                        <p>Inscrito en Registro Mercantil de Zaragoza al Tomo 3542, Folio 4, Seccion 8, Hoja Z-44463</p>
                    </div>
                </t>
                <ul t-if="not company.custom_footer" name="financial_infos"></ul>
                <t t-if="company.custom_footer">
                    <span t-raw="company.rml_footer"/>
                </t>
            </div>
        </div>
        <!--
        <ul class="list-inline">
            <li>Page:</li>
            <li><span class="page"/></li>
            <li>/</li>
            <li><span class="topage"/></li>
        </ul>
        !-->
    </div>      
</t>
```

### [report_arelux] report_saleorder_document
Original > https://github.com/odoo/odoo/blob/10.0/addons/sale/report/sale_report_templates.xml#L3

#### Original
```
<?xml version="1.0"?>
<t t-name="sale.report_saleorder_document">
    <t t-call="report.external_layout">
        <t t-set="doc" t-value="doc.with_context({'lang':doc.partner_id.lang})"/>
        <div class="page">
            <div class="oe_structure"/>
            <div class="row">
                <div class="col-xs-6">
                    <strong t-if="doc.partner_shipping_id == doc.partner_invoice_id">Invoicing and shipping address:</strong>
                    <strong t-if="doc.partner_shipping_id != doc.partner_invoice_id">Invoicing address:</strong>
                    <div t-field="doc.partner_invoice_id" t-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;name&quot;, &quot;phone&quot;, &quot;fax&quot;], &quot;no_marker&quot;: True, &quot;phone_icons&quot;: True}"/>
                    <p t-if="doc.partner_id.vat">VAT: <span t-field="doc.partner_id.vat"/></p>
                    <div t-if="doc.partner_shipping_id != doc.partner_invoice_id" class="mt8">
                        <strong>Shipping address:</strong>
                        <div t-field="doc.partner_shipping_id" t-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;name&quot;, &quot;phone&quot;, &quot;fax&quot;], &quot;no_marker&quot;: True, &quot;phone_icons&quot;: True}"/>
                        <p t-if="doc.partner_id.vat">VAT: <span t-field="doc.partner_id.vat"/></p>
                    </div>
                </div>
                <div class="col-xs-5 col-xs-offset-1">
                    <div t-field="doc.partner_id" t-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;name&quot;], &quot;no_marker&quot;: True}"/>
                </div>
            </div>

            <h2>
                <span t-if="doc.state not in ['draft','sent']">Order # </span>
                <span t-if="doc.state in ['draft','sent']">Quotation # </span>
                <span t-field="doc.name"/>
            </h2>

            <div class="row mt32 mb32" id="informations">
                <div t-if="doc.client_order_ref" class="col-xs-3">
                    <strong>Your Reference:</strong>
                    <p t-field="doc.client_order_ref"/>
                </div>
                <div t-if="doc.date_order" class="col-xs-3">
                    <strong t-if="doc.state not in ['draft','sent']">Date Ordered:</strong>
                    <strong t-if="doc.state in ['draft','sent']">Quotation Date:</strong>
                    <p t-field="doc.date_order"/>
                </div>
                <div t-if="doc.user_id.name" class="col-xs-3">
                    <strong>Salesperson:</strong>
                    <p t-field="doc.user_id"/>
                </div>
                <div name="payment_term" t-if="doc.payment_term_id" class="col-xs-3">
                    <strong>Payment Terms:</strong>
                    <p t-field="doc.payment_term_id"/>
                </div>
            </div>

            <!-- Is there a discount on at least one line? -->
            <t t-set="display_discount" t-value="any([l.discount for l in doc.order_line])"/>

            <t t-foreach="doc.order_lines_layouted()" t-as="page">
                <table class="table table-condensed">
                    <thead>
                        <tr>
                            <th>Description</th>
                            <th class="text-right">Quantity</th>
                            <th class="text-right">Unit Price</th>
                            <th t-if="display_discount" class="text-right" groups="sale.group_discount_per_so_line">Disc.(%)</th>
                            <th class="text-right">Taxes</th>
                            <th class="text-right" groups="sale.group_show_price_subtotal">Price</th>
                            <th class="text-right price_tax_included" groups="sale.group_show_price_total">Total Price</th>
                        </tr>
                   </thead>
                   <tbody class="sale_tbody">
                        <t t-foreach="page" t-as="layout_category">

                            <t t-if="layout_category_size &gt; 1 or page_size &gt; 1" groups="sale.group_sale_layout">
                                <tr class="active">
                                    <td colspan="7" style="font-weight: bold; border-bottom: 1px solid black;">&amp;bull;
                                        <t t-esc="layout_category['name']"/>
                                    </td>
                                </tr>
                            </t>

                            <!-- Lines associated -->
                            <t t-foreach="layout_category['lines']" t-as="l">
                                <tr>
                                    <td><span t-field="l.name"/></td>
                                    <td class="text-right">
                                        <span t-field="l.product_uom_qty"/>
                                        <span t-field="l.product_uom" groups="product.group_uom"/>
                                    </td>
                                    <td class="text-right">
                                        <span t-field="l.price_unit"/>
                                    </td>
                                    <td t-if="display_discount" class="text-right" groups="sale.group_discount_per_so_line">
                                        <span t-field="l.discount"/>
                                    </td>
                                    <td class="text-right">
                                        <span t-esc="', '.join(map(lambda x: (x.description or x.name), l.tax_id))"/>
                                    </td>
                                    <td class="text-right" groups="sale.group_show_price_subtotal">
                                        <span t-field="l.price_subtotal" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                                    </td>
                                    <td class="text-right" groups="sale.group_show_price_total">
                                        <span t-field="l.price_total" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                                    </td>
                                </tr>
                            </t>

                            <t t-if="(layout_category_size &gt; 1 or page_size &gt; 1) and layout_category['subtotal']" groups="sale.group_sale_layout">
                                <tr class="text-right">
                                    <td colspan="6">
                                        <strong>Subtotal: </strong>
                                        <t t-set="subtotal" t-value="sum(line.price_subtotal for line in layout_category['lines'])"/>
                                        <span t-esc="subtotal" t-options="{'widget': 'monetary', 'display_currency': doc.pricelist_id.currency_id}"/>
                                    </td>
                                </tr>
                            </t>

                        </t>
                    </tbody>
                </table>

                <t t-if="page_index &lt; page_size - 1" groups="sale.group_sale_layout">
                    <p style="page-break-before:always;"> </p>
                </t>
            </t>

            <div class="row" name="total">
                <div class="col-xs-4 pull-right">
                    <table class="table table-condensed">
                        <tr class="border-black">
                            <td><strong>Total Without Taxes</strong></td>
                            <td class="text-right">
                                <span t-field="doc.amount_untaxed" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                            </td>
                        </tr>
                        <t t-foreach="doc._get_tax_amount_by_group()" t-as="amount_by_group">
                            <tr>
                                <td><span t-esc="amount_by_group[0] or 'Taxes'"/></td>
                                <td class="text-right">
                                    <span t-esc="amount_by_group[1]" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                                </td>
                            </tr>
                        </t>
                        <tr class="border-black">
                            <td><strong>Total</strong></td>
                            <td class="text-right">
                                <span t-field="doc.amount_total" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>

            <p t-field="doc.note"/>
            <p t-if="doc.payment_term_id.note">
                <span t-field="doc.payment_term_id.note"/>
            </p>
            <p id="fiscal_position_remark" t-if="doc.fiscal_position_id and doc.fiscal_position_id.note">
                <strong>Fiscal Position Remark:</strong>
                <span t-field="doc.fiscal_position_id.note"/>
            </p>
            <div class="oe_structure"/>
        </div>
    </t>
</t>
```

#### Modificado
```
<?xml version="1.0"?>
<t t-name="sale.report_saleorder_document">
    <t t-call="report.external_layout">
        <t t-set="doc" t-value="doc.with_context({'lang':doc.partner_id.lang})"/>
        <t t-if="doc.ar_qt_activity_type=='arelux'">                
            <t t-set="custom_color_1" t-value="'#195660'" />
            <t t-set="custom_color_2" t-value="'#307584'" />
            <t t-set="custom_color_3" t-value="'#4996AA'" />
            <t t-set="custom_color_4" t-value="'#60B2C4'" />
            <t t-set="custom_color_5" t-value="'#8ECCD3'" />
        </t>
        <t t-else="">
            <t t-set="custom_color_1" t-value="'#12575E'" />
            <t t-set="custom_color_2" t-value="'#076973'" />
            <t t-set="custom_color_3" t-value="'#057473'" />
            <t t-set="custom_color_4" t-value="'#008C73'" />
            <t t-set="custom_color_5" t-value="'#18A379'" />
        </t>
        <div class="page">
            <div class="oe_structure"/>
            <div class="row" style="margin-bottom: 20px;">
                <div class="col-xs-6" style="margin-top:10px;">
                    <t t-if="doc.proforma==True">
                        <div class='title_bar' t-att-style="'background:'+custom_color_1+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;'">Direccion de facturación</div>                    
                        <div style="margin-left:15px;margin-top: 5px;">
                           <p t-field="doc.partner_invoice_id.name" style="margin-bottom:0px;" />
                           <p t-field="doc.partner_invoice_id.street" style="margin-bottom:0px;" />
                           <p style="margin-bottom:0px;"><span t-field="doc.partner_invoice_id.zip" /> <span t-field="doc.partner_invoice_id.city" /></p>
                           <p t-field="doc.partner_invoice_id.country_id" style="margin-bottom:0px;" />
                           <t t-if="doc.partner_invoice_id.phone">
                                <p style="margin-bottom:0px;">
                                    <i class="fa fa-phone"></i>
                                    <span t-field="doc.partner_invoice_id.phone" />
                                </p>
                           </t>
                           <p t-if="doc.partner_invoice_id.vat" style="margin-bottom: 0px;">NIF: <span t-field="doc.partner_invoice_id.vat"/></p>
                        </div>
                    </t>
                    <t t-if="doc.proforma==False">
                        <div class='title_bar' t-att-style="'background:'+custom_color_1+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;'">Cliente</div>                    
                        <div style="margin-left:15px;margin-top: 5px;">
                           <p t-field="doc.partner_id.name" style="margin-bottom:0px;" />
                           <p t-field="doc.partner_id.street" style="margin-bottom:0px;" />
                           <p style="margin-bottom:0px;"><span t-field="doc.partner_id.zip" /> <span t-field="doc.partner_id.city" /></p>
                           <p t-field="doc.partner_id.country_id" style="margin-bottom:0px;" />
                           <t t-if="doc.partner_id.phone">
                                <p style="margin-bottom:0px;">
                                    <i class="fa fa-phone"></i>
                                    <span t-field="doc.partner_id.phone"  />
                                </p>
                           </t>
                           <p t-if="doc.partner_id.vat" style="margin-bottom: 0px;">NIF: <span t-field="doc.partner_id.vat"/></p>
                        </div>
                    </t>
                </div>
                <div class="col-xs-6" style="padding-right: 0px;padding-left:0px;margin-top:10px;">
                    <div t-if="doc.partner_shipping_id != doc.partner_id" class='title_bar' t-att-style="'background:'+custom_color_1+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;'">Direccion de envío</div>                    
                    <t t-if="doc.partner_shipping_id != doc.partner_id">
                        <div style="margin-left:15px;margin-top: 5px;">
                           <p t-field="doc.partner_shipping_id.name" style="margin-bottom:0px;" />
                           <p t-field="doc.partner_shipping_id.street" style="margin-bottom:0px;" />
                           <p style="margin-bottom:0px;"><span t-field="doc.partner_shipping_id.zip" /> <span t-field="doc.partner_shipping_id.city" /></p>
                           <p t-field="doc.partner_shipping_id.country_id" style="margin-bottom:0px;" />
                           <t t-if="doc.partner_shipping_id.phone">
                                <p style="margin-bottom:0px;">
                                    <i class="fa fa-phone"></i>
                                    <span t-field="doc.partner_shipping_id.phone" />
                                </p>
                           </t>
                           <p t-if="doc.partner_shipping_id.vat" style="margin-bottom: 0px;">NIF: <span t-field="doc.partner_shipping_id.vat"/></p>
                        </div>
                    </t>
                </div>
            </div>
            <div class="row" style="margin-bottom: 15px;">
                <div class="col-xs-6">
                    <h4 style="font-weight:bold;margin-bottom:0px;">
                    <t t-if="doc.proforma==False">Presupuesto</t>
                    <t t-if="doc.proforma==True">Factura Proforma</t>
                    # <span t-field="doc.name"/>
                    </h4>
                </div>
                <div class="col-xs-3" style="padding-right: 0px;padding-left: 0px;">
                    <t t-if="doc.payment_term_id">
                        <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;width:100%;padding:5px 5px 5px 15px;margin-bottom: 5px;'">Plazo de pago</div>                    
                        <p t-field="doc.payment_term_id" style="padding-left: 15px;" />
                    </t>
                </div>
                <div class="col-xs-3" style="padding-right: 0px;">
                    <t t-if="doc.payment_mode_id">
                        <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;width:100%;padding:5px 5px 5px 15px;margin-bottom: 5px;'">Forma de pago</div>
                        <p t-field="doc.payment_mode_id" style="padding-left: 15px;" />
                    </t>
                </div>
            </div>
            <div class="row" id="informations" style="margin-bottom: 10px;">
                <div class="col-xs-6">
                    <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;margin-bottom: 5px;'">Fecha de presupuesto</div>    
                    <p t-field="doc.date_order" style="padding-left: 15px;" />
                </div>
                <div class="col-xs-3" style="text-align:center;padding-right:0px;padding-left: 0px;">
                    <t t-if="doc.user_id.name">
                        <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Asesor comercial</div>    
                        <p style="margin-bottom: 0px;"><span t-field="doc.user_id"/> <span t-field="doc.user_id.commercial_phone"/></p>
                        <p t-field="doc.user_id.commercial_email"/>
                    </t>
                </div>    
                <div class="col-xs-3" style="text-align:center;padding-right: 0px;">
                    <t t-if="doc.validity_date">
                        <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Fecha de caducidad</div>                        
                        <p t-field="doc.validity_date"/>
                    </t>
                </div>
            </div>
            <!-- Is there a discount on at least one line? -->
            <t t-set="display_discount" t-value="any([l.discount for l in doc.order_line])"/>
            <t t-foreach="doc.order_lines_layouted()" t-as="page">
                <div class="row" id="table_header">
                    <div class="col-xs-6">
                        <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;padding-left: 15px;width:100%;height: 40px;line-height: 40px;'">Descripción</div>
                    </div>
                    <div class="col-xs-1" style="padding-right: 0px;padding-left: 0px;">
                        <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;text-align:center;'">Cantidad<br/><small>m2/Kg/L</small></div>
                    </div>
                    <div class="col-xs-2" style="padding-right:0px;">
                        <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;height: 40px;line-height: 40px;text-align:center;'">Precio unitario</div>
                    </div>
                    <div class="col-xs-1" style="padding-right:0px;">
                        <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;height: 40px;line-height: 40px;text-align:center;'">Dto.</div>
                    </div>
                    <div class="col-xs-2" style="padding-right: 0px;">
                        <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;height: 40px;line-height: 40px;text-align:center;'">Importe</div>
                    </div>
                </div>
                <t t-foreach="page" t-as="layout_category">
                    <t t-foreach="layout_category['lines']" t-as="l">
                        <div class="row" style="padding: 5px 0px;">
                            <div class="col-xs-6">
                               <span t-field="l.name" style="padding-left:15px" />
                            </div>
                            <div class="col-xs-1" style="text-align:center;padding-left: 0px;padding-right: 0px;">
                                <t t-if="l.product_uom_qty>0">
                                    <span t-field="l.product_uom_qty"/>
                                </t>
                            </div>
                            <div class="col-xs-2" style="text-align:center;padding-right:0px;">
                                <t t-if="l.price_unit>0">
                                    <span t-field="l.price_unit"/>
                                </t>
                            </div>
                            <div class="col-xs-1" groups="sale.group_discount_per_so_line" style="text-align:center;padding-right:0px;">
                                <t t-if="l.discount>0">
                                   <span t-field="l.discount"/>%
                                </t>
                            </div>
                            <div class="col-xs-2" style="text-align:right;" groups="sale.group_show_price_subtotal">
                                <t t-if="l.price_subtotal>0">
                                    <span t-field="l.price_subtotal" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                                </t>
                            </div>
                        </div>
                    </t>
                </t>
                <t t-if="doc.show_total==True">
                    <div class="row" style="margin-top: 20px;">
                        <div class="col-xs-5"></div>
                        <div class="col-xs-2"></div>
                        <div class="col-xs-5" style="border-top:1px solid black;">
                            <div class="row" style="padding-bottom:5px;">
                                <div class="col-xs-8">Base imponible</div>
                                <div class="col-xs-4" style="text-align:right;">
                                    <span t-field="doc.amount_untaxed" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                                </div>
                            </div>
                            <div class="row" style="padding-bottom:5px;">
                                <!--<div class="col-xs-8">Iva</div>!-->
                                <div class="col-xs-8">
                                    <t t-set="order_taxes" t-value="[]"/>
                                    <t t-foreach="page" t-as="layout_category">
                                        <t t-foreach="layout_category['lines']" t-as="l">
                                            <t t-foreach="l.tax_id" t-as="tax">
                                                <t t-set="order_taxes" t-value="list(set([tax.name]))"/>
                                            </t>
                                        </t>
                                    </t>
                                    <t t-foreach="order_taxes" t-as="order_tax">
                                        <span t-esc="order_tax"/>
                                    </t>
                                </div>
                                <div class="col-xs-4" style="text-align:right;">
                                    <span t-field="doc.amount_tax" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                                </div>
                            </div>
                            <div name="total" class="row" t-att-style="'border: 1px solid '+custom_color_3+';'">
                                <div class="col-xs-8" t-att-style="'background:'+custom_color_4+';color:white;font-weight:bold;'">Total</div>
                                <div class="col-xs-4" style="text-align:right;font-weight:bold;">
                                    <span t-field="doc.amount_total" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: doc.pricelist_id.currency_id}"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </t>
                <t t-if="doc.show_total==False">
                    <div class="row">
                        <p class="text-right" style="font-size: 11px;">*21% IVA no incluido</p>
                    </div>
                </t>
            </t>
            <div class="row" style="margin-left: 0px;margin-right: 0px;">
                <p style="font-size: 11px;">*Portes gratuitos en Península en pedidos superiores a 150 + IVA. Resto de zonas a consultar</p>
            </div>
            <div class="row">
                <div class="col-xs-7" style="padding-left: 0px;">
                    <t t-if="doc.state!='sale'">
                        <t t-if="doc.opportunity_id!=0">
                            <t t-foreach="doc.opportunity_id.order_ids" t-as="order">
                                <t t-if="order.state=='sale' and order.amount_total==0">
                                    <t t-foreach="order.picking_ids" t-as="picking">
                                        <t t-if="picking.shipping_expedition_id!=0">
                                            <div>
                                                <strong>Expedición <span t-field="picking.carrier_id"/>:</strong> <span t-field="picking.shipping_expedition_id.delivery_code"/>
                                            </div>
                                        </t>
                                    </t>                        
                                </t>
                            </t>
                        </t>
                    </t>
                </div>
                <div class="col-xs-5" style="padding-left: 0px;padding-right: 0px;padding-left: 0px;padding-right: 0px;">
                    <div class='title_bar' t-att-style="'background:'+custom_color_5+';color: white;font-weight: bold;padding: 5px;width:100%%;text-align:center;'">Observaciones</div>                                                
                    <div t-att-style="'border-left: 1px solid '+custom_color_5+';border-right:1px solid '+custom_color_5+';border-bottom:1px solid  '+custom_color_5+';padding: 10px;'">
                        <p style="font-size:11px;" t-field="doc.note"/>
                        <t t-if="doc.proforma==True">
                            <t t-if="doc.picking_note">
                                <div style="padding-top:10px;">
                                    <p style="font-size:11px;" t-field="doc.picking_note"/>        
                                </div>
                            </t>
                        </t>
                    </div>
                </div>
             </div>
             <!--
             <p id="fiscal_position_remark" t-if="doc.fiscal_position_id and doc.fiscal_position_id.note">
                 <strong>Fiscal Position Remark:</strong>
                 <span t-field="doc.fiscal_position_id.note"/>
             </p>
             !-->
            <div class="oe_structure"/>
        </div>
    </t>
</t>
```

### [report_arelux] report_delivery_document
Original > https://github.com/odoo/odoo/blob/10.0/addons/stock/report/report_deliveryslip.xml#L4

#### Original
```
<?xml version="1.0"?>
<t t-name="stock.report_delivery_document">
        <t t-call="report.html_container">
            <t t-call="report.external_layout">
                <t t-set="o" t-value="o.with_context({'lang':o.partner_id.lang})"/>
                <div class="page">
                    <div class="row" name="customer_address">
                        <div class="col-xs-4 pull-right">
                            <div>
                                <span><strong>Customer Address:</strong></span>
                            </div>
                            <div t-if="o.move_lines and o.move_lines[0].partner_id" name="partner_header">
                                <div t-field="o.move_lines[0].partner_id" t-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;name&quot;, &quot;phone&quot;, &quot;fax&quot;], &quot;no_marker&quot;: True}"/>
                            </div>
                            <div t-if="not (o.move_lines and o.move_lines[0].partner_id) and o.partner_id" name="partner_header">
                                <div t-field="o.partner_id" t-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;name&quot;, &quot;phone&quot;, &quot;fax&quot;], &quot;no_marker&quot;: True}"/>
                            </div>
                        </div>
                    </div>
                    <h2>
                        <span t-field="o.name"/>
                    </h2>
                    <table class="table table-condensed">
                        <thead>
                            <tr>
                                <th t-if="o.origin"><strong>Order (Origin)</strong></th>
                                <th name="td_sched_date_h">
                                    <strong>Date</strong>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td t-if="o.origin">
                                    <span t-field="o.origin"/>
                                </td>
                                <td name="td_sched_date">
                                   <t t-if="o.state == 'done'">
                                        <span t-field="o.date_done"/>
                                   </t>
                                   <t t-if="o.state != 'done'">
                                        <span t-field="o.min_date"/>
                                   </t>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table class="table table-condensed mt48" t-if="not o.pack_operation_ids">
                        <thead>
                            <tr>
                                <th><strong>Product</strong></th>
                                <th><strong>Ordered Quantity</strong></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr t-foreach="o.move_lines" t-as="move">
                                <td><span t-field="move.product_id"/></td>
                                <td>
                                    <span t-field="move.ordered_qty"/>
                                    <span t-field="move.product_uom"/>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <t t-set="backorder" t-value="False"/>
                    <table class="table table-condensed mt48" t-if="o.pack_operation_ids">
                        <t t-set="has_serial_number" t-value="o.pack_operation_ids.filtered('pack_lot_ids')" groups="stock.group_production_lot"/>
                        <thead>
                            <tr>
                                <th><strong>Product</strong></th>
                                <th name="lot_serial" t-if="has_serial_number">
                                    <span class="pull-left">Lot/Serial Number</span>
                                </th>
                                <th class="text-center"><strong>Ordered Quantity</strong></th>
                                <th t-if="any([pack_operation.state == 'done' for pack_operation in o.pack_operation_ids])" class="text-right">
                                        <strong>Delivered Quantity</strong>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr t-foreach="o.pack_operation_ids" t-as="pack_operation">
                                <td>
                                    <span t-field="pack_operation.product_id"/>
                                    <t t-if="not pack_operation.product_id and pack_operation.package_id">
                                        <span t-field="pack_operation.package_id"/>
                                    </t>
                                </td>
                                <t t-if="has_serial_number">
                                    <td t-if="pack_operation.pack_lot_ids">
                                        <table class="table table-condensed" t-if="pack_operation.pack_lot_ids">
                                            <tr t-foreach="pack_operation.pack_lot_ids" t-as="packlot">
                                                <td>
                                                    <span t-field="packlot.lot_id"/>
                                                    <t t-if="not packlot.lot_id">
                                                        <span t-field="packlot.lot_name"/>
                                                    </t>
                                                </td>
                                                <td name="lot_qty">
                                                    <span t-field="packlot.qty"/>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td t-if="not pack_operation.pack_lot_ids"/>
                                </t>
                                <td class="text-center">
                                    <span t-if="pack_operation.package_id">:</span>
                                    <span t-field="pack_operation.package_id"/>
                                    <span t-field="pack_operation.ordered_qty"/>
                                    <t t-if="pack_operation.linked_move_operation_ids">
                                        <span t-field="pack_operation.linked_move_operation_ids[0].move_id.product_uom"/>
                                    </t>
                                    <t t-else="1">
                                        <span t-field="pack_operation.product_uom_id"/>
                                    </t>
                                </td>
                                <td class="text-right" t-if="pack_operation.state == 'done'">
                                    <t t-if="pack_operation.ordered_qty != pack_operation.qty_done_uom_ordered">
                                        <t t-set="backorder" t-value="True"/>
                                    </t>
                                    <span t-field="pack_operation.qty_done_uom_ordered"/>
                                    <t t-if="pack_operation.linked_move_operation_ids">
                                        <span t-field="pack_operation.linked_move_operation_ids[0].move_id.product_uom"/>
                                    </t>
                                    <t t-else="1">
                                        <span t-field="pack_operation.product_uom_id"/>
                                    </t>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p t-if="o.backorder_id">
                        This shipment is a backorder of <t t-esc="o.backorder_id.name"/>.
                    </p>
                    <p>
                        <t t-if="backorder">
                            All items couldn't be shipped, the remaining ones will be shipped as soon as they become available.
                        </t>
                    </p>
                </div>
            </t>
         </t>
    </t>
```

#### Modificado
```
<?xml version="1.0"?>
<t t-name="stock.report_delivery_document">
        <t t-call="report.html_container">
            <t t-call="report.external_layout">
                <t t-set="o" t-value="o.with_context({'lang':o.partner_id.lang})"/>
                <t t-if="o.ar_qt_activity_type=='arelux'">                
                    <t t-set="custom_color_1" t-value="'#195660'" />
                    <t t-set="custom_color_2" t-value="'#307584'" />
                    <t t-set="custom_color_3" t-value="'#4996AA'" />
                    <t t-set="custom_color_4" t-value="'#60B2C4'" />
                    <t t-set="custom_color_5" t-value="'#8ECCD3'" />
                </t>
                <t t-else="">
                    <t t-set="custom_color_1" t-value="'#12575E'" />
                    <t t-set="custom_color_2" t-value="'#076973'" />
                    <t t-set="custom_color_3" t-value="'#057473'" />
                    <t t-set="custom_color_4" t-value="'#008C73'" />
                    <t t-set="custom_color_5" t-value="'#18A379'" />
                </t>
                <div class="page">
                    <div class="row">
                        <div class="col-xs-5"></div>
                        <div class="col-xs-6 col-xs-offset-1" style="padding-right:0px;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_1+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;'">Dirección de entrega</div>                    
                            <div style="margin-left:15px;margin-top: 5px;">
                               <p t-field="o.partner_id.name" style="margin-bottom:0px;" />
                               <p t-field="o.partner_id.street" style="margin-bottom:0px;" />
                               <p style="margin-bottom:0px;"><span t-field="o.partner_id.zip" /> <span t-field="o.partner_id.city" /></p>
                               <p t-field="o.partner_id.country_id" style="margin-bottom:0px;" />
                               <t t-if="o.partner_id.phone">
                                    <p style="margin-bottom:0px;">
                                        <i class="fa fa-phone"></i>
                                        <span t-field="o.partner_id.phone" />
                                    </p>
                               </t>
                               <p t-if="o.partner_id.vat" style="margin-bottom: 0px;">NIF: <span t-field="o.partner_id.vat"/></p>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-xs-5">
                            <h4 style="font-weight:bold;"><span t-field="o.name"/></h4>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-xs-5">
                            <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;margin-bottom: 5px;'">Cliente</div>    
                            <t t-if="o.partner_id.parent_id.id>0">
                                <p t-field="o.partner_id.parent_id.name" style="margin-bottom:0px;margin-left: 15px;" />
                            </t>
                            <t t-if="o.partner_id.parent_id.id==0">
                                <p t-field="o.partner_id.name" style="margin-bottom:0px;margin-left: 15px;" />
                            </t>
                        </div>
                        <div class="col-xs-3">
                            <div class="row">
                                <div class="col-xs-6" style="text-align:center;padding-left:0px;padding-right:0px;">
                                    <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Origen</div>    
                                    <p t-field="o.origin" />
                                </div>
                                <div class="col-xs-6" style="text-align:center;padding-right: 0px;">
                                    <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Fecha</div>    
                                    <t t-if="o.management_date">
                                        <p t-esc="o.management_date[:-9]" t-options="{&quot;widget&quot;: &quot;date&quot;}" />
                                    </t>
                                </div>
                            </div>
                        </div>
                        <div class="col-xs-2" style="text-align:center;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Transporte</div>    
                            <p t-field="o.carrier_id" />
                        </div>
                        <div class="col-xs-1" style="text-align:center;padding-left:0px;padding-right:0px;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Peso</div>    
                            <span t-field="o.weight"/>
                            <span t-field="o.weight_uom_id"/>
                        </div>
                        <div class="col-xs-1" style="text-align:center;padding-right: 0px;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Bultos</div>    
                            <p t-field="o.number_of_packages" />
                        </div>
                    </div>
                    <div class="row" id="table_header" style="margin-top:20px;">
                        <div class="col-xs-8" style="padding-right: 0px;">
                            <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;height: 40px;line-height: 40px;padding-left:15px;'">Descripción</div>
                        </div>
                        <div class="col-xs-2">
                            <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;text-align:center;height:40px;'">Cantidad<br/><small>m2/L</small></div>
                        </div>
                        <div class="col-xs-2" style="padding-right: 0px;padding-left: 0px;">
                            <t t-if="o.total_cashondelivery>0">
                                <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;height: 40px;line-height: 40px;text-align:center;'">Importe total</div>
                            </t>
                        </div>
                    </div>
                    <t t-foreach="o.pack_operation_ids" t-as="move">
                       <div class="row" style="padding: 5px 0px;">
                           <div class="col-xs-8" style="margin-left: 15px;margin-right: -15px;">
                              <span t-field="move.name"/>
                           </div>
                           <div class="col-xs-2" style="text-align:center;padding-right: 0px;">
                               <span t-field="move.qty_done"/>
                           </div>
                            <div class="col-xs-2" style="text-align:right;padding-left:0px;">
                                <t t-if="o.total_cashondelivery>0">
                                     <t t-if="o.order_id">
                                         <t t-set="price_unit_line" t-value="0"/>
                                         <t t-foreach="o.order_id.order_line" t-as="line">
                                             <t t-if="line.product_id.id==move.product_id.id">
                                                 <t t-set="price_unit_line" t-value="line.price_subtotal"/>        
                                             </t>
                                         </t>
                                         <t t-if="price_unit_line>0">
                                             <span t-esc="price_unit_line" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                         </t>
                                     </t>
                                </t>
                            </div>
                       </div>
                   </t>
                   <t t-if="o.total_cashondelivery>0">
                       <div class="row">
                           <div class="col-xs-7"></div>
                           <div class="col-xs-5" style="border-top:1px solid black;margin-top: 20px;">
                               <div class="row" style="padding-bottom:5px;">
                                   <div class="col-xs-8">Base imponible</div>
                                   <div class="col-xs-4" style="text-align:right;">
                                       <span t-field="o.order_id.amount_untaxed" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                   </div>
                               </div>
                               <div class="row" style="padding-bottom:5px;">
                                   <!--<div class="col-xs-8">Iva</div>!-->
                                   <div class="col-xs-8">
                                       <t t-set="order_taxes" t-value="[]"/>
                                       <t t-foreach="o.order_id.order_line" t-as="l">
                                           <t t-foreach="l.tax_id" t-as="tax">
                                               <t t-set="order_taxes" t-value="list(set([tax.description]))"/>
                                           </t>
                                       </t>
                                       <t t-foreach="order_taxes" t-as="order_tax">
                                           <span t-esc="order_tax"/>
                                       </t>
                                    </div>
                                   <div class="col-xs-4" style="text-align:right;">
                                       <span t-field="o.order_id.amount_tax" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                   </div>
                               </div>
                               <div name="total" class="row" t-att-style="'border: 1px solid '+custom_color_4+';'">
                                   <div class="col-xs-8" t-att-style="'background:'+custom_color_4+';color:white;font-weight:bold;'">Total</div>
                                   <div class="col-xs-4" style="text-align:right;font-weight:bold;">
                                       <span t-field="o.order_id.amount_total" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                   </div>
                               </div>
                           </div>
                       </div>
                   </t>
                   <div class="row" style="margin-left: 0px;margin-right: 0px;margin-top: 30px;">
                        <p style="font-size: 11px;"><b>IMPORTANTE - Comprobar Estado Mercancía.</b></p>   
                        <p style="font-size: 11px;">Esta mercancía ha salido de nuestro almacén en perfecto estado. Le rogamos compruebe, en el momento de la recepción, si existe algún desperfecto <b>anótelo en el albarán de entrega</b> de la empresa de transporte y <b>efectúe inmediatamente la reclamación</b> oportuna a la agencia de transporte y a Grupo Arelux.</p>
                        <p style="font-size: 11px;"><b>Grupo Arelux no se responsabiliza del estado de la mercancía pasadas 24 horas.</b></p>
                    </div>
                    <div class="row" style="margin-top:30px;">
                        <div class="col-xs-6">
                            <t t-if="o.total_cashondelivery>0">
                                <div class="title_bar" t-att-style="'background:'+custom_color_5+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;'">PEDIDO CONTRAREEMBOLSO</div>
                                <div class="row" style="padding:5px 0px;">
                                    <div class="col-xs-6" style="margin-left: 15px;font-weight:bold;">CANTIDAD A ABONAR</div>
                                    <div class="col-xs-4" style="text-align: right;font-weight: bold;font-size: 15px;">
                                        <span t-field="o.total_cashondelivery" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                    </div>
                                </div>
                            </t>
                        </div>
                        <div class="col-xs-6" style="padding-left:0px;padding-right:0px;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_5+';color: white;font-weight: bold;padding: 5px;width:100%%;text-align:center;'">Observaciones</div>                                                
                            <div t-att-style="'border-left:1px solid  '+custom_color_5+';border-right:1px solid  '+custom_color_5+';border-bottom:1px solid  '+custom_color_5+';padding: 10px;'">
                                <p style="font-size:11px;" t-field="o.sale_order_note"/>
                            </div>
                        </div>
                    </div>
                </div>
            </t>
         </t>
    </t>
```    

### [report_arelux] report_purchaseorder

#### Original
```
<?xml version="1.0"?>
<t t-name="purchase.report_purchaseorder">
    <t t-call="report.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="purchase.report_purchaseorder_document" t-lang="o.partner_id.lang"/>
        </t>
    </t>
</t>
```

### [report_arelux] report_purchaseorder_document
Original > https://github.com/odoo/odoo/blob/10.0/addons/purchase/report/purchase_order_templates.xml#L3

#### Original
```
<?xml version="1.0"?>
<t t-name="purchase.report_purchaseorder_document">
    <t t-call="report.external_layout">
        <t t-set="o" t-value="o.with_context({'lang':o.partner_id.lang})"/>
        <div class="page">
            <div class="oe_structure"/>
            <div class="row">
                <div class="col-xs-6">
                    <strong>Shipping address:</strong>
                    <div t-if="o.dest_address_id">
                        <div t-field="o.dest_address_id" t-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;name&quot;, &quot;phone&quot;, &quot;fax&quot;], &quot;no_marker&quot;: True, &quot;phone_icons&quot;: True}"/>
                    </div>

                    <div t-if="not o.dest_address_id and o.picking_type_id and o.picking_type_id.warehouse_id">
                        <span t-field="o.picking_type_id.warehouse_id.name"/>
                        <div t-field="o.picking_type_id.warehouse_id.partner_id" t-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;phone&quot;, &quot;fax&quot;], &quot;no_marker&quot;: True, &quot;phone_icons&quot;: True}"/>
                    </div>
                </div>
                <div class="col-xs-5 col-xs-offset-1">
                    <div t-field="o.partner_id" t-options="{&quot;widget&quot;: &quot;contact&quot;, &quot;fields&quot;: [&quot;address&quot;, &quot;name&quot;, &quot;phone&quot;, &quot;fax&quot;], &quot;no_marker&quot;: True, &quot;phone_icons&quot;: True}"/>
                        <p t-if="o.partner_id.vat">VAT: <span t-field="o.partner_id.vat"/></p>
                </div>
            </div>

            <h2 t-if="o.state != 'draft'">Purchase Order Confirmation #<span t-field="o.name"/></h2>
            <h2 t-if="o.state == 'draft'">Request for Quotation #<span t-field="o.name"/></h2>

            <div class="row mt32 mb32">
                <div t-if="o.name" class="col-xs-3">
                    <strong>Our Order Reference:</strong>
                    <p t-field="o.name"/>
                </div>
                <div t-if="o.partner_ref" class="col-xs-3">
                    <strong>Your Order Reference</strong>
                    <p t-field="o.partner_ref"/>
                </div>
                <div t-if="o.date_order" class="col-xs-3">
                    <strong>Order Date:</strong>
                    <p t-field="o.date_order"/>
                </div>
            </div>

            <table class="table table-condensed">
                <thead>
                    <tr>
                        <th><strong>Description</strong></th>
                        <th><strong>Taxes</strong></th>
                        <th class="text-center"><strong>Date Req.</strong></th>
                        <th class="text-right"><strong>Qty</strong></th>
                        <th class="text-right"><strong>Unit Price</strong></th>
                        <th class="text-right"><strong>Net Price</strong></th>
                    </tr>
                </thead>
                <tbody>
                    <tr t-foreach="o.order_line" t-as="line">
                        <td>
                            <span t-field="line.name"/>
                        </td>
                        <td>
                            <span t-esc="', '.join(map(lambda x: x.name, line.taxes_id))"/>
                        </td>
                        <td class="text-center">
                            <span t-field="line.date_planned"/>
                        </td>
                        <td class="text-right">
                            <span t-field="line.product_qty"/>
                            <span t-field="line.product_uom.name" groups="product.group_uom"/>
                        </td>
                        <td class="text-right">
                            <span t-field="line.price_unit"/>
                        </td>
                        <td class="text-right">
                            <span t-field="line.price_subtotal" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.currency_id}"/>
                        </td>
                    </tr>
                </tbody>
            </table>

            <div class="row">
                <div class="col-xs-4 pull-right">
                    <table class="table table-condensed">
                        <tr class="border-black">
                            <td><strong>Total Without Taxes</strong></td>
                            <td class="text-right">
                                <span t-field="o.amount_untaxed" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.currency_id}"/>
                            </td>
                        </tr>
                        <tr>
                            <td>Taxes</td>
                            <td class="text-right">
                                <span t-field="o.amount_tax" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.currency_id}"/>
                            </td>
                        </tr>
                        <tr class="border-black">
                            <td><strong>Total</strong></td>
                            <td class="text-right">
                                <span t-field="o.amount_total" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.currency_id}"/>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>

            <p t-field="o.notes"/>
            <div class="oe_structure"/>
        </div>
    </t>
</t>
```

#### Modificado
```
<?xml version="1.0"?>
<t t-name="stock.report_delivery_document">
        <t t-call="report.html_container">
            <t t-call="report.external_layout">
                <t t-set="o" t-value="o.with_context({'lang':o.partner_id.lang})"/>
                <t t-if="o.ar_qt_activity_type=='arelux'">                
                    <t t-set="custom_color_1" t-value="'#195660'" />
                    <t t-set="custom_color_2" t-value="'#307584'" />
                    <t t-set="custom_color_3" t-value="'#4996AA'" />
                    <t t-set="custom_color_4" t-value="'#60B2C4'" />
                    <t t-set="custom_color_5" t-value="'#8ECCD3'" />
                </t>
                <t t-else="">
                    <t t-set="custom_color_1" t-value="'#12575E'" />
                    <t t-set="custom_color_2" t-value="'#076973'" />
                    <t t-set="custom_color_3" t-value="'#057473'" />
                    <t t-set="custom_color_4" t-value="'#008C73'" />
                    <t t-set="custom_color_5" t-value="'#18A379'" />
                </t>
                <div class="page">
                    <div class="row">
                        <div class="col-xs-5"></div>
                        <div class="col-xs-6 col-xs-offset-1" style="padding-right:0px;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_1+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;'">Dirección de entrega</div>                    
                            <div style="margin-left:15px;margin-top: 5px;">
                               <p t-field="o.partner_id.name" style="margin-bottom:0px;" />
                               <p t-field="o.partner_id.street" style="margin-bottom:0px;" />
                               <p style="margin-bottom:0px;"><span t-field="o.partner_id.zip" /> <span t-field="o.partner_id.city" /></p>
                               <p t-field="o.partner_id.country_id" style="margin-bottom:0px;" />
                               <t t-if="o.partner_id.phone">
                                    <p style="margin-bottom:0px;">
                                        <i class="fa fa-phone"></i>
                                        <span t-field="o.partner_id.phone" />
                                    </p>
                               </t>
                               <p t-if="o.partner_id.vat" style="margin-bottom: 0px;">NIF: <span t-field="o.partner_id.vat"/></p>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-xs-5">
                            <h4 style="font-weight:bold;"><span t-field="o.name"/></h4>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-xs-5">
                            <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;margin-bottom: 5px;'">Cliente</div>    
                            <t t-if="o.partner_id.parent_id.id>0">
                                <p t-field="o.partner_id.parent_id.name" style="margin-bottom:0px;margin-left: 15px;" />
                            </t>
                            <t t-if="o.partner_id.parent_id.id==0">
                                <p t-field="o.partner_id.name" style="margin-bottom:0px;margin-left: 15px;" />
                            </t>
                        </div>
                        <div class="col-xs-3">
                            <div class="row">
                                <div class="col-xs-6" style="text-align:center;padding-left:0px;padding-right:0px;">
                                    <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Origen</div>    
                                    <p t-field="o.origin" />
                                </div>
                                <div class="col-xs-6" style="text-align:center;padding-right: 0px;">
                                    <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Fecha</div>    
                                    <t t-if="o.management_date">
                                        <p t-esc="o.management_date[:-9]" t-options="{&quot;widget&quot;: &quot;date&quot;}" />
                                    </t>
                                </div>
                            </div>
                        </div>
                        <div class="col-xs-2" style="text-align:center;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Transporte</div>    
                            <p t-field="o.carrier_id" />
                        </div>
                        <div class="col-xs-1" style="text-align:center;padding-left:0px;padding-right:0px;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Peso</div>    
                            <span t-field="o.weight"/>
                            <span t-field="o.weight_uom_id"/>
                        </div>
                        <div class="col-xs-1" style="text-align:center;padding-right: 0px;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_2+';color: white;font-weight: bold;padding: 5px;width:100%;margin-bottom: 5px;'">Bultos</div>    
                            <p t-field="o.number_of_packages" />
                        </div>
                    </div>
                    <div class="row" id="table_header" style="margin-top:20px;">
                        <div class="col-xs-8" style="padding-right: 0px;">
                            <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;height: 40px;line-height: 40px;padding-left:15px;'">Descripción</div>
                        </div>
                        <div class="col-xs-2">
                            <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;text-align:center;height:40px;'">Cantidad<br/><small>m2/L</small></div>
                        </div>
                        <div class="col-xs-2" style="padding-right: 0px;padding-left: 0px;">
                            <t t-if="o.total_cashondelivery>0">
                                <div class="title_bar" t-att-style="'background:'+custom_color_3+';color: white;font-weight: bold;width:100%;height: 40px;line-height: 40px;text-align:center;'">Importe total</div>
                            </t>
                        </div>
                    </div>
                    <t t-foreach="o.pack_operation_ids" t-as="move">
                       <div class="row" style="padding: 5px 0px;">
                           <div class="col-xs-8" style="margin-left: 15px;margin-right: -15px;">
                              <span t-field="move.name"/>
                           </div>
                           <div class="col-xs-2" style="text-align:center;padding-right: 0px;">
                               <span t-field="move.qty_done"/>
                           </div>
                            <div class="col-xs-2" style="text-align:right;padding-left:0px;">
                                <t t-if="o.total_cashondelivery>0">
                                     <t t-if="o.order_id">
                                         <t t-set="price_unit_line" t-value="0"/>
                                         <t t-foreach="o.order_id.order_line" t-as="line">
                                             <t t-if="line.product_id.id==move.product_id.id">
                                                 <t t-set="price_unit_line" t-value="line.price_subtotal"/>        
                                             </t>
                                         </t>
                                         <t t-if="price_unit_line>0">
                                             <span t-esc="price_unit_line" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                         </t>
                                     </t>
                                </t>
                            </div>
                       </div>
                   </t>
                   <t t-if="o.total_cashondelivery>0">
                       <div class="row">
                           <div class="col-xs-7"></div>
                           <div class="col-xs-5" style="border-top:1px solid black;margin-top: 20px;">
                               <div class="row" style="padding-bottom:5px;">
                                   <div class="col-xs-8">Base imponible</div>
                                   <div class="col-xs-4" style="text-align:right;">
                                       <span t-field="o.order_id.amount_untaxed" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                   </div>
                               </div>
                               <div class="row" style="padding-bottom:5px;">
                                   <!--<div class="col-xs-8">Iva</div>!-->
                                   <div class="col-xs-8">
                                       <t t-set="order_taxes" t-value="[]"/>
                                       <t t-foreach="o.order_id.order_line" t-as="l">
                                           <t t-foreach="l.tax_id" t-as="tax">
                                               <t t-set="order_taxes" t-value="list(set([tax.description]))"/>
                                           </t>
                                       </t>
                                       <t t-foreach="order_taxes" t-as="order_tax">
                                           <span t-esc="order_tax"/>
                                       </t>
                                    </div>
                                   <div class="col-xs-4" style="text-align:right;">
                                       <span t-field="o.order_id.amount_tax" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                   </div>
                               </div>
                               <div name="total" class="row" t-att-style="'border: 1px solid '+custom_color_4+';'">
                                   <div class="col-xs-8" t-att-style="'background:'+custom_color_4+';color:white;font-weight:bold;'">Total</div>
                                   <div class="col-xs-4" style="text-align:right;font-weight:bold;">
                                       <span t-field="o.order_id.amount_total" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                   </div>
                               </div>
                           </div>
                       </div>
                   </t>
                   <div class="row" style="margin-left: 0px;margin-right: 0px;margin-top: 30px;">
                        <p style="font-size: 11px;"><b>IMPORTANTE - Comprobar Estado Mercancía.</b></p>   
                        <p style="font-size: 11px;">Esta mercancía ha salido de nuestro almacén en perfecto estado. Le rogamos compruebe, en el momento de la recepción, si existe algún desperfecto <b>anótelo en el albarán de entrega</b> de la empresa de transporte y <b>efectúe inmediatamente la reclamación</b> oportuna a la agencia de transporte y a Grupo Arelux.</p>
                        <p style="font-size: 11px;"><b>Grupo Arelux no se responsabiliza del estado de la mercancía pasadas 24 horas.</b></p>
                    </div>
                    <div class="row" style="margin-top:30px;">
                        <div class="col-xs-6">
                            <t t-if="o.total_cashondelivery>0">
                                <div class="title_bar" t-att-style="'background:'+custom_color_5+';color: white;font-weight: bold;padding: 5px 5px 5px 15px;width:100%;'">PEDIDO CONTRAREEMBOLSO</div>
                                <div class="row" style="padding:5px 0px;">
                                    <div class="col-xs-6" style="margin-left: 15px;font-weight:bold;">CANTIDAD A ABONAR</div>
                                    <div class="col-xs-4" style="text-align: right;font-weight: bold;font-size: 15px;">
                                        <span t-field="o.total_cashondelivery" t-options="{&quot;widget&quot;: &quot;monetary&quot;, &quot;display_currency&quot;: o.order_id.currency_id}"/>
                                    </div>
                                </div>
                            </t>
                        </div>
                        <div class="col-xs-6" style="padding-left:0px;padding-right:0px;">
                            <div class='title_bar' t-att-style="'background:'+custom_color_5+';color: white;font-weight: bold;padding: 5px;width:100%%;text-align:center;'">Observaciones</div>                                                
                            <div t-att-style="'border-left:1px solid  '+custom_color_5+';border-right:1px solid  '+custom_color_5+';border-bottom:1px solid  '+custom_color_5+';padding: 10px;'">
                                <p style="font-size:11px;" t-field="o.sale_order_note"/>
                            </div>
                        </div>
                    </div>
                </div>
            </t>
         </t>
    </t>
```    