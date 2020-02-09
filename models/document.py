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
    ratingByDownload = fields.Float(string="Rating by Download", compute="_ratings_download")
    
    user_id = fields.Many2one('res.partner', ondelete='set null', string="Author")
    
    @api.constrains('document','name')
    def _verify_name_too_short(self):
        for record in self:
            if len(record.name) < 4:
                raise ValidationError("Document name must have at least 4 characters")
            if len(record.name) > 10:
                raise ValidationError("Document's name max lenght is 10")
    
    @api.constrains('document','totalRating')
    def _verify_name_valid_onchange(self):
        for record in self:
            if record.totalRating > record.totalDownloads:
                raise ValidationError("The document can't have more ratings than downloads")
        
        
    @api.constrains('document', 'totalDownloads')
    def _verify_downloads_positive_constraint(self):
        for record in self:
            if record.totalDownloads < 0:
                raise ValidationError("The downloads can't be negative")
            
    @api.onchange('totalDownloads')
    def _verify_downloads_positive_onchange(self):
        if self.totalDownloads < 0: 
            return {
                'warning': {
                    'title': "Downloads warning",
                    'message': "Downloads must be positive",
                },
        }
    
    @api.depends('totalDownloads','ratingDoc')
    def _ratings_download(self):
        for record in self:
            if record.totalDownloads > 0:
                record.ratingByDownload= record.ratingDoc / record.totalDownloads
            else:
                record.ratingByDownload = 0.0
            