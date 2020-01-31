# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Group(models.Model):
    
    _name = 'users_management.group'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    premiums = fields.Many2many('res.partner', string="Premiums")
    
    @api.constrains('group', 'name')
    def _verify_group_too_short_or_long(self):
        for record in self:
            if len(record.name) < 4:
                raise ValidationError("Group name must have at least 4 characters")
            if len(record.name) > 10:
                raise ValidationError("Group's name max lenght is 10")
            
    @api.onchange('userType')
    def _verify_description_valid_onchange(self):
        if self.description and self.description == self.name: 
            return {
                'warning': {
                    'title': "Invalid Description",
                    'message': "Description is not valid.",
                },
        }
        