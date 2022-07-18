
def add_time(start,duration,dow=False):
    
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    #split and clean the data
    start = start.split(" ")
    tod = str(start[1]).upper()
    startlst = start[0].split(":")
    start_hour = int(startlst[0])
    start_min = int(startlst[1])
    
    duration = duration.split(":")
    duration_hours = int(duration[0])
    duration_mins = int(duration[1])
    
    #set initial values
    day_count = 0
    hr_count = 0
    hrs = 0
    mins = 0
    day = None

    #check the minutes value
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
    #keeping track of the total hours so we can cycle through TOD (AM,PM)            
    total_hours = start_hour + hrs


    #check the hours value
    if duration_hours == 0: 
        hrs = start_hour + hrs
    else:
        hrs = start_hour + hrs
        #the amount of hours will be determined first in the minutes loop, plus the actual start hour
        for hour in range(duration_hours):
            total_hours = total_hours + 1
            hr_count = hr_count + 1
            hrs = hrs + 1
            if hrs > 12:
                #if hours is 13 or higher,take 12 out of it to keep the hours in the 12 range
                hrs = hrs - 12
            #count the days   
            if hr_count == 24:
                day_count = day_count + 1
                hr_count = 0
            if tod == "PM" and hrs > 11 and day_count < 1:
                day_count = day_count + 1

    #check the final TOD result
    while True:
        if total_hours < 12: break
        if total_hours >= 12:
            if tod == "PM":
                tod = "AM"
                if total_hours < 24:
                    day = "next day"
            elif tod =="AM":      
                tod = "PM"
            total_hours = total_hours - 12
    
    #check the day input
    if not dow == False:
        dow = dow.capitalize()
        if dow in weekdays:
            #determine the position of the start day within the weekdays list
            dow_pos = weekdays.index(dow)
            #loop through the weekdays in order for the amount of days that pass
            for i in range(day_count):
                #start the loop from the current day onward!
                dow_pos = dow_pos + 1
                if dow_pos > 6:
                    dow_pos = 0
                    continue
                #if the index goes farther than the last day of the week, reset the index to the first day of the week [0] , then continue on.
            dow = weekdays[dow_pos]

    #fix the minutes string in the output
    if len(str(mins)) == 1 : mins = "0" + str(mins)
    
    #this next block will return the proper output depending whether the third argument(day) isn't given or not
    if dow is False:
        if day == "next day" and not day_count > 1:
            return f"{hrs}:{mins} {tod} ({day})"     
        if day_count > 1:
            day = f"{day_count} days later"
            return f"{hrs}:{mins} {tod} ({day})"
        else:
            return f"{hrs}:{mins} {tod}"
    else :
        #if the day hasnt been altered by any of the previous loops, give it the proper value
        if day != None:
            if day_count > 1:
                day = f"{day_count} days later"
                return f"{hrs}:{mins} {tod}, {dow} ({day})"
            if day == "next day":
                return f"{hrs}:{mins} {tod}, {dow} ({day})"    
        else:
            return f"{hrs}:{mins} {tod}, {dow}"
            
   
print(add_time("11:40 AM", "0:25"))

#set a bunch of possible cases!
times = [("3:00 PM", "3:10"),("11:30 AM", "2:32"),("11:43 AM", "00:20"),("10:10 PM", "3:30"),("11:43 PM", "24:20"),("6:30 PM", "205:12"),("8:16 PM", "466:02"),("11:59 PM","24:05"),("2:59 AM", "24:00", "saturDay"),("3:30 PM", "2:12", "Monday"),("11:40 AM", "0:25")]
