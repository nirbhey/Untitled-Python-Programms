import random

file_to_edit = open('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Vora ma\'am\'s work\\example_with_year.csv', 'a')
number_of_samples = 1000
comma = ','

OHU = []
Gender = []
Age = []
Religion = []
Caste = []
Scholarship = []
Time_to_reach_college = []
X_pct = []
X_Board = []
XII_pct = 0
XII_Board = 0
Diploma_pct = 0
University = 0
Private_Class = 0
Number_of_Subjects = 0
Overall_Attendance = []
Major_Illness = []
Score_of_Exam_CET = 0
Score_of_Exam_AIEEE = 0
Fathers_Ocuupation = []
Fathers_Education = []
F_Stream = []
F_Health_Issue = []
Mothers_Ocuupation = []
Mothers_Education = []
M_Stream = []
M_Health_Issue = []
Family_Income = []
No_of_Siblings = []
Extra_Curricular_Activity = []
Active_in_Sports = []
Drop = []
SEM1_CGPA = []
SEM1_KT = []
SEM2_CGPA = []
SEM2_KT = []
SEM3_CGPA = []
SEM3_KT = []
SEM4_CGPA = []
SEM4_KT = []
SEM5_CGPA = []
SEM5_KT = []
SEM6_CGPA = []
SEM6_KT = []

for i in range(number_of_samples):
    Age.append(random.randrange(21, 25))
    Time_to_reach_college.append(str(random.randrange(20, 120)))
    X_pct.append(str(random.randrange(50, 96)))
    Overall_Attendance.append(str(random.randrange(1, 4)))
    Fathers_Ocuupation.append(str(random.randrange(1, 5)))
    Fathers_Education.append(str(random.randrange(1, 4)))
    F_Stream.append(str(random.randrange(1, 4)))
    F_Health_Issue.append(str(random.randrange(1, 3)))
    Mothers_Ocuupation.append(str(random.randrange(1, 4)))
    Mothers_Education.append(str(random.randrange(1, 4)))
    M_Health_Issue.append(str(random.randrange(1, 4)))
    M_Stream.append(str(random.randrange(1, 4)))
    Family_Income.append(str(random.randrange(1, 4)))
    No_of_Siblings.append(str(random.randrange(1, 4)))
    Extra_Curricular_Activity.append(str(random.randrange(1, 4)))
    Active_in_Sports.append(str(random.randrange(1, 3)))

    if i < (number_of_samples / 10):
        OHU.append('1')
        Scholarship.append('2')
    else:
        OHU.append('0')
        Scholarship.append('1')

    if i % 2 == 0:
        Gender.append('1')
        Religion.append('1')
        Caste.append('3')
        X_Board.append('1')
        Major_Illness.append('2')

    else:
        Gender.append('2')
        Religion.append(str(random.randrange(2, 6)))
        Caste.append(str(random.randrange(1, 3)))
        X_Board.append(str(random.randrange(2, 4)))
        Major_Illness.append(str(random.randrange(1, 3)))

def cgpa_and_kt(is_diploma):
    kt_prob = random.randrange(0, 10)
    year_of_student = random.randrange(0,3)

    if kt_prob > 6:
        Drop = (str(random.randrange(1, 3)))
        if is_diploma == 0:
            x = random.randrange(0, 2)
            if x == 0:
                SEM1_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
                SEM1_KT = ('No_KT')
            else:
                SEM1_CGPA = ('No_CGPA')
                SEM1_KT = (str(random.randrange(1, 7)))
            x = random.randrange(0, 2)
            if x == 0:
                SEM2_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
                SEM2_KT = ('No_KT')
            else:
                SEM2_CGPA = ('No_CGPA')
                SEM2_KT = (str(random.randrange(1, 7)))
        else:
            SEM1_CGPA = ('NA_Diploma')
            SEM1_KT = ('NA_Diploma')
            SEM2_CGPA = ('NA_Diploma')
            SEM2_KT = ('NA_Diploma')

        x = random.randrange(0, 2)
        if x == 0:
            SEM3_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
            SEM3_KT = ('No_KT')
        else:
            SEM3_CGPA = ('No_CGPA')
            SEM3_KT = (str(random.randrange(1, 7)))
        x = random.randrange(0, 2)
        if x == 0:
            SEM4_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
            SEM4_KT = ('No_KT')
        else:
            SEM4_CGPA = ('No_CGPA')
            SEM4_KT = (str(random.randrange(1, 7)))
        if year_of_student < 2:
            x = random.randrange(0, 2)
            if x == 0:
                SEM5_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
                SEM5_KT = ('No_KT')
            else:
                SEM5_CGPA = ('No_CGPA')
                SEM5_KT = (str(random.randrange(1, 7)))
            x = random.randrange(0, 2)
            if x == 0:
                SEM6_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
                SEM6_KT = ('No_KT')
            else:
                SEM6_CGPA = ('No_CGPA')
                SEM6_KT = (str(random.randrange(1, 7)))
        else:
            SEM5_CGPA = ('NA_3rd_Year')
            SEM5_KT = ('NA_3rd_Year')
            SEM6_CGPA = ('NA_3rd_Year')
            SEM6_KT = ('NA_3rd_Year')


    else:
        Drop = (2)
        if is_diploma == 0:
            SEM1_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
            SEM1_KT = ('No_KT')
            SEM2_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
            SEM2_KT = ('No_KT')
        else:
            SEM1_CGPA = ('NA_Diploma')
            SEM1_KT = ('NA_Diploma')
            SEM2_CGPA = ('NA_Diploma')
            SEM2_KT = ('NA_Diploma')
        SEM3_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
        SEM3_KT = ('No_KT')
        SEM4_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
        SEM4_KT = ('No_KT')
        if year_of_student < 2:
            SEM5_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
            SEM5_KT = ('No_KT')
            SEM6_CGPA = (str(random.randrange(5, 10)) + '.' + str(random.randrange(0, 100)))
            SEM6_KT = ('No_KT')
        else:
            SEM5_CGPA = ('NA_3rd_Year')
            SEM5_KT = ('NA_3rd_Year')
            SEM6_CGPA = ('NA_3rd_Year')
            SEM6_KT = ('NA_3rd_Year')

    return Drop, SEM1_CGPA, SEM1_KT, SEM2_CGPA, SEM2_KT, SEM3_CGPA, SEM3_KT, SEM4_CGPA, SEM4_KT, SEM5_CGPA, SEM5_KT, SEM6_CGPA, SEM6_KT


def make_related_values():
    Private_Class = (random.randrange(1, 3))
    is_diploma = 0
    if (Private_Class == 1):
        Number_of_Subjects = (str(random.randrange(1, 6)))
    else:
        Number_of_Subjects = (str(0))
    # print(Private_Class[i], Number_of_Subjects[i])
    # print((x,i,number_of_samples-i))
    rand = random.randrange(0, 5)
    if rand > 3:
        if i % 3 == 0:
            is_diploma = 1
            XII_Board = ('NA_exam_not_given')
            XII_pct = ('NA_exam_not_given')
            Score_of_Exam_AIEEE = ('NA_exam_not_given')
            Score_of_Exam_CET = ('NA_exam_not_given')
            Diploma_pct = (str(random.randrange(60, 91)))
            if i % 2 == 0:
                University = ('2')
            else:
                University = ('1')
        else:
            XII_Board = ('1')
            XII_pct = (str(random.randrange(50, 96)))
            Diploma_pct = ('NA_exam_not_given')
            University = ('NA_exam_not_given')
            Score_of_Exam_AIEEE = (str(random.randrange(120, 280)))
            Score_of_Exam_CET = (str(random.randrange(75, 180)))
    else:
        XII_Board = (str(random.randrange(2, 4)))
        XII_pct = (str(random.randrange(50, 96)))
        Diploma_pct = ('NA_exam_not_given')
        University = ('NA_exam_not_given')
        Score_of_Exam_AIEEE = (str(random.randrange(120, 280)))
        Score_of_Exam_CET = (str(random.randrange(75, 180)))

    Drop, SEM1_CGPA, SEM1_KT, SEM2_CGPA, SEM2_KT, SEM3_CGPA, SEM3_KT, SEM4_CGPA, SEM4_KT, SEM5_CGPA, SEM5_KT, SEM6_CGPA, SEM6_KT = cgpa_and_kt(is_diploma)

    return Private_Class, Number_of_Subjects, XII_Board, XII_pct, Score_of_Exam_AIEEE, Score_of_Exam_CET, Diploma_pct, University, Drop, SEM1_CGPA, SEM1_KT, SEM2_CGPA, SEM2_KT, SEM3_CGPA, SEM3_KT, SEM4_CGPA, SEM4_KT, SEM5_CGPA, SEM5_KT, SEM6_CGPA, SEM6_KT


def make_file():
    file_to_edit = open('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Vora ma\'am\'s work\\example_with_year.csv','a')
    file_to_edit.write('S.No,OHU,Gender,Age,Religion,Caste,Scholarship,Time_to_reach_college(HRS),X_pct,X_Board,XII_pct,XII_Board,Diploma_pct,University,Private_Class,Number_of_Subjects,Overall_Attendance,Major_Illness,Score_of_Exam_CET,Score_of_Exam_AIEEE,Fathers_Ocuupation,Fathers_Education,F_Stream,F_Health_Issue,Mothers_Ocuupation,Mothers_Education,M_Stream,F_Health_Issue,Family_Income,No_of_Siblings,Extra_Curricular_Activity,Active_in_Sports,Drop,SEM1_CGPA,SEM1_KT,SEM2_CGPA,SEM2_KT,SEM3_CGPA,SEM3_KT,SEM4_CGPA,SEM4_KT,SEM5_CGPA,SEM5_KT,SEM6_CGPA,SEM6_KT\n')
    file_to_edit.close()



make_file()

for i in range(0, number_of_samples):
    x = random.randrange(0, number_of_samples - i)
    Private_Class, Number_of_Subjects, XII_Board, XII_pct, Score_of_Exam_AIEEE, Score_of_Exam_CET, Diploma_pct, University, Drop, SEM1_CGPA, SEM1_KT, SEM2_CGPA, SEM2_KT, SEM3_CGPA, SEM3_KT, SEM4_CGPA, SEM4_KT, SEM5_CGPA, SEM5_KT, SEM6_CGPA, SEM6_KT = make_related_values()

    values_to_save = str(i + 1) + comma + str(OHU[x])+comma+str(Gender[x])+comma+str(Age[x])+comma+str(Religion[x])+comma+str(Caste[x])+comma+str(Scholarship[x])+comma+str(Time_to_reach_college[x])+comma+str(X_pct[x])+comma+str(X_Board[x])+comma+str(XII_pct)+comma+str(XII_Board)+comma+str(Diploma_pct)+comma+str(University)+comma+str(Private_Class)+comma+str(Number_of_Subjects)+comma+str(Overall_Attendance[x])+comma+str(Major_Illness[x])+comma+str(Score_of_Exam_CET)+comma+str(Score_of_Exam_AIEEE)+comma+str(Fathers_Ocuupation[x])+comma+str(Fathers_Education[x])+comma+str(F_Stream[x])+comma+str(F_Health_Issue[x])+comma+str(Mothers_Ocuupation[x])+comma+str(Mothers_Education[x])+comma+str(M_Stream[x])+comma+str(M_Health_Issue[x])+comma+str(Family_Income[x])+comma+str(No_of_Siblings[x])+comma+str(Extra_Curricular_Activity[x])+comma+str(Active_in_Sports[x])+comma+str(Drop)+comma+str(SEM1_CGPA)+comma+str(SEM1_KT)+comma+str(SEM2_CGPA)+comma+str(SEM2_KT)+comma+str(SEM3_CGPA)+comma+str(SEM3_KT)+comma+str(SEM4_CGPA)+comma+str(SEM4_KT)+comma+str(SEM5_CGPA)+comma+str(SEM5_KT)+comma+str(SEM6_CGPA)+comma+str(SEM6_KT )+ '\n'

    file_to_edit.write(values_to_save)
    OHU.remove(OHU[x])
    Gender.remove(Gender[x])
    Age.remove(Age[x])
    Religion.remove(Religion[x])
    Caste.remove(Caste[x])
    Scholarship.remove(Scholarship[x])
    Time_to_reach_college.remove(Time_to_reach_college[x])
    X_pct.remove(X_pct[x])
    X_Board.remove(X_Board[x])
    Overall_Attendance.remove(Overall_Attendance[x])
    Major_Illness.remove(Major_Illness[x])
    Fathers_Ocuupation.remove(Fathers_Ocuupation[x])
    Fathers_Education.remove(Fathers_Education[x])
    F_Stream.remove(F_Stream[x])
    F_Health_Issue.remove(F_Health_Issue[x])
    Mothers_Ocuupation.remove(Mothers_Ocuupation[x])
    Mothers_Education.remove(Mothers_Education[x])
    M_Stream.remove(M_Stream[x])
    M_Health_Issue.remove(M_Health_Issue[x])
    Family_Income.remove(Family_Income[x])
    No_of_Siblings.remove(No_of_Siblings[x])
    Extra_Curricular_Activity.remove(Extra_Curricular_Activity[x])
    Active_in_Sports.remove(Active_in_Sports[x])

file_to_edit.close()