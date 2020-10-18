# HackerRank Challenge.
# Ahmed Amin 18 / 10 / 2020.

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def time_conversion(s):
    time_array = s.split(':')
    if 'PM' in time_array[2]:
        if time_array[0] == '12':
            time_array[0] = '12'
        else:
            time_array[0] = str(int(time_array[0]) + 12)
        time_array[2] = time_array[2].replace('PM', '')
    else:
        if time_array[0] == '12':
            time_array[0] = '00'
        time_array[2] = time_array[2].replace('AM', '')
    return ':'.join(time_array)


print(time_conversion('07:05:45PM'))
print(time_conversion('12:01:00PM'))
print(time_conversion('12:01:00AM'))
