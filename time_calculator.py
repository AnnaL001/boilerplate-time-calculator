def add_time(start_time, duration, start_day=""):
    final_result = ""
    days_later = ""
    new_day = ""
    no_of_days = 0
    start_day = start_day.capitalize()
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    s_time = start_time.split()
    # Dictionary to remove the colon (ASCII code 58) from time and duration
    replacement_chars = {58: ""}
    working_time = s_time[0].translate(replacement_chars)
    working_am_pm = s_time[1]
    working_duration = duration.translate(replacement_chars)

    # Add duration to start-time in 24hr format
    if working_am_pm == "AM":
        result = str(int(working_time) + int(working_duration))
    else:
        result = str(int(working_time) + 1200 + int(working_duration))

    # Check if minutes is less than 60
    if int(result[-2:]) < 60:
        working_result = int(result)
    else:
        # Subtract 60 from minutes then add 1 to hour(s) where total value = 100
        working_result = int(result) - 60 + 100

    # Conversion to time in 24hrs format and no of days
    if working_result >= 2400:
        no_of_days = int(working_result / 2400)
        new_result = working_result % 2400
        if no_of_days == 1:
            days_later = f' (next day)'
        else:
            days_later = f' ({no_of_days} days later)'
    else:
        new_result = working_result

    # Retrieve new day of the week after adding the duration
    if start_day in days_of_the_week:
        old_index = days_of_the_week.index(start_day)
        new_index = old_index + no_of_days
        if new_index <= len(days_of_the_week):
            # New index within length of days in a week
            new_day = f', {days_of_the_week[new_index]}'
        else:
            # New index exceeds length of days in a week
            new_day = f', {days_of_the_week[(new_index % len(days_of_the_week))]}'

    # Determine time in AM/PM
    if 0 <= new_result <= 59:
        am_pm = "AM"
        new_time = str(new_result + 1200)
    elif 59 < new_result < 1200:
        am_pm = "AM"
        new_time = str(new_result)
    elif 1200 <= new_result < 1300:
        am_pm = "PM"
        new_time = str(new_result)
    else:
        am_pm = "PM"
        new_time = str(new_result - 1200)

    # Display the new time
    if len(new_time) == 4:
        final_result = f'{new_time[0:2]}:{new_time[2:]} {am_pm}{new_day}{days_later}'
    elif len(new_time) == 3:
        final_result = f'{new_time[0:1]}:{new_time[1:]} {am_pm}{new_day}{days_later}'

    return final_result
