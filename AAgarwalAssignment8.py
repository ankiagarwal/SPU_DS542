# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:02:28 2022

@author: ankia
"""

class University:
    
    def __init__(self, university_name, location, undergraduate_students, graduate_students):
        self.university_name = university_name
        self.location = location
        self.undergraduate_students = undergraduate_students
        self.graduate_students = graduate_students
        
    def print_university_size(self):
        return self.undergraduate_students + self.graduate_students
    
    def is_undergraduate_greater(self):
        if self.undergraduate_students > self.graduate_students:
            print("There are more undergraduate students than graduate students")
        else:
            print("There are more graduate students than undergraduate student")
            
            
SPU = University(university_name = "Saint Peter's University", 
                 location = "Jersey City, NJ",
                 undergraduate_students = 2134, 
                 graduate_students=875)

SPU.print_university_size()
SPU.is_undergraduate_greater()

############ bonus question 

class College(University):
    def print_name_location(self):
        print(f"{self.university_name} is located in {self.location}")
        
College.print_name_location(SPU)
    
    