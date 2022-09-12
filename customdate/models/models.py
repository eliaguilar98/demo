# -*- coding: utf-8 -*-

from odoo import models, fields, api


class customdate(models.Model):
    _inherit = 'project.task.recurrence'
    
    next_recurrence_date = fields.Datetime()


