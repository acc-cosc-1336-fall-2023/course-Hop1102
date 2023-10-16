#
def calculate_time(seconds_since_1970):
    hours = (seconds_since_1970 // 3600) % 24
    minutes = (seconds_since_1970 // 60) % 60
    seconds = seconds_since_1970 % 60
    return hours, minutes, seconds 