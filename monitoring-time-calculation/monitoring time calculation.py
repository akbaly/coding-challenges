import datetime

# Enter the original film duration in hours and minutes (e.g., 3 hours 18 minutes as 3.18)
original_duration = "4.05"

# Set the desired playback speed
playback_speed = 2

# Split the original duration into hours and minutes
original_hours, original_minutes = map(int, original_duration.split('.'))

# Calculate the original duration in minutes
original_duration_min = original_hours * 60 + original_minutes

# Calculate the playback duration
playback_duration_min = original_duration_min / playback_speed

# Get the current time
now = datetime.datetime.now()

# Calculate the actual end time
actual_end_time = now + datetime.timedelta(minutes=playback_duration_min)

# Calculate the remaining time
remaining_time = actual_end_time - now

# Split the remaining time into hours and minutes
remaining_hours = remaining_time.seconds // 3600
remaining_minutes = (remaining_time.seconds // 60) % 60

# Print the results
print("Actual remaining time: {} hours {} minutes".format(remaining_hours, remaining_minutes))
print("Actual end time: {}".format(actual_end_time))

