{
    'name': 'Real estate',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage properties',
    'author': 'Nazir',
    'description': 'This module manages properties and their information.',
    'depends': ['base'],   # ✅ REQUIRED
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
}
