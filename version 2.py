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

    #"11:30 AM", "2:32"
    if duration_mins == 0 :
        mins = start_min
    else:
        mins = start_min
        #the mins output should always start with the actual start minutes, then keep adding to it according to the duraton
        for minute in range(duration_mins):
            mins = mins + 1
            if mins > 59 :
                #if the minutes pass 60, subtract that number, then add an hour                    
                hrs = hrs + 1
                mins = mins - 60

    #next part (hours) nees work            
    if duration_hours == 0: 
        hrs = start_hour + hrs
    else:
        hrs = start_hour + hrs
        #the hours here is 12, the start hours is 11, then only added an extra hours vuz of the minutes.
        for hour in range(duration_hours):
            hr_count = hr_count + 1
            hrs = hrs + 1
            #need to move the tod manipulation outside of the hours loop (why)
            if hrs > 12:
                hrs = hrs - 12     # if hours is 13 or higher  , take 12 out of it
            if hr_count == 24:
                day_count = day_count + 1
                hr_count = 0
    #program is succesful until the pm and am portion
    #also need to work on the days count part           
    if hrs == 12:
        if tod == "PM":       #if its 12 PM
            tod = "AM"        #make it 12 AM
            day = "Next day"  # move on to the next day 
        elif tod =="AM":      # if its 12 AM  
            tod = "PM"        #switch it to PM
    
    #need to do somthine about the pm and am
                
    day = f"{day_count} days later"
                
    
        
        
    if len(str(mins)) == 1 : mins = "0" + str(mins)
    
    
    if day_count > 0:
        return f"Time now is {hrs}:{mins} {tod} ({day})"
    else:
        return f"Time now is {hrs}:{mins} {tod}"
        
        
    
print(add_time("6:30 PM", "205:12"))

times = [("3:00 PM", "3:10"),("11:30 AM", "2:32"),("11:43 AM", "00:20"),("10:10 PM", "3:30"),("11:43 PM", "24:20"),("6:30 PM", "205:12")]

