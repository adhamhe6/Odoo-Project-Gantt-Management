# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectGantt(http.Controller):
#     @http.route('/project_gantt/project_gantt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_gantt/project_gantt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_gantt.listing', {
#             'root': '/project_gantt/project_gantt',
#             'objects': http.request.env['project_gantt.project_gantt'].search([]),
#         })

#     @http.route('/project_gantt/project_gantt/objects/<model("project_gantt.project_gantt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_gantt.object', {
#             'object': obj
#         })
