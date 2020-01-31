# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class Document(models.Model):
    
    _name = 'users_management.document'

    name = fields.Char(string="Name")
    totalDownloads = fields.Integer(string="Total downloads")
    ratingDoc = fields.Integer(string="Total rating")
    totalRating = fields.Integer(string="Ratings count")
    
    user_id = fields.Many2one('res.partner', ondelete='set null', string="Author")
    
    @api.constrains('document','name')
    def _verify_name_too_short(self):
        for record in self:
            if len(record.name) < 4:
                raise ValidationError("Document name must have at least 4 characters")
            if len(record.name) > 10:
                raise ValidationError("Document's name max lenght is 10")
               
    def _verify_name_valid_onchange(self):
        if self.totalRating and self.totalRating > self.totalDownloads : 
            return {
                'warning': {
                    'title': "Error",
                    'message': "To set a Rating must be downloaded first",
                },
        }