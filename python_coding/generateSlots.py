from datetime import datetime, timezone, timedelta
import pytz
import json
x = datetime.strptime("2023-12-15T03:30:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
start_time = "2023-12-15T03:30:00.000Z"
start_time = datetime.strptime("2023-12-15T03:30:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
end_time =  "2023-12-15T17:39:00.000Z"
end_time = datetime.strptime("2023-12-15T17:39:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
break_start_time = "15:00"
break_end_time = "17:00".split(":")
slot_duration = 30
dic = []

while start_time < end_time:
    # print(start_time.time().strftime("%H:%M"), "----------------")
    if start_time.time().strftime("%H:%M") == break_start_time:
        start_time = datetime(start_time.year, start_time.month, start_time.day, int(break_end_time[0]), int(break_end_time[1]))
    else:
        stop = start_time + timedelta(minutes = slot_duration)
        save_start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        save_stop_time = stop.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        dic.append({"start_time": save_start_time, "end_time": save_stop_time})
        start_time = stop
print(dic)
print(len(dic))