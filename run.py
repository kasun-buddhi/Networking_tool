import os
from datetime import timedelta
from datetime import date

#######################################################################################################################
#       Func List
#######################################################################################################################

def get_color(percentage):
    exelent_color = "#43f94a" 
    good_color    = "#43f9e1"
    ok_color      = "#f9bf43"
    bad_color     = "#ff3d3d"

    if(percentage < 25):
        return bad_color
    elif(percentage < 50):
        return ok_color
    elif(percentage < 75):
        return good_color
    else:
        return exelent_color

# Give True or false with date available on a specific person (ex : person="person_a", specific_day="[[2024.01.01]]")
def is_connect_with_specific_date(person,specific_day):
    is_connected    = False
    path            = "Networking/people"
    file            = open(path+"/"+person+".md","r")
    content         = file.readlines()
        
    for single_line in content:
        if(specific_day in single_line):
            is_connected = True
            break
    file.close()
    return is_connected
# t1 = datetime.date(year=2024,month=1,day=1)

# Get peoples from the main lists categories( ex : from A_list list_name="A_list.md")
# Will return string people list (ex: ["[[person_a]]", "[[person_b]]"])
def get_people_from_lists(list_name):
    a_list_file     = open("Networking/"+list_name,"r")
    a_people        = a_list_file.readlines()
    while (True):
        try:
            a_people.remove("\n")
        except:
            break
    for count in range(len(a_people)):
        if(a_people[count][-1:] == "\n"):
            a_people[count] = a_people[count][:-1]
    a_list_file.close()
    return a_people

# Append html code into daily dairy (ex : today="2024-01-01",html_code=str(code))
def put_html_on_daily_dairy(today,html_code):
    today_list          = str(today).split("-")
    today_file_format   = today_list[0]+"."+today_list[1]+"."+today_list[2]+".md"
    path                = "Diary/"+today_file_format
    file = open(path,"+a");
    file.write(html_code)
    file.close()

# html string maker 
def make_html_code(a_percentage,b_percentage,c_percentage,d_percentage):
    #type
    a_class_type = "progress"
    b_class_type = "progress"
    c_class_type = "progress"
    d_class_type = "progress"

    if(a_percentage < 50):
        a_class_type = "progress less"
    if(b_percentage < 50):
        b_class_type = "progress less"
    if(c_percentage < 50):
        c_class_type = "progress less"
    if(d_percentage < 50):
        d_class_type = "progress less"
    
    #colors
    a_color     = get_color(a_percentage)
    b_color     = get_color(b_percentage)
    c_color     = get_color(c_percentage)
    d_color     = get_color(d_percentage)
    
    code =  f"""<body>
        <div class="container">
            <div class="{a_class_type}" style="--i:{int(a_percentage)};--clr:{a_color}; font-size:9; '">
                <h3 style="top:35px">{int(a_percentage)}<span>%</span></h3>
                <h4 style="top:50px; font-size:16;">A</h4>
            </div>
            <div class="{b_class_type}" style="--i:{int(b_percentage)};--clr:{b_color}; font-size:9;">
                <h3 style="top:35px">{int(b_percentage)}<span>%</span></h3>
                <h4 style="top:50px; font-size:16;">B</h4>
            </div>
            <div class="{c_class_type}" style="--i:{int(c_percentage)};--clr:{c_color}; font-size:9;">
                <h3 style="top:35px">{int(c_percentage)}<span>%</span></h3>
                <h4 style="top:50px; font-size:16;"> C</h4>
            </div>
            <div class="{d_class_type}" style="--i:{int(d_percentage)};--clr:{d_color}; font-size:9;">
                <h3 style="top:35px">{int(d_percentage)}<span>%</span></h3>
                <h4 style="top:50px; font-size:16;"> D </h4>
            </div>
        </div>
    </body>
    """
    return code

#calculate percentage for a specific list (ex : people_list=A_list, days_counts=15, today=date.today())
def calculate_list_percentage(people_list,days_count,today):
    number_of_list_members  = len(people_list)
    contacted_list          = []
    contacted_count         = 0
    for d_days in range(days_count):

        #get the a dpecific date
        delta_days      = timedelta(days=d_days)
        specific_day    = today - delta_days

        #format date YYYY-MM-DD -> [[YYYY.MM.DD]]
        s_specific_day = str(specific_day)
        s_specific_day_list = s_specific_day.split("-")
        s_specific_day = "[[" + s_specific_day_list[0]+"." + s_specific_day_list[1] + "." + s_specific_day_list[2] + "]]"

        for person_index in range(len(people_list)):
            if(is_connect_with_specific_date(people_list[person_index][2:-2],s_specific_day)):
                if(not(people_list[person_index] in contacted_list)):
                    contacted_count += 1           
                    contacted_list.append(people_list[person_index])
    if(number_of_list_members != 0 ):
        percentage = contacted_count*100.0/number_of_list_members 
    else:
        percentage = 0.0
    return percentage


#######################################################################################################################
#       Main flow 
#######################################################################################################################

today = date.today() 
a_people_list = get_people_from_lists("A_list.md")
b_people_list = get_people_from_lists("B_list.md")
c_people_list = get_people_from_lists("C_list.md")
d_people_list = get_people_from_lists("D_list.md")

number_of_a_people = len(a_people_list)
number_of_b_people = len(b_people_list)
number_of_c_people = len(c_people_list)
number_of_d_people = len(d_people_list)

a_contact_count = 0
b_contact_count = 0
c_contact_count = 0
d_contact_count = 0

# put_html_on_daily_dairy(today=date(year=2024,month=1,day=1),html_code="<html>")
# print(make_html_code(23.3,39,13,44.9))

# print(calculate_list_percentage(a_people_list,15,today))

a_list_percentage = calculate_list_percentage(a_people_list,15,today)
b_list_percentage = calculate_list_percentage(b_people_list,15,today)
c_list_percentage = calculate_list_percentage(c_people_list,15,today)
d_list_percentage = calculate_list_percentage(d_people_list,15,today)

html_code = make_html_code(a_list_percentage,b_list_percentage,c_list_percentage,d_list_percentage)
put_html_on_daily_dairy(today,html_code)