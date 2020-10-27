# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:45:18 2020
smth smth
@author: Tristan
"""
#import smth
class SubjectPeriod:    #the whole class schedule in general, what our class schedule looks like
    def __init__(self, _subject_name = "", _teacher_name = "", _room_name = ""):
        self.subject = Subject(_subject_name)
        self.teacher = Teacher(_teacher_name)
        self.room = Room(_room_name)
        self.block = []
        
class Subject:
    def __init__(self, _name = "", _unit = "", parameters = ""):
        self.id = ""
        self.name = _name
        self.prefTime = [[0]*4 for i in range(8)]
        self.unit = _unit
        self.unitCounter = 0
        prefTime = Subject.neighbors(self, parameters)
        
    def neighbors(self, parameters):
        param = parameters.split("-")
        if param[0] == "" or param[1] == "" or param[2] == "":
            return [[0]*4 for i in range(8)]
        
        i1, i2 = map(int, param[0:2])
        
        if param[2] == "True":
            counter_subject = i1 + 1
            
            for i in range(0,i1):
                self.prefTime[i] = [round(1/counter_subject, 2)]*4
                counter_subject -= 1
            
            for i in range(i1, len(self.prefTime)):
                self.prefTime[i] = [round(1/(1+(i-i1)), 2)]*4
                
        if param[2] == "False":
            for i in range(0, len(self.prefTime)):
                for j in range(0, len(self.prefTime[i])):
                    self.prefTime[i][j] = round(1/( 1 + (abs(i1-i) + abs(i2 - j))), 2)
        
class Teacher:
    def __init__(self, _name = "", _parameters = ""):
        self.id = ""
        self.name = _name
        self.prefTime = [[0]*4 for i in range(8)]
        prefTime = Teacher.neighbors(self, _parameters)
        
    def neighbors(self, parameters):
        param = parameters.split("-")
        if param[0] == "" or param[1] == "" or param[2] == "":
            return [[0]*4 for i in range(8)]
        
        i1, i2 = map(int, param[0:2])
        
        if param[2] == "True":
            counter_subject = i1 + 1
            
            for i in range(0,i1):
                self.prefTime[i] = [round(1/counter_subject, 2)]*4
                counter_subject -= 1
            
            for i in range(i1, len(self.prefTime)):
                self.prefTime[i] = [round(1/(1+(i-i1)), 2)]*4
                
        if param[2] == "False":
            for i in range(0, len(self.prefTime)):
                for j in range(0, len(self.prefTime[i])):
                    self.prefTime[i][j] = round(1/( 1 + (abs(i1-i) + abs(i2 - j))), 2)
        

class Block:
    def __init__(self, _name, _size):
        self.id = ""
        self.name = ""
        self.size = 0

class Room:    #classroom, not the whole class schedule in general
    def __init__(self, _name, _size = 31):
        self.id = ""
        self.name = _name
        self.size = _size
        self.occupied = [[0]*4 for i in range(8)]
        
    values = [[0]*4 for i in range(8)]



