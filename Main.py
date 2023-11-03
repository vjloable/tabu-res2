import random
from classes import Subject
from classes import Teacher
import time
import itertools
import xl

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def overall_fitness(mat):
    temp = 0
    for x in mat:
        for y in x:
            temp += float(y)
    return temp/32

#swapping axes in matrices
def swapaxes(mat, r, c):
    new_mat = [['0']*r for _ in range(c)]
    for x in range(r):
        for y in range(c):
            new_mat[y][x] = mat[x][y]
    return new_mat

#random desirability generator
def rand_desirability(r, c):
    return [[round(random.random(), 2) for _ in range(columns)] for _ in range(rows)]

#getting the fitness value of the sched matrix 
def get_fitness(choice, sched, subj_pref, r, c):
    if choice == "matrix":
        new_mat = [[0.0 for _ in range(c)] for _ in range(r)]
        for x in range(r):
            for y in range(c):
                if(sched[x][y]!='-'):
                    new_mat[x][y] = subj_pref[sched[x][y] if "CE" in sched[x][y] else sched[x][y][:-1]][x][y]
                else:
                    new_mat[x][y] = 1
        return new_mat
    else:
        new_val = subj_pref[sched if "CE" in sched else sched[:-1]][r][c] if sched!='-' else 1
        return new_val

def randomization_twelve(sched, swapped, subj_pref, sched_fit):
    r1, r2 = 0, 0
    c1, c2 = 0, 0
    while(True):
        r1, r2 = random.randint(0, 7), random.randint(0, 7)
        c1, c2 = random.randint(0, 3), random.randint(0, 3)
        if sched[r1][c1] == 'CE2' or sched[r2][c2] == 'CE2':
            continue
        if 'CE' not in sched[r1][c1]:
            if sched[r1][c1] in swapped[c2]:
                continue
            if sched[r1][c1] == '-':
                continue
        if 'CE' not in sched[r2][c2]:
            if sched[r2][c2] in swapped[c1]:
                continue
            if sched[r2][c2] == '-':
                continue
        break
        
    temp = sched[r1][c1]
    sched[r1][c1] = sched[r2][c2]
    sched[r2][c2] = temp

    sched_fit[r1][c1] = get_fitness('value', sched[r1][c1], subj_pref, r1, c1)
    sched_fit[r2][c2] = get_fitness('value', sched[r2][c2], subj_pref, r2, c2)
    swapped = swapaxes(sched, 8, 4)
    return sched, swapped, sched_fit

def hello():
    print("hello")

def randomization(sched, swapped, subj_pref, sched_fit):
    r1, r2 = 0, 0
    c1, c2 = 0, 0
    while(True):
        r1, r2 = random.randint(0, 7), random.randint(0, 7)
        c1, c2 = random.randint(0, 3), random.randint(0, 3)
        if 'CE' not in sched[r1][c1]:
            if sched[r1][c1] in swapped[c2]:
                continue
            if sched[r1][c1] == '-':
                continue
        if 'CE' not in sched[r2][c2]:
            if sched[r2][c2] in swapped[c1]:
                continue
            if sched[r2][c2] == '-':
                continue
        break
    
    temp = sched[r1][c1]
    sched[r1][c1] = sched[r2][c2]
    sched[r2][c2] = temp

    sched_fit[r1][c1] = get_fitness('value', sched[r1][c1], subj_pref, r1, c1)
    sched_fit[r2][c2] = get_fitness('value', sched[r2][c2], subj_pref, r2, c2)
    
    swapped = swapaxes(sched, 8, 4)
    return sched, swapped, sched_fit

def eval_gui(iters,in_subj, in_teach):
    columns, rows = (4, 8)                                      
    col, row = (0, 0)

    sched = [['0']*columns for _ in range(rows)]
    sched[0][0] = '-'                               #slot for flag cem shouldnt be affected
                                         
    filipino = Subject("Filipino", 3, "1-1-True")
    english = Subject("English", 3, "1-1-True")
    social_science = Subject("Social Science", 3, "1-1-True")

    research = Subject("Research", 3, "1-1-True")
    mathematics = Subject("Mathematics", 3, "1-1-True")

    physics = Subject("Physics", 3, "1-1-True")
    chemistry = Subject("Chemistry", 3, "1-1-True")
    biology = Subject("Biology", 3, "1-1-True")

    computer_science = Subject("Computer Science", 3, "1-1-True")
    technology = Subject("Technology", 3, "1-1-True")
    agriculture = Subject("Agriculture", 3, "1-1-True")
    engineering = Subject("Engineering", 3, "1-1-True")

    subject_list = [
            filipino, english, social_science,
            research, mathematics,
            physics, chemistry, biology,
            computer_science, technology, agriculture, engineering
            ]

    filipino_teacher = Teacher("janryl", "1-1-True")
    english_teacher = Teacher("zaldy", "1-1-True")
    social_science_teacher = Teacher("tabs", "1-1-True")

    research_teacher = Teacher("rox", "1-1-True")
    mathematics_teacher = Teacher("jov", "1-1-True")

    physics_teacher = Teacher("liza", "1-1-True")
    chemistry_teacher = Teacher("luv", "1-1-True")
    biology_teacher = Teacher("rose", "1-1-True")

    computer_science_teacher = Teacher("sheena", "1-1-True")
    technology_teacher = Teacher("kevin", "1-1-True")
    agriculture_teacher = Teacher("kz", "1-1-True")
    engineering_teacher = Teacher("glad", "1-1-True")


    teacher_list = [
            filipino_teacher, english_teacher, social_science_teacher,
            research_teacher, mathematics_teacher,
            physics_teacher, chemistry_teacher, biology_teacher,
            computer_science_teacher, technology_teacher, agriculture_teacher, engineering_teacher
            ]

    humss  = [[0]*4 for i in range(8)]
    rs_math  = [[0]*4 for i in range(8)]
    core_elec_1  = [[0]*4 for i in range(8)]
    core_elec_2  = [[0]*4 for i in range(8)]

    for (subject,insubj) in zip(subject_list, in_subj):
        subject.neighbors(insubj)

    for (teacher,inteach) in zip(teacher_list, in_teach):
        teacher.neighbors(inteach)

    start = time.time()
    for k in range(0, len(subject_list)):
        for i in range(0, len(subject_list[k].prefTime)):
            for j in range(0, len(subject_list[k].prefTime[i])):
                 if subject_list[k].name in ("English", "Filipino","Social Science"):#k in range(0, 3)
                     humss[i][j] += (subject_list[k].prefTime[i][j] + teacher_list[k].prefTime[i][j])/6.00
                 if subject_list[k].name in ("Mathematics", "Research"):#k in range(3, 5):
                     rs_math[i][j] += (subject_list[k].prefTime[i][j] + teacher_list[k].prefTime[i][j])/4.00
                 if subject_list[k].name in ("Physics", "Chemistry", "Biology"):#k in range(5, 8):
                     core_elec_1[i][j] += (subject_list[k].prefTime[i][j] + teacher_list[k].prefTime[i][j])/6.00
                     core_elec_2[i][j] += (subject_list[k].prefTime[i][j] + teacher_list[k].prefTime[i][j])/14.0
                 if subject_list[k].name in ("Computer Science", "Technology", "Agriculture", "Engineering"):#k in range(8, 12):
                     core_elec_2[i][j] += (subject_list[k].prefTime[i][j] + teacher_list[k].prefTime[i][j])/14.0

    grade_eleven_sched = [[['0']*columns for _ in range(rows)] for _ in range(3)]
    grade_twelve_sched = [[['0']*columns for _ in range(rows)] for _ in range(3)]

    labels = [
        ["HUMSS1", 3], ["HUMSS2", 3], ["HUMSS3", 3],
        ["RMF1", 3], ["RMF2", 3], ["RMF3", 3],
        ["CE1", 5], ["CE2", 5]
    ]

    subjects = {"HUMSS1":["SS", "FIL", "ENG"], "HUMSS2":["ENG", "SS", "FIL"], "HUMSS3":["FIL", "ENG", "SS"],
                "RMF1":["RS", "MATH", "-"], "RMF2":["-", "RS", "MATH"], "RMF3":["MATH", "-", "RS"]}

    subject_preference ={   "HUMSS":humss,
                            "RMF":rs_math,
                            "CE1":core_elec_1,
                            "CE2":core_elec_2}

    for _ in range(3):                                          #for empty slot assignment
        while(True):
            day = random.randint(0, 3)
            if sched[7][day] == '0':
                break
        sched[7][day] = '-'

    swapped_sched = swapaxes(sched, rows, columns)

    for group in labels:                                        #loop for randomly assigning labels in a sched
        for _ in range(group[1]):
            while(True):
                col = random.randint(0, 3)
                row = random.randint(0, 7)
                if sched[row][col] == '0':
                    if 'CE' in group[0]:
                        break
                    else:
                        if group[0] not in swapped_sched[col]:
                            break
            sched[row][col] = swapped_sched[col][row] = group[0]

    sched_fitness = get_fitness("matrix", sched, subject_preference, rows, columns)

    max_sched = sched
    max_fitness = sched_fitness
    max_val = overall_fitness(sched_fitness)

    for x in range(iters):
        sched, swapped_sched, sched_fitness = randomization(sched, swapped_sched, subject_preference, sched_fitness)
        temp = overall_fitness(sched_fitness)
        if temp > max_val:
            print('Max val found!', x)
            max_val = temp
            max_fitness = sched_fitness
            max_sched = sched

    print("MAXIMUM FITNESS: ", '%.5f'%max_val, '\n')

    for x in range(rows):                                       #for assigning subjects to section scheds
        for y in range(columns):
            for z in range(3):
                grade_eleven_sched[z][x][y] = max_sched[x][y] if max_sched[x][y] not in subjects else subjects[max_sched[x][y]][z]

    #for x in range(3):
    #    for y in range(rows):
    #        print('\t'.join(word.ljust(6) for word in grade_eleven_sched[x][y]), end="\n")
    #    print("\n")
        
    for x in range(rows):
        for y in range(columns):
            if max_sched[x][y] == '-' or 'CE2' in max_sched[x][y]:
                sched[x][y] = max_sched[x][y]
            else:
                sched[x][y] = '0'

    swapped_sched = swapaxes(sched, rows, columns)

    for group in labels:                                        #loop for randomly assigning labels in a sched
        for _ in range(group[1]):
            if group[0] == 'CE2':
                continue
            while(True):
                col = random.randint(0, 3)
                row = random.randint(0, 7)
                if sched[row][col] == '0':
                    if 'CE' in group[0]:
                        break
                    else:
                        if group[0] not in swapped_sched[col]:
                            break
            sched[row][col] = swapped_sched[col][row] = group[0]

    sched_fitness = get_fitness("matrix", sched, subject_preference, rows, columns)

    max_sched = sched
    max_fitness = sched_fitness
    max_val = overall_fitness(sched_fitness)

    for x in range(iters):
        sched, swapped_sched, sched_fitness = randomization_twelve(sched, swapped_sched, subject_preference, sched_fitness)
        temp = overall_fitness(sched_fitness)
        if temp > max_val:
            print('Max val found!', x)
            max_val = temp
            max_fitness = sched_fitness
            max_sched = sched

    for x in range(rows):                                       #for assigning subjects to section scheds
        for y in range(columns):
            for z in range(3):
                    grade_twelve_sched[z][x][y] = max_sched[x][y] if max_sched[x][y] not in subjects else subjects[max_sched[x][y]][z]

    #print("Grade 12")
    #for x in range(3):
    #    for y in range(rows):
    #        print('\t'.join(word.ljust(6) for word in grade_twelve_sched[x][y]), end="\n")
    #    print("\n")

    #print(grade_twelve_sched)
    
    end = time.time()
    print("ELAPSED TIME: ", end - start)
    xl.write_excel(grade_eleven_sched,grade_twelve_sched)
    return True

####################################################
