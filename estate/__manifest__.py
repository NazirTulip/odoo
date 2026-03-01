{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real Estate Management',
    'description': 'Module to manage real estate properties',
    'author': 'Your Name',
    'category': 'Training',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
}