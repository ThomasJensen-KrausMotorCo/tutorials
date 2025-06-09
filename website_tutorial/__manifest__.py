{
    'name': 'Tutorial Theme',
    'description': 'Tutorial Theme - Drones, modelling, camera',
    'category': 'Website/Theme',
    'version': '17.0.1.0',
    'author': 'Tom Jensen',
    'license': 'LGPL-3',
    'depends': ['website_sale', 'website_sale_wishlist', 'website_blog', 'website_mass_mailing'],
    'data': [
        # Options
        'data/presets.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_tutorial/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'website_tutorial/static/src/scss/bootstrap_overridden.scss'),
        ],
    },
}