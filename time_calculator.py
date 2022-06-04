

def add_time(start, add_time, *args):
    hours_additional = 0
    accumulator, day_counter = 0, 0
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    #Convert data into integers and split correctly
    time_start, meridiem = start.split()
    hours_add, min_add = list(map(lambda i: int(i), add_time.split(":")))
    hours_start, min_start = list(map(lambda i: int(i), time_start.split(":")))
    alter_meridiem = meridiem
    if(meridiem == "AM"):
        inverse_meridiem = "PM"
    elif(meridiem == "PM"):
        inverse_meridiem = "AM"

    result_min = min_start + min_add
    
    if(result_min > 60):
        hours_additional = 1 
        min_refill = result_min - 60
        result_min = min_refill
    if(result_min < 10):
        result_min = str(result_min).zfill(2)

    result_hours = hours_start + hours_add + hours_additional

    if(meridiem == "AM" and hours_add < 12):
        result_days_rounded = 0
    else:
        result_days_rounded = round(result_hours / 24)

    if(result_hours >= 12):
        i = 1
        hours_refill = result_hours - 12 
        while(hours_refill > 12):
            hours_refill -= 12
            i += 1
        if(hours_refill == 12):
            i += 1
        if(hours_refill != 0):
            result_hours = hours_refill
        if(i % 2 != 0):
            alter_meridiem = inverse_meridiem
        elif(i % 2 == 0):
            alter_meridiem = meridiem

    if(args != ()):
        index = week_days.index(args[0].title())
        day_selected = result_days_rounded + index
        while(day_selected > 6):
            day_selected -= 7
            
    if(result_days_rounded == 1):
        day_counter = "next day"
        result_timer = f"{result_hours}:{result_min} {alter_meridiem} ({day_counter})"
        if(args != ()):
            result_timer = f"{result_hours}:{result_min} {alter_meridiem}, {week_days[day_selected]} ({day_counter})"

    elif(result_days_rounded > 1):
        day_counter = f"{result_days_rounded} days later"
        result_timer = f"{result_hours}:{result_min} {alter_meridiem} ({day_counter})"
        if(args != ()):
            result_timer = f"{result_hours}:{result_min} {alter_meridiem}, {week_days[day_selected]} ({day_counter})"

    else:            
        result_timer = f"{result_hours}:{result_min} {alter_meridiem}"
        if(args != ()):
            result_timer = f"{result_hours}:{result_min} {alter_meridiem}, {week_days[day_selected]}" 
     
    return result_timer