# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class vit_has_group(models.Model):
#     _name = 'vit_has_group.vit_has_group'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100