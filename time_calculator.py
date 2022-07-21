def add_time(start, duration, day=None):
  week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
  day_index = 0
  
  if day:
    count = 0
    
    for index in range(len(week)):
      if week[index] == day.lower():
        day_index = count
      else:
        count += 1
  
  day_count_str = ""
  total_hour_str = ""
  total_minutes_str = ""
  
  # split AM/PM
  clock_format = start.split(" ")[1]

  # split start
  start_split = start.split(" ")[0].split(':')
  start_split_hour = int(start_split[0])
  start_split_minutes = int(start_split[1])
  if clock_format == "PM":
    start_split_hour += 12

  # split duration
  duration_split = duration.split(':')
  duration_split_hour = int(duration_split[0])
  duration_split_minutes = int(duration_split[1])

  # convert start and duration to minutes
  total_start_minutes = (start_split_hour * 60) + start_split_minutes
  total_duration_minutes = (duration_split_hour * 60) + duration_split_minutes

  # calculate start + duration
  total = total_start_minutes + total_duration_minutes
  total_hour = total // 60
  total_minutes = total % 60

  # count day
  day_count = total_hour // 24
  
  if day_count == 1:
    day_count_str = "next day"
  elif day_count > 1:
    day_count_str = str(day_count) + " days later"

  # count day name
    day_index += day_count
    if day_index > 6:
      day_index = day_index % 6
    
  # calculate clock format
  total_hour = total_hour % 24
  if total_hour >= 12:
    if total_hour > 12:
      total_hour -= 12 
    clock_format = "PM"
  else:
    if total_hour == 0:
      total_hour = 12
    clock_format = "AM"
    
  # convert total_hour to str 
  total_hour_str = str(total_hour)

  # calculate minutes
  if total_minutes < 10:
    total_minutes_str = "0" + str(total_minutes)
  else:
    total_minutes_str = str(total_minutes)

  # convert to new time
  new_time = total_hour_str + ":" + total_minutes_str + " " + clock_format

  if day:
    new_time += ", " + week[day_index].capitalize()
  
  if day_count > 0:
    new_time += " " + "(" + day_count_str + ")"

  print(new_time)
  return new_time
