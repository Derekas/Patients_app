 #-*- coding: utf-8 -*-

from odoo import models, fields, api
import random


class visitsModel(models.Model):
    _name = 'patients_app.visits_model'
    _description = 'Visits Model'

    
    date=fields.Date("Date",required=True,help="Date",default=fields.Datetime.today())
    detail = fields.Html("Detail",required=True,help="Detail of the visit")
    

    patient=fields.Many2one("patients_app.patient_model","Patient")