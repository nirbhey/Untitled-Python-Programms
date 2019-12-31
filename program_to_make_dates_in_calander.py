from datetime import date, timedelta

date_from = "2017-04-02"

def dates_with_same_day(date_from, d0):
    col = []
    row = []
    cal_list = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]
                ]
    month_var = int(date_from[5:7])
    day_count = 1
    day_var_d0 = d0.weekday()

    print(date_from, month_var, day_var_d0)

    if month_var == 2:
        if (int(date_from[:4]) == 2016):
            number_of_days_var = 29
        else:
            number_of_days_var = 28
    elif (month_var == 1) | (month_var == 3) | (month_var == 5) | (month_var == 7) | (month_var == 8) | (
                month_var == 10) | (month_var == 12):
        number_of_days_var = 31
    else:
        number_of_days_var = 30

    d1 = date(int(date_from[:4]), int(date_from[5:7]), 1)
    day_var_d1 = d1.weekday()

    print(date_from, month_var, day_var_d1, d1)

    for i in range(day_var_d1, 7):
        cal_list[0][i] = day_count
        day_count += 1
    for i in range(1, 6):
        if day_count > number_of_days_var:
            print(day_count, number_of_days_var)
            break
        for j in range(0, 7):
            cal_list[i][j] = day_count
            day_count += 1
            if day_count > number_of_days_var:
                print(day_count, number_of_days_var)
                break

    print(cal_list)
    x = [x for x in cal_list if int(date_from[8:10]) in x][0]
    print("x = " + str(x))
    print(cal_list.index(x), x.index(int(date_from[8:10])))
    row.append(cal_list.index(x))
    col.append(x.index(int(date_from[8:10])))

    return row, col

d0 = date(int(date_from[:4]), int(date_from[5:7]), int(date_from[8:10]))

row_var, col_var = dates_with_same_day(date_from, d0) # Make a function to search by this index in all previous years (2014 to 2016)
