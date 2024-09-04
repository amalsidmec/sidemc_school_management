from email.policy import default

from odoo import models, fields, api,_
from datetime import datetime

from odoo.exceptions import ValidationError
from odoo.tools.populate import compute


class SchoolStudent(models.Model):
    _name = "school.student"

    name = fields.Char(string="Student Name", required=True)
    address = fields.Char(string="Address")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    standard = fields.Char(string="Class")
    guardian_name = fields.Char(string="Guardian Name")
    guardian_phone = fields.Char(string="Guardian_Phone")
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age",compute="_compute_age",store=True)
    joining_date = fields.Date(string="Joining Date")
    class_teacher = fields.Many2one("school.teacher", string="class teacher")
    teacher_mob_no = fields.Char(string="Teacher No")
    teacher_ids = fields.Many2many(
        'school.teacher', string="Other Subject Teachers",
        help='Mention the teachers who teach other subjects.')
    select_status = fields.Selection([('not_selected','Not selected'),('selected','Selected')],default='not_selected')
    fee_structure_ids = fields.One2many('fees.structure', 'student_id', string='Fees Structures',
                                        help="Related Fees Structure")



    def create(self, vals):
        if vals["guardian_phone"]:
            student = self.env["school.student"].search([("guardian_phone",'=',vals['guardian_phone'])])
            if student:
              raise ValidationError("its exists")
        return super(SchoolStudent, self).create(vals)



    def action_suggestion(self):
        return {
            'name': _('complaint'),
            'view_mode': 'form',
            'res_model': 'suggestion',
            'type': 'ir.actions.act_window',
            'target': 'new',

        }


    def action_select(self):
        self.select_status = 'selected'

    @api.onchange("class_teacher")
    def _onchange_teacher(self):
       if self.class_teacher:
         self.teacher_mob_no = self.class_teacher.phone_number

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = datetime.today()
                dob = fields.Date.from_string(record.date_of_birth)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                record.age = age


class SchoolTeacher(models.Model):
    _name = "school.teacher"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address")
    phone_number = fields.Char(string="Phone Number")
    date_of_birth = fields.Date(string="Date Of Birth")
    is_a_teacher = fields.Boolean()
    add_student = fields.One2many("school.student","class_teacher",string="Add Student")



