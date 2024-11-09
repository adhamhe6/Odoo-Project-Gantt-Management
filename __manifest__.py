# project_gantt/__manifest__.py
{
    'name': 'Project Gantt Management',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Project Management Tool with Gantt Chart',
    'description': 'Manage projects with task assignment, deadlines, and Gantt chart view.',
    'depends': ['project', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'data/project_gantt_data.xml',
        'data/task_gantt_data.xml', 
        'data/task_notification_cron.xml',
        'templates/email_templates.xml',
        'views/project_gantt_views.xml',
        'views/project_task_views.xml',
        'views/action_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project_gantt/static/src/js/gantt_custom.js',
            'project_gantt/static/src/css/gantt_styles.css',
        ],
    },
    'installable': True,
    'application': True,
}
