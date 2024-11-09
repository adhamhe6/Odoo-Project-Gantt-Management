// project_gantt/static/src/js/gantt_custom.js
odoo.define('project_gantt.gantt_custom', function (require) {
    "use strict";

    var GanttRenderer = require('web_gantt.GanttRenderer');

    GanttRenderer.include({
        // Custom code can be added here, like modifying colors or adding tooltips
        _renderBars: function () {
            this._super.apply(this, arguments);
            // Example: Add a class to customize the color based on task stage
            this.$('.o_gantt_bar').each(function () {
                var stage = $(this).data('record').stage;
                if (stage === 'done') {
                    $(this).addClass('gantt-task-done');
                } else if (stage === 'in_progress') {
                    $(this).addClass('gantt-task-in-progress');
                }
            });
        },
    });
});
