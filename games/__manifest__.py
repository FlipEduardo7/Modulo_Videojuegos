{
    'name':'games',
    'description':'games',
    'author':'Equipo 2',
    'website':'www.juegos.com',
    'depends':['base'],
    'data':[
        'security/groups.xml',
        'security/ir.model.access.csv',
        'reportes/report_renta.xml',
        'reportes/report_ticket.xml',
        'views/rentas_view.xml',
        'views/productos_view.xml',
        'views/ventas_view.xml',
        'views/menu_view.xml',
        ],
    'application':True,
}