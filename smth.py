# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:36:02 2020

@author: Tristan
"""
"""
input looks like [[subject_name, index1, index2], [teacher_name, index1, index2]]
"""
"""
Apply GAUSSIAN BLUR??????
"""
from classes import *
def evaluate(time_table):
    for i in range(0, len(time_table)):
        for j in range(0, len(i)):
            time_table[i][j].Room.values = time_table[i][j].subject.prefTime[i][j] \
                                         + time_table[i][j].teacher.prefTime[i][j] \
                                         + time_table[i][j].room.prefTime[i][j]
        
    #return a

def neighborOfSubject(sub, param):
#    for k in range(0, len(subject_list)):
#        i1, i2, i3, i4 = map(int, indices[k].split("-"))
#        #For subject
#        if inclusive[k][0]:
#            counter_subject = i1 + 1
#            
#            for i in range(0,i1):
#                subject_list[k].prefTime[i] = [round(1/counter_subject, 2)]*4
#                counter_subject -= 1
#            
#            for i in range(i1, len(subject_list[k].prefTime)):
#                subject_list[k].prefTime[i] = [round(1/(1+(i-i1)), 2)]*4
#                
#        else:
#            for i in range(0, len(subject_list[k].prefTime)):
#                for j in range(0, len(subject_list[k].prefTime[i])):
#                    subject_list[k].prefTime[i][j] = round(1/( 1 + (abs(i1-i) + abs(i2 - j))), 2)
#        #For Teacher    
#        if inclusive[k][1]:
#            counter_teacher = i3 + 1
#            
#            for i in range(0,i3):
#                teacher_list[k].prefTime[i] = [round(1/counter_subject, 2)]*4
#                counter_teacher -= 1
#                
#            for i in range(i3, len(teacher_list[k].prefTime)):
#                teacher_list[k].prefTime[i] = [round(1/(1+(i-i3)), 2)]*4
#                
#        else:
#             for i in range(0, len(teacher_list[k].prefTime)):
#                for j in range(0, len(teacher_list[k].prefTime[i])):
#                    teacher_list[k].prefTime[i][j] = round(1/( 1 + (abs(i3-i) + abs(i4 - j))), 2)
    
    sub.neighbors(param)
        

def firstTimeTable(neighbor_of_subjects):
    first_time_table = []
    value_of_table = evaluate(first_time_table)
    
    """Process"""
    
    return first_time_table, value_of_table

def neighborOfTimeTable(current_solution, dict_of_neighbor):
    neighbor_of_time_table = {}
    
    """Some process"""
    
    return neighbor_of_time_table
    

t1 = Subject("Math", 3, "2-3-False")
t2 = Subject("Fil", 3, "1-3-True")
t3 = Subject("Eng", 3, "4-1-False")
t4 = Subject("CS", 3, "5-2-True")
arr = [t1,t2,t3,t4]

s1 = Teacher("I", "4-3-True")
s2 = Teacher("He", "6-2-True")
s3 = Teacher("They", "2-1-True")
s4 = Teacher("She", "5-2-False")
arr2 = [s1,s2,s3,s4]
table = [[0]*4 for i in range(8)]

print("probability of the SUBJECT landing on a given sched using its prefTime")
for k in arr:
    for i in k.prefTime:
        print(i)
    print("")
    
print("probability of the TEACHER landing on a given sched using its prefTime")
for k in arr2:
    for i in k.prefTime:
        print(i)
    print("")
    
def r(i):
    return round(i,2)
print("COMBINED PROBABILITY gives where the teacher and subject should be placed")
print("Assuming a one-to-one relationship, that is, no subject shall be taught by two different teachers")
for k in range(0, len(arr)):
    for i in range(0, len(arr[k].prefTime)):
        for j in range(0, len(arr[k].prefTime[i])):
            table[i][j] = arr[k].prefTime[i][j] + arr2[k].prefTime[i][j]
    """For printing purposes"""
    print("Printing CP")
    for i in table:
        print(list(map(r,i)))
               




#evaluate(time_table)
    