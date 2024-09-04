from odoo import models,fields

class StudentSuggestion(models.TransientModel):
    _name = "suggestion"
    _description = "student suggestion"

    name = fields.Many2one("school.student", string="Name")
    suggestion = fields.Char(string="Suggestion")
    std_class = fields.Char(string="Class")



    def suggestion_creation(self):
        student = self.env['student.suggestion'].create({
            'name': self.name.name,
            'standard': self.std_class,
            'suggestion': self.suggestion
        })