from odoo import models, fields, api


class inherit_invoice(models.Model):
    _name = 'inherit_invoice.inherit_invoice'
    _description = 'inherit_invoice.inherit_invoice'


class InheritProduct(models.Model):
    _inherit = 'product.template'

    total_sale_price = fields.Float(
        string='Total Sale Price',
        related='list_price',
        required=False)

    total_cost_price = fields.Float(
        string='Total Cost Price',
        related='standard_price',
        required=False)

    profit = fields.Float(
        string='Profit',
        required=False)



