# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Document(models.Module):
    
    _name = 'usersmanagement.document'

    name = fields.Char(string="Name")
    totalDownloads = fields.Integer(string="Total downloads")
    ratingDoc = fields.Integer(string="Total rating")
    totalRating = fields.Integer(string="Ratings count")
    
    user_id = fields.Many2one('res.users', ondelete='set null', string="Author")
    
 