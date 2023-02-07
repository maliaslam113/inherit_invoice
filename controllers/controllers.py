# -*- coding: utf-8 -*-
# from odoo import http


# class InheritInvoice(http.Controller):
#     @http.route('/inherit_invoice/inherit_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_invoice/inherit_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_invoice.listing', {
#             'root': '/inherit_invoice/inherit_invoice',
#             'objects': http.request.env['inherit_invoice.inherit_invoice'].search([]),
#         })

#     @http.route('/inherit_invoice/inherit_invoice/objects/<model("inherit_invoice.inherit_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_invoice.object', {
#             'object': obj
#         })
