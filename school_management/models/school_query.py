from odoo import models, fields
from odoo.exceptions import ValidationError


class SchoolQuery(models.Model):
    _name = "school.query"
    _description = "structure"

    child_name = fields.Char(string="Child Name", required=True)
    child_age = fields.Char(string="Age")
    class_to = fields.Char(string="Class To")
    guardian_name = fields.Char(string="Guardian Name")
    guardian_phon_no = fields.Char(string="Guardian Ph No")
    select_status = fields.Selection([('not_admit','Not Admit'),('admit','Admit')],default='not_admit')




    # def action_admit(self):
    #     self.select_status = 'admit'

    def student_creation(self):
        student_id = self.env["school.student"].search([("guardian_phone",'=',self.guardian_phon_no)] and [("name",'=',self.child_name)])

        if student_id:
            raise ValidationError("The Student with same Data already exists")

        student = self.env['school.student'].create({
            'name' : self.child_name,
            'age' : self.child_age,
            'guardian_phone':self.guardian_phon_no

        })
        self.select_status = 'admit'







