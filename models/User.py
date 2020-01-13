# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class User(models.Module):
    
    _inherit = 'res.partner'
    
    login = fields.Char(string = "Login")
    userType = fields.Char(string = "Type")
    premiumCount = fields.Integer(string = "Months premium")
    documents = fields.one2Many('usersmanagement.document', 'user_id', ondelete = "cascade", string = "Documents")
    
class Premium(models.Module):
    
    _inherit = 'usersmanagement.user'
    
    autorenovation = fields.Boolean(string = "Autorenovation")
    
    
    
