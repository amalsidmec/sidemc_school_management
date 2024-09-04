from odoo import models,fields


class StudentSuggestion(models.Model):
    _name = "student.suggestion"
    _rec_name ="name"

    name = fields.Char(string="Student")
    standard = fields.Char(string="Class")
    suggestion = fields.Char(string="Suggestion")
