from odoo import models, fields

class clasificaciones(models.Model):
    _name = 'games.clasificaciones'
    _description = 'clasificaciones de productos'
    name = fields.Char('Nombre', required=True)
    producto_ids = fields.One2many('games.productos', 'clasif', string='Productos')
    productos = fields.Many2many('games.productos', string='Productos')
    _sql_constraints = [('class_name_unique','unique(name)','la clasificacion esta duplicada')]

class productos(models.Model):
    _name = 'games.productos'
    _description = 'Videojuegos LTC'
    name = fields.Char('Nombre', required=True)
    foto = fields.Binary('Foto')
    precio = fields.Float('Precio')
    costo = fields.Float('Costo')
    stock = fields.Integer('Existencia')
    tipo = fields.Selection([('fis','Fisico'),('dig','Digital')],'Tipo',default='fis',required=True)
    clasif = fields.Many2one('games.clasificaciones',string='clasificacion', required=True)
    _sql_constraints = [('name_unique', 'unique(name)', 'el cliente esta duplicado')]