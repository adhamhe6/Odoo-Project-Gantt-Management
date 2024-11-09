# project_gantt/models/task.py
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class ProjectGanttTask(models.Model):
    _name = 'project.gantt.task'
    _description = 'Project Task Management'

    name = fields.Char(string='Task Name', required=True)
    assigned_to = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user.id)
    start_date = fields.Date(string='Start Date', default=fields.Date.context_today)
    end_date = fields.Date(string='End Date')
    project_id = fields.Many2one('project.gantt', string='Project')
    stage = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='Stage', default='draft')

    @api.model
    def notify_upcoming_tasks(self):
        """ Notify assigned users about tasks that are nearing their deadline. """
        today = fields.Date.context_today(self)
        upcoming_tasks = self.search([
            ('end_date', '>=', today),
            ('end_date', '<=', today + timedelta(days=2)),
            ('stage', '!=', 'done')
        ])

        for task in upcoming_tasks:
            if task.assigned_to:
                self._send_task_notification(task)

    def _send_task_notification(self, task):
        """ Send email notification to the user assigned to the task. """
        template = self.env.ref('project_gantt.email_template_task_deadline')
        if template:
            template.send_mail(task.id, force_send=True)
            
    def _send_inapp_notification(self, task):
        """ Send in-app notification to the user assigned to the task. """
        self.env['mail.notification'].create({
            'res_partner_id': task.assigned_to.partner_id.id,
            'message_type': 'notification',
            'body': f"Task '{task.name}' is due on {task.end_date}.",
            'res_model': 'project.gantt.task',
            'res_id': task.id,
        })