import pandas as pd
comma = ','
df = pd.read_csv('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Vora ma\'am\'s work\\example_with_year.csv')
file_diploma_3rd_year = open('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Vora ma\'am\'s work\\example_diploma_3rd_year.csv','a')
file_diploma_4th_year = open('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Vora ma\'am\'s work\\example_diploma_4th_year.csv','a')
file_XII_3rd_year = open('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Vora ma\'am\'s work\\example_XII_3rd_year.csv','a')
file_XII_4th_year = open('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Vora ma\'am\'s work\\example_XII_4th_year.csv','a')

file_diploma_3rd_year.write('OHU'+ comma +'Gender'+ comma +'Age'+ comma +
                  'Religion'    + comma +     'Caste'    + comma +     'Scholarship'    + comma +
                  'Time_to_reach_college(HRS)'    + comma +     'X_pct'    + comma +
                  'X_Board'    + comma +    'Diploma_pct'    + comma +     'University'    + comma +
                  'Private_Class'    + comma +     'Number_of_Subjects'    + comma +
                  'Overall_Attendance'    + comma +     'Major_Illness'    + comma +
                  'Fathers_Ocuupation'    + comma +     'Fathers_Education'    + comma +
                  'F_Stream'    + comma +     'F_Health_Issue'    + comma +
                  'Mothers_Ocuupation'    + comma +     'Mothers_Education'    + comma +
                  'M_Stream'    + comma +     'M_Health_Issue'    + comma +
                  'Family_Income'    + comma +     'No_of_Siblings'    + comma +
                  'Extra_Curricular_Activity'    + comma +     'Active_in_Sports'    + comma +
                  'Drop'    + comma+     'SEM3_CGPA'    + comma +
                  'SEM3_KT'    + comma +     'SEM4_CGPA'    + comma +     'SEM4_KT'     + '\n')
file_diploma_4th_year.write(    'OHU'    + comma +     'Gender'    + comma +     'Age'    + comma +
                  'Religion'    + comma +     'Caste'    + comma +     'Scholarship'    + comma +
                  'Time_to_reach_college(HRS)'    + comma +     'X_pct'    + comma +
                  'X_Board'    + comma +    'Diploma_pct'    + comma +     'University'    + comma +
                  'Private_Class'    + comma +     'Number_of_Subjects'    + comma +
                  'Overall_Attendance'    + comma +     'Major_Illness'    + comma +
                  'Fathers_Ocuupation'    + comma +     'Fathers_Education'    + comma +
                  'F_Stream'    + comma +     'F_Health_Issue'    + comma +
                  'Mothers_Ocuupation'    + comma +     'Mothers_Education'    + comma +
                  'M_Stream'    + comma +     'M_Health_Issue'    + comma +
                  'Family_Income'    + comma +     'No_of_Siblings'    + comma +
                  'Extra_Curricular_Activity'    + comma +     'Active_in_Sports'    + comma +
                  'Drop'    + comma  +     'SEM3_CGPA'    + comma +
                  'SEM3_KT'    + comma +     'SEM4_CGPA'    + comma +     'SEM4_KT'     + comma +     'SEM5_CGPA'    + comma +     'SEM5_KT'     + comma +     'SEM6_CGPA'    + comma +     'SEM6_KT'     + '\n')
file_XII_3rd_year.write( 'OHU'  + comma +  'Gender'  + comma +  'Age'  + comma +
                  'Religion'  + comma +  'Caste'  + comma +  'Scholarship'  + comma +
                  'Time_to_reach_college(HRS)'  + comma +  'X_pct'  + comma +
                  'X_Board'  + comma +  'XII_pct'  + comma +  'XII_Board'  + comma +
                  'Private_Class'  + comma +  'Number_of_Subjects'  + comma +
                  'Overall_Attendance'  + comma +  'Major_Illness'  + comma +
                  'Score_of_Exam_CET'  + comma +  'Score_of_Exam_AIEEE'  + comma +
                  'Fathers_Ocuupation'  + comma +  'Fathers_Education'  + comma +
                  'F_Stream'  + comma +  'F_Health_Issue'  + comma +
                  'Mothers_Ocuupation'  + comma +  'Mothers_Education'  + comma +
                  'M_Stream'  + comma +  'M_Health_Issue'  + comma +
                  'Family_Income'  + comma +  'No_of_Siblings'  + comma +
                  'Extra_Curricular_Activity'  + comma +  'Active_in_Sports'  + comma +
                  'Drop'  + comma +  'SEM1_CGPA'  + comma +  'SEM1_KT'  + comma +
                  'SEM2_CGPA'  + comma +  'SEM2_KT'  + comma +  'SEM3_CGPA'  + comma +
                  'SEM3_KT'  + comma +  'SEM4_CGPA'  + comma +  'SEM4_KT'  + '\n')
file_XII_4th_year.write( 'OHU'  + comma +  'Gender'  + comma +  'Age'  + comma +
                  'Religion'  + comma +  'Caste'  + comma +  'Scholarship'  + comma +
                  'Time_to_reach_college(HRS)'  + comma +  'X_pct'  + comma +
                  'X_Board'  + comma +  'XII_pct'  + comma +  'XII_Board'  + comma +
                  'Private_Class'  + comma +  'Number_of_Subjects'  + comma +
                  'Overall_Attendance'  + comma +  'Major_Illness'  + comma +
                  'Score_of_Exam_CET'  + comma +  'Score_of_Exam_AIEEE'  + comma +
                  'Fathers_Ocuupation'  + comma +  'Fathers_Education'  + comma +
                  'F_Stream'  + comma +  'F_Health_Issue'  + comma +
                  'Mothers_Ocuupation'  + comma +  'Mothers_Education'  + comma +
                  'M_Stream'  + comma +  'M_Health_Issue'  + comma +
                  'Family_Income'  + comma +  'No_of_Siblings'  + comma +
                  'Extra_Curricular_Activity'  + comma +  'Active_in_Sports'  + comma +
                  'Drop'  + comma +  'SEM1_CGPA'  + comma +  'SEM1_KT'  + comma +
                  'SEM2_CGPA'  + comma +  'SEM2_KT'  + comma +  'SEM3_CGPA'  + comma +
                  'SEM3_KT'  + comma +  'SEM4_CGPA'  + comma +  'SEM4_KT'  + comma +     'SEM5_CGPA'    + comma +     'SEM5_KT'     + comma +     'SEM6_CGPA'    + comma +     'SEM6_KT'    + '\n')
# print(df.head())
# print(len(df['S.No']))

for i in range(len(df['S.No'])):
    # print(df['Diploma_pct'][i], df['SEM6_CGPA'][i])
    if df['XII_pct'][i] == 'NA_exam_not_given':
        if df['SEM6_CGPA'][i] == 'NA_3rd_Year':
            values_to_save = str(df['OHU'][i]) + comma + str(df['Gender'][i]) + comma + str(df['Age'][i]) + comma + str(
                df['Religion'][i]) + comma + str(df['Caste'][i]) + comma + str(df['Scholarship'][i]) + comma + str(
                df['Time_to_reach_college(HRS)'][i]) + comma + str(df['X_pct'][i]) + comma + str(
                df['X_Board'][i]) + comma +str(df['Diploma_pct'][i]) + comma + str(df['University'][i]) + comma + str(
                df['Private_Class'][i]) + comma + str(df['Number_of_Subjects'][i]) + comma + str(
                df['Overall_Attendance'][i]) + comma + str(df['Major_Illness'][i]) + comma + str(
                df['Fathers_Ocuupation'][i]) + comma + str(df['Fathers_Education'][i]) + comma + str(
                df['F_Stream'][i]) + comma + str(df['F_Health_Issue'][i]) + comma + str(
                df['Mothers_Ocuupation'][i]) + comma + str(df['Mothers_Education'][i]) + comma + str(
                df['M_Stream'][i]) + comma + str(df['M_Health_Issue'][i]) + comma + str(
                df['Family_Income'][i]) + comma + str(df['No_of_Siblings'][i]) + comma + str(
                df['Extra_Curricular_Activity'][i]) + comma + str(df['Active_in_Sports'][i]) + comma + str(
                df['Drop'][i]) + comma + str(df['SEM3_CGPA'][i]) + comma + str(
                df['SEM3_KT'][i]) + comma + str(df['SEM4_CGPA'][i]) + comma + str(df['SEM4_KT'][i])  + '\n'
            file_diploma_3rd_year.write(values_to_save)
        else:
            values_to_save = str(df['OHU'][i]) + comma + str(df['Gender'][i]) + comma + str(df['Age'][i]) + comma + str(
                df['Religion'][i]) + comma + str(df['Caste'][i]) + comma + str(df['Scholarship'][i]) + comma + str(
                df['Time_to_reach_college(HRS)'][i]) + comma + str(df['X_pct'][i]) + comma + str(
                df['X_Board'][i]) + comma + str(df['Diploma_pct'][i]) + comma + str(df['University'][i]) + comma + str(
                df['Private_Class'][i]) + comma + str(df['Number_of_Subjects'][i]) + comma + str(
                df['Overall_Attendance'][i]) + comma + str(df['Major_Illness'][i]) + comma + str(
                df['Fathers_Ocuupation'][i]) + comma + str(df['Fathers_Education'][i]) + comma + str(
                df['F_Stream'][i]) + comma + str(df['F_Health_Issue'][i]) + comma + str(
                df['Mothers_Ocuupation'][i]) + comma + str(df['Mothers_Education'][i]) + comma + str(
                df['M_Stream'][i]) + comma + str(df['M_Health_Issue'][i]) + comma + str(
                df['Family_Income'][i]) + comma + str(df['No_of_Siblings'][i]) + comma + str(
                df['Extra_Curricular_Activity'][i]) + comma + str(df['Active_in_Sports'][i]) + comma + str(
                df['Drop'][i]) + comma + str(df['SEM3_CGPA'][i]) + comma + str(
                df['SEM3_KT'][i]) + comma + str(df['SEM4_CGPA'][i]) + comma + str(df['SEM4_KT'][i]) + comma + str(
                df['SEM5_CGPA'][i]) + comma + str(df['SEM5_KT'][i]) + comma + str(df['SEM6_CGPA'][i]) + comma + str(
                df['SEM6_KT'][i]) + '\n'
            file_diploma_4th_year.write(values_to_save)
    else:
        if df['SEM6_CGPA'][i] == 'NA_3rd_Year':
            values_to_save = str(df['OHU'][i]) + comma + str(df['Gender'][i]) + comma + str(df['Age'][i]) + comma + str(
                df['Religion'][i]) + comma + str(df['Caste'][i]) + comma + str(df['Scholarship'][i]) + comma + str(
                df['Time_to_reach_college(HRS)'][i]) + comma + str(df['X_pct'][i]) + comma + str(
                df['X_Board'][i]) + comma + str(df['XII_pct'][i]) + comma + str(df['XII_Board'][i]) + comma + str(
                df['Private_Class'][i]) + comma + str(df['Number_of_Subjects'][i]) + comma + str(
                df['Overall_Attendance'][i]) + comma + str(df['Major_Illness'][i]) + comma + str(
                df['Score_of_Exam_CET'][i]) + comma + str(df['Score_of_Exam_AIEEE'][i]) + comma + str(
                df['Fathers_Ocuupation'][i]) + comma + str(df['Fathers_Education'][i]) + comma + str(
                df['F_Stream'][i]) + comma + str(df['F_Health_Issue'][i]) + comma + str(
                df['Mothers_Ocuupation'][i]) + comma + str(df['Mothers_Education'][i]) + comma + str(
                df['M_Stream'][i]) + comma + str(df['M_Health_Issue'][i]) + comma + str(
                df['Family_Income'][i]) + comma + str(df['No_of_Siblings'][i]) + comma + str(
                df['Extra_Curricular_Activity'][i]) + comma + str(df['Active_in_Sports'][i]) + comma + str(
                df['Drop'][i]) + comma + str(df['SEM1_CGPA'][i]) + comma + str(df['SEM1_KT'][i]) + comma + str(
                df['SEM2_CGPA'][i]) + comma + str(df['SEM2_KT'][i]) + comma + str(df['SEM3_CGPA'][i]) + comma + str(
                df['SEM3_KT'][i]) + comma + str(df['SEM4_CGPA'][i]) + comma + str(df['SEM4_KT'][i]) + '\n'
            file_XII_3rd_year.write(values_to_save)
        else:
            values_to_save = str(df['OHU'][i]) + comma + str(df['Gender'][i]) + comma + str(df['Age'][i]) + comma + str(
                df['Religion'][i]) + comma + str(df['Caste'][i]) + comma + str(df['Scholarship'][i]) + comma + str(
                df['Time_to_reach_college(HRS)'][i]) + comma + str(df['X_pct'][i]) + comma + str(
                df['X_Board'][i]) + comma + str(df['XII_pct'][i]) + comma + str(df['XII_Board'][i]) + comma + str(
                df['Private_Class'][i]) + comma + str(df['Number_of_Subjects'][i]) + comma + str(
                df['Overall_Attendance'][i]) + comma + str(df['Major_Illness'][i]) + comma + str(
                df['Score_of_Exam_CET'][i]) + comma + str(df['Score_of_Exam_AIEEE'][i]) + comma + str(
                df['Fathers_Ocuupation'][i]) + comma + str(df['Fathers_Education'][i]) + comma + str(
                df['F_Stream'][i]) + comma + str(df['F_Health_Issue'][i]) + comma + str(
                df['Mothers_Ocuupation'][i]) + comma + str(df['Mothers_Education'][i]) + comma + str(
                df['M_Stream'][i]) + comma + str(df['M_Health_Issue'][i]) + comma + str(
                df['Family_Income'][i]) + comma + str(df['No_of_Siblings'][i]) + comma + str(
                df['Extra_Curricular_Activity'][i]) + comma + str(df['Active_in_Sports'][i]) + comma + str(
                df['Drop'][i]) + comma + str(df['SEM1_CGPA'][i]) + comma + str(df['SEM1_KT'][i]) + comma + str(
                df['SEM2_CGPA'][i]) + comma + str(df['SEM2_KT'][i]) + comma + str(df['SEM3_CGPA'][i]) + comma + str(
                df['SEM3_KT'][i]) + comma + str(df['SEM4_CGPA'][i]) + comma + str(df['SEM4_KT'][i]) + comma + str(
                df['SEM5_CGPA'][i]) + comma + str(df['SEM5_KT'][i]) + comma + str(df['SEM6_CGPA'][i]) + comma + str(
                df['SEM6_KT'][i]) + '\n'
            file_XII_4th_year.write(values_to_save)

file_diploma_3rd_year.close()
file_diploma_4th_year.close()
file_XII_3rd_year.close()
file_XII_4th_year.close()