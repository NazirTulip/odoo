from datetime import timedelta
from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")

    date_availability = fields.Date(
        string="Available From",
        copy=False,
        default=lambda self: fields.Date.today() + timedelta(days=90)
    )

    expected_price = fields.Float(string="Expected Price", required=True)

    selling_price = fields.Float(
        string="Selling Price",
        #readonly=True,
        copy=False
    )

    bedrooms = fields.Integer(
        string="Bedrooms",
        default=2
    )

    living_area = fields.Integer(string="Living Area (sqm)")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden = fields.Boolean(string="Garden")

    active = fields.Boolean(
        string="Active",
        default=True
    )

    state = fields.Selection(
        [
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled'),
        ],
        string="Status",
        required=True,
        copy=False,
        default='new'
    )