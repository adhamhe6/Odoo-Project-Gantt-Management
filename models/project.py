# project_gantt/models/project.py
from odoo import models, fields

class ProjectGantt(models.Model):
    _name = 'project.gantt'
    _description = 'Project Gantt Management'

    name = fields.Char(string='Project Name', required=True)
    deadline = fields.Date(string='Deadline')
    task_ids = fields.One2many('project.gantt.task', 'project_id', string='Tasks')
