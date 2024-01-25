import os
from datetime import timedelta
from datetime import date


def get_file(specific_day):
    path            = "People"
    network_list    = os.listdir(path)

    for per_person in network_list:
        file    = open(path+"/"+per_person,"r")
        content = file.readlines()
        
        for single_line in content:
            if(specific_day in single_line):
                print("file : "+(per_person)+" content : "+ str(single_line))

# t1 = datetime.date(year=2024,month=1,day=1)

# Get peoples from the main lists categories( ex : from A_list list_name="A_list.md")
def get_people_from_lists(list_name):
    a_list_file = open(list_name,"r")
    a_people       = a_list_file.readlines()
    while (True):
        try:
            a_people.remove("\n")
        except:
            break
    for count in range(len(a_people)):
        a_people[count] = a_people[count][:-1]
    
    return a_people




today = date.today() 
for d_days in range(15):
    # get the date 
    delta_days = timedelta(days=d_days)
    specific_day     = today - delta_days

    # format date YYYY-MM-DD -> [[YYYY.MM.DD]]
    s_specific_day = str(specific_day)
    s_specific_day_list = s_specific_day.split("-")
    s_specific_day = "[[" + s_specific_day_list[0]+"." + s_specific_day_list[1] + "." + s_specific_day_list[2] + "]]"


