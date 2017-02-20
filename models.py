# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Hospital(models.Model):
    _name = 'rubricaFinal.hospital'
    name = fields.Char(string="Nombre hospital", required=True)
    medicos_id = fields.One2many('rubricaFinal.medicos', 'hospital_id', string='Medicos')
    ambulancias_id = fields.One2many('rubricaFinal.ambulancias', 'hospital_id', string='Ambulancias')
    consultas_id = fields.One2many('rubricaFinal.consultas', 'hospital_id', string='Consultas')
    pacientes_id = fields.One2many('rubricaFinal.pacientes', 'hospital_id', string='Pacientes')

    consultas = fields.Selection([
    	('privado', "Privado"),
    	('publico', "Publico"),
    	])

    @api.one
    def action_privado(self):
    	self.cargo = 'privado'

    @api.one
    def action_publico(self):
    	self.cargo = 'publico'

class Ambulancias(models.Model):
    _name = 'rubricaFinal.ambulancias'
    name = fields.Char(string="Nombre ambulancia", required=True)
    hospital_id = fields.Many2one('rubricaFinal.hospital', string='Hospital')

class Medicos(models.Model):
    _name = 'rubricaFinal.medicos'
    name = fields.Char(string="Nombre medicos", required=True)
    hospital_id = fields.Many2one('rubricaFinal.hospital', string='Hospital')
    consultas_id = fields.Many2many('rubricaFinal.consultas', 'consultasMedicas', 'medicos_id', 'consultas_id', 'Consultas')
    pacientes_id = fields.Many2many('rubricaFinal.pacientes', 'pacientes_medicos', 'medicos_id', 'pacientes_id', 'Pacientes')

    cargo = fields.Selection([
    	('dermatologo', "Dermatologo"),
    	('neurologo', "Neurologo"),
    	('cardiologo', "Cardiologo"),
    	('nefrologo', "Nefrologo"),
    	('reumatologo', "Reumatologo"),
    	('gastroenterologo', "Gastroenterologo"),
    	('otorrinolaringologo', "Otorrinolaringologo"),
    	])

    @api.one
    def action_dermatologo(self):
    	self.cargo = 'dermatologo'

    @api.one
    def action_neurologo(self):
    	self.cargo = 'neurologo'

    @api.one
    def action_cardiologo(self):
    	self.cargo = 'cardiologo'

    @api.one
    def action_nefrologo(self):
    	self.cargo = 'nefrologo'

    @api.one
    def action_reumatologo(self):
    	self.cargo = 'reumatologo'

    @api.one
    def action_gastroenterologo(self):
    	self.cargo = 'gastroenterologo'

    @api.one
    def action_otorrinolaringologo(self):
    	self.cargo = 'otorrinolaringologo'

class Consultas(models.Model):
    _name = 'rubricaFinal.consultas'
    name = fields.Char(string="Nombre consultas", required=True)
    hospital_id = fields.Many2one('rubricaFinal.hospital', string='Hospital')
    medicos_id = fields.Many2many('rubricaFinal.medicos', 'consultasMedicas', 'consultas_id', 'medicos_id', 'Medicos')
    pacientes_id = fields.Many2many('rubricaFinal.pacientes', 'pacientes_medicos', 'consultas_id', 'pacientes_id', 'Pacientes')

    consultas = fields.Selection([
    	('externas', "Externas"),
    	('urgencias', "Urgencias"),
    	])

    @api.one
    def action_externas(self):
    	self.cargo = 'externas'

    @api.one
    def action_urgencias(self):
    	self.cargo = 'urgencias'

class Pacientes(models.Model):
    _name = 'rubricaFinal.pacientes'
    name = fields.Char(string="Nombre pacientes ", required=True)
    hospital_id = fields.Many2one('rubricaFinal.hospital', string='Hospital')
    medicos_id = fields.Many2many('rubricaFinal.medicos', 'pacientes_medicos', 'pacientes_id', 'medicos_id', 'Medicos')
    consultas_id = fields.Many2many('rubricaFinal.consultas', 'pacientes_medicos', 'pacientes_id', 'consultas_id', 'Consultas')

    pacientes = fields.Selection([
    	('ninos', "Niños"),
    	('adultos', "Adultos"),
    	('ancianos', "Ancianos"),
    	])

    @api.one
    def action_ninos(self):
    	self.cargo = 'ninos'

    @api.one
    def action_adultos(self):
    	self.cargo = 'adultos'

    @api.one
    def action_ancianos(self):
    	self.cargo = 'ancianos'
 

   

