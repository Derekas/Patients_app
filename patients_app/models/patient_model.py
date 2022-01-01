 #-*- coding: utf-8 -*-

import re
from odoo import models, fields, api
import random

from odoo.exceptions import ValidationError


class patientModel(models.Model):
    _name = 'patients_app.patient_model'
    _description = 'Patients Model'

    dni = fields.Char(string='DNI', required=True,size=9,help="DNI")
    name = fields.Char(string="Patient Name",required=True,index=True,help="Name")
    surname = fields.Char(string='Patient Surname', required=True,index=True,help="Surname")
    phone= fields.Char(string='Phone', required=True,size=9,index=True,help="Phone")
    date=fields.Date("Date",required=True,help="Date")
    email = fields.Char(string='Email', required=True,size=100,help="Input Gmail")
    photo = fields.Binary(string='Photo', required=True)

    visit=fields.One2many("patients_app.visits_model","patient",string="Visits")


    @api.constrains("dni")
    def _check_DNI(self):
        letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        
            
        dni = self.dni
        letter = dni[-1].upper()
        number = dni[:-1]
        if (len(dni) == 9 and number.isdigit()):
            number = int(dni[:-1])
        else:
            raise ValidationError("Incorrect Format DNI")

        mod = number%23
        if letters[mod] == letter:
            pass
        else:
            raise ValidationError("Incorrect Letter")

    @api.constrains("email")
    def _check_Email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, self.email)):
                pass
        else:
            raise ValidationError("Gmail incorrecto")
    