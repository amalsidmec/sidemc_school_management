from email.policy import default

from odoo import models, fields


class SchoolStudent(models.Model):
    _name = "school.student"

    name = fields.Char(string="Student Name", required=True)
    address = fields.Char(string="Address")
    guardian_name = fields.Char(string="Guardian Name")
    guardian_phone = fields.Char(string="Guardian_Phone")
    date_of_birth = fields.Date(string="Date Of Birth")
    joining_date = fields.Date(string="Joining Date")
    class_teacher = fields.Many2one("school.teacher", string="class teacher")
    teacher_ids = fields.Many2many(
        'school.teacher', string="Other Subject Teachers",
        help='Mention the teachers who teach other subjects.')
    select_status = fields.Selection([('not_selected','Not selected'),('selected','Selected')],default='not_selected')
    fee_structure_ids = fields.One2many('fees.structure', 'student_id', string='Fees Structures',
                                        help="Related Fees Structure")


    def action_select(self):
        print("loopp", self.name)
        self.select_status = 'selected'


class SchoolTeacher(models.Model):
    _name = "school.teacher"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address")
    phone_number = fields.Char(string="Phone Number")
    date_of_birth = fields.Date(string="Date Of Birth")
    is_a_teacher = fields.Boolean()
    add_student = fields.One2many("school.student","class_teacher",string="Add Student")



