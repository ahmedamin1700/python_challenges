# convert start time to minutes. this need function due to 12 hours format.
# convert duration time to minutes.
# addition will be easier in minutes.
# convert the result to 12 hour format.

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


def calculate_hours(time):
    hours = int(time / 60)
    while hours > 24:
        hours -= 24
    return hours


def calculate_minutes(time):
    return time - (int(time / 60) * 60)


def calculate_days(time):
    return int(int(time / 60) / 24)


def convert_to_twelve_format(time: int) -> str:
    converted_message = ""
    hours = calculate_hours(time)
    minutes = calculate_minutes(time)
    days = calculate_days(time)

    if len(str(minutes)) < 2:
        minutes_str = "0" + str(minutes)
    else:
        minutes_str = str(minutes)

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

    if days > 1:
        converted_message += " (" + str(days) + " days later)"
    elif days > 0:
        converted_message += " (next day)"

    return converted_message


def add_time(start, duration):
    st = convert_start_to_minutes(start)
    du = convert_duration_to_minutes(duration)
    added = st + du
    new_time = convert_to_twelve_format(added)
    return new_time


# print(add_time("11:40 AM", "28:00"))
# add_time("3:30 PM", "2:12")