# -*- coding: utf-8 -*-
# from odoo import http


# class Customdate(http.Controller):
#     @http.route('/customdate/customdate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customdate/customdate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customdate.listing', {
#             'root': '/customdate/customdate',
#             'objects': http.request.env['customdate.customdate'].search([]),
#         })

#     @http.route('/customdate/customdate/objects/<model("customdate.customdate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customdate.object', {
#             'object': obj
#         })
