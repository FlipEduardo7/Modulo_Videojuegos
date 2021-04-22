#from productos import productos
from odoo import models, fields, api

class clientes(models.Model):
    _name = 'games.clientes'
    name = fields.Char('Cliente', required=True)
    _sql_constraints = [('cliente_name_unique', 'unique(name)', 'el cliente esta duplicado')]

class ventas(models.Model):
    _name = 'games.ventas'
    name = fields.Char('Folio', required=True)
    fecha = fields.Datetime('Fecha', required=True)
    cliente = fields.Many2one('games.clientes', string='Cliente', required=True)
    total = fields.Float('Total', readonly=True)
    productos = fields.One2many('games.ventas_det', 'venta', string='Productos')
    tipos = fields.Selection([('cre', 'Creada'), ('gen', 'Generada'), ('can', 'Cancelada')],'Estado', default='gen', readonly=True)
    _sql_constraints = [('venta_name_unique', 'unique(name)', 'La venta esta duplicada')]

class ventas_det(models.Model):
    _name = 'games.ventas_det'
    venta = fields.Many2one('games.ventas', string='venta', required=True)
    producto = fields.Many2one('games.productos', string='producto', required=True)
    cantidad = fields.Integer('Cantidad', default=1)
    precio = fields.Float('Precio')
    importe = fields.Float(compute='cal_importe', string='importe', readonly=True)
    _sql_constraints = [('ventadet_name_unique', 'unique(venta.producto', 'el producto esta duplicado')]

    @api.depends('cantidad', 'precio')
    def cal_importe(self):
        for rec in self:
            rec.importe = rec.cantidad * rec.precio