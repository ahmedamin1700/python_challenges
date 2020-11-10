"""
 10 / 11 / 2020 Done by Ahmed Amin.
"""
WEEK_DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]


def convert_start_to_minutes(time: str) -> int:
    """
    Converts the start time from 12 hour format to minutes.
    :param time: str time 12 hour format.
    :return: int calculated minutes.
    """
    day = time.split()[1]
    hours = time.split()[0].split(":")[0]
    minutes = time.split()[0].split(":")[1]

    if day == "AM":
        result = (int(hours) * 60) + int(minutes)
        return result
    elif day == "PM":
        result = (int(hours) + 12) * 60 + int(minutes)
        return result


def convert_duration_to_minutes(time: str) -> int:
    """
    Converts the duration to minutes.
    :param time: str of the duration time.
    :return: int calculated minutes.
    """
    return int(time.split(":")[0]) * 60 + int(time.split(":")[1])


def calculate_hours(time: int) -> int:
    hours = int(time / 60)
    while hours > 24:
        hours -= 24
    return hours


def calculate_minutes(time: int) -> int:
    return time - (int(time / 60) * 60)


def calculate_days(time: int) -> int:
    return int(int(time / 60) / 24)


def convert_to_twelve_format(time: int, day_week: str) -> str:
    converted_message = ""  # store the converted message.
    hours = calculate_hours(time)
    minutes = calculate_minutes(time)
    days = calculate_days(time)

    # refine the less 2 length minutes by adding 0.
    if len(str(minutes)) < 2:
        minutes_str = "0" + str(minutes)
    else:
        minutes_str = str(minutes)

    # check and decide how to represent the hours and AM or PM.
    if hours == 24:
        converted_message = str(hours - 12) + ":" + minutes_str + " AM"
    elif hours > 12:
        converted_message = str(hours - 12) + ":" + minutes_str + " PM"
    elif hours < 12:
        converted_message = str(hours) + ":" + minutes_str + " AM"
    elif hours == 12:
        converted_message = str(hours) + ":" + minutes_str + " PM"
    elif hours == 0:
        converted_message = str(hours) + ":" + minutes_str + " AM"

    # decide the day to appear in the message.
    if day_week is not None:
        if day_week.lower() in WEEK_DAYS:
            old = WEEK_DAYS.index(day_week.lower())
            current = old + days
            if current > len(WEEK_DAYS) - 1:
                current %= len(WEEK_DAYS)
            converted_message += ", " + WEEK_DAYS[current].title()
    # add to the message how many days moved.
    if days > 1:
        converted_message += " (" + str(days) + " days later)"
    elif days > 0:
        converted_message += " (next day)"

    return converted_message


def add_time(start: str, duration: str, day_week: str = None) -> str:
    st = convert_start_to_minutes(start)
    du = convert_duration_to_minutes(duration)
    added = st + du
    new_time = convert_to_twelve_format(added, day_week)
    return new_time
