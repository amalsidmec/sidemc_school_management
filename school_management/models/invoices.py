from odoo import models, fields


class InvoiceOrder(models.Model):
    _inherit = "account.move"

    parent_name = fields.Char(string="Parent Name")
    parent_phone = fields.Char(string="Parent Phone")


class Fees(models.Model):
    _inherit = "account.move.line"

    fees_amt = fields.Many2one("fees.structure", string="Fees")
    gst_amt = fields.Many2one("fees.structure", string="GST")