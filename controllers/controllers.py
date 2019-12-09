# -*- coding: utf-8 -*-
from odoo import http

# class UsersManagement(http.Controller):
#     @http.route('/users_management/users_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/users_management/users_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('users_management.listing', {
#             'root': '/users_management/users_management',
#             'objects': http.request.env['users_management.users_management'].search([]),
#         })

#     @http.route('/users_management/users_management/objects/<model("users_management.users_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('users_management.object', {
#             'object': obj
#         })