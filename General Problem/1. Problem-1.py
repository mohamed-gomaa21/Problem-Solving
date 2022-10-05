
# Finished Solve Date : 16/08/2021
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile)
# and 1 mile at easy pace again, what time do I get home for breakfast?

start_time_hours = 6
start_time_minutes = 52

time_in_easy_pace_minutes = 8 * 60
time_in_easy_pace_second = 15
time_easy_pace = time_in_easy_pace_minutes + time_in_easy_pace_second   # total time in easy pace per second

time_in_tempo_minutes = 7 * 60
time_in_tempo_second = 12
time_tempo = time_in_tempo_second + time_in_tempo_minutes       # total time in tempo per second

total = (time_easy_pace * 2) + (time_tempo * 3)
total_min = total/60                                            # total time running per minutes

if total_min + start_time_minutes >= 60:
    x = (total_min + start_time_minutes) % 60
    start_time_minutes = x
    start_time_hours = start_time_hours+ 1

else :
    start_time_minutes = start_time_minutes + total_min

print(start_time_hours, ':', start_time_minutes)
