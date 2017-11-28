# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import api, fields, models, exceptions


class x_task_proyects_inherit(models.Model):
    _inherit = 'project.task'

    x_fechaInicio = fields.Date(
        string='Fecha Inicio',

    )
    x_duracion = fields.Float(
        digits=(6, 2), help="Duration in days", compute="_set_duration")
    #x_fechaFin = fields.Date(string="Fecha Límite")

    @api.depends('date_deadline', 'x_fechaInicio')
    def _set_duration(self):
        for r in self:
            if not (r.x_fechaInicio and r.date_deadline):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            start_date = fields.Datetime.from_string(r.x_fechaInicio)
            end_date = fields.Datetime.from_string(r.date_deadline)
            r.x_duracion = ((end_date - start_date).days + 1) * 24

    @api.constrains('date_deadline', 'x_fechaInicio')
    def _check_date_not_error(self):
        for r in self:
            if r.date_deadline and r.date_deadline < r.x_fechaInicio:
                raise exceptions.ValidationError(
                    "-Fecha límite- no puede ser menor que -Fecha inicio-")
