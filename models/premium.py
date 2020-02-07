# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class Premium(models.Model):
    
    _inherit = 'res.partner'
    
    login = fields.Char(string="Login")
    userType = fields.Selection([('free', 'FREE'), ('premium', 'PREMIUM'), ('admin', 'ADMIN')])
    premiumCount = fields.Integer(string="Months premium", default=0)
    documents = fields.One2many('users_management.document', 'user_id', ondelete="cascade", string="Documents")
    groups = fields.Many2many('users_management.group', string='groups')
    
    autorenovation = fields.Boolean(string="Autorenovation")
    
    @api.constrains('premium', 'login')
    def _verify_login_too_short(self):
        for record in self:
            if len(record.login) < 4:
                raise ValidationError("Login must have at least 4 characters")
            if len(record.login) > 10:
                raise ValidationError("Login's max lenght is 10")
        
    @api.onchange('userType')
    def _verify_user_type_valid_onchange(self):
        for rec in self:
            if rec.userType != 'premium':
                rec.premiumCount = 0
        
    @api.constrains('premium', 'userType')
    def _verify_user_type_valid_constrain(self):
        for rec in self:
            if rec.userType != 'premium' and rec.premiumCount != 0:
                raise ValidationError("Months count must be 0")
        
    @api.onchange('autorenovation')
    def _premium_has_autorenovation(self):
        if self.autorenovation and self.autorenovation == 1: 
            return {
                'warning': {
                    'title': "Autorenovation warning",
                    'message': "User has autorenovation enabled",
                },
        }
    
    
