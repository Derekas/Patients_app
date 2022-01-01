# -*- coding: utf-8 -*-
# from odoo import http


# class PatientsApp(http.Controller):
#     @http.route('/patients_app/patients_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/patients_app/patients_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('patients_app.listing', {
#             'root': '/patients_app/patients_app',
#             'objects': http.request.env['patients_app.patients_app'].search([]),
#         })

#     @http.route('/patients_app/patients_app/objects/<model("patients_app.patients_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('patients_app.object', {
#             'object': obj
#         })
