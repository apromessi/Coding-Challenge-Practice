def time_converter(time_in):
    time = time_in.split(":")
    if time[2][2:] == "PM" and int(time[0]) < 12:
        hours = int(time[0]) + 12
        if hours < 24:
            time[0] = str(hours)
    if time[2][2:] == "AM" and int(time[0]) == 12:
        time[0] = "00"
    time[2] = time[2][:2]
    time_out = ":".join(time)
    print time_out

time_in = raw_input()
time_converter(time_in)