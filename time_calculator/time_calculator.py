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


def add_time(start, duration):
    print(convert_start_to_minutes(start))




    # return new_time
add_time("3:30 PM", "2:12")