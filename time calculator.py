#dont forget to add the optional argument later!
def add_time(start,duration):
    
    start = start.split(" ")
    tod = str(start[1]).upper()
    startlst = start[0].split(":")
    start_hour = int(startlst[0])
    start_min = int(startlst[1])
    
    
    duration = duration.split(":")
    duration_hours = int(duration[0])
    duration_mins = int(duration[1])
    

    
    day_count = 0
    hr_count = 0
    hrs = 0
    mins = 0
    min_count = 0
    
    
    #if duration_hours == 0 and start_hour < 12 : return f"Time now is  {start_hour}:{start_min + duration_mins}"
    
    if duration_hours == 0: 
        hrs = start_hour
    else:
        for hour in range(duration_hours):
            hr_count = hr_count + 1
            if hrs == 0:
                hrs = start_hour +1
            else:
                hrs = hrs + 1
                if hrs == 12:
                    if tod == "PM":       #if its 12 PM
                        tod = "AM"        #make it 12 AM
                        day = "Next day"  # move on to the next day 
                    elif tod =="AM":      # if its 12 AM  
                        tod = "PM"        #switch it to PM
                    print(hrs,tod)
                if hrs > 12:
                    hrs = hrs - 12     # if hours is 13 or higher  , take 12 out of it
            if hr_count == 24:
                day_count = day_count + 1
                hr_count = 0
             
            
    if duration_mins == 0 :
        mins = start_min
    else:
        for minute in range(duration_mins):
            min_count = min_count + 1
            if mins == 0:
                mins = start_min + 1
            elif mins > 59 :
                hrs = hrs + 1
                mins = mins - 59
                if hrs > 11:
                    if tod == "AM" : 
                        tod = "PM"
                    else :
                        tod = "AM"
            else:
                mins = mins + 1
            if min_count == 60 :
                hr_count = hr_count + 1
                min_count = 0
    #need to do somthine about the pm and am
                
    day = f"{day_count} days later"
                
    
        
        
    if len(str(mins)) == 1 : mins = "0" + str(mins)
    
    
    if day_count > 0:
        return f"Time now is {hrs}:{mins} {tod} ({day})"
    else:
        return f"Time now is {hrs}:{mins} {tod}"
        
        
    
print(add_time("11:43 PM", "24:20"))

times = [("3:00 PM", "3:10"),("11:30 AM", "2:32"),("11:43 AM", "00:20"),("10:10 PM", "3:30"),("11:43 PM", "24:20"),("6:30 PM", "205:12")]

