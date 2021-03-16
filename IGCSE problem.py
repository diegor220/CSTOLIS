#IGCSE problem 2.0
#Diego Rodríguez

student_votes= {"A":{1:0,2:0,3:0,4:0,5:0},
                "B":{1:0,2:0,3:0,4:0,5:0},
                "C":{1:0,2:0,3:0,4:0,5:0},
                "D":{1:0,2:0,3:0,4:0,5:0},
                "E":{1:0,2:0,3:0,4:0,5:0}}

admin_votes= {"A":{1:0,2:0,3:0,4:0,5:0},
            "B":{1:0,2:0,3:0,4:0,5:0},
            "C":{1:0,2:0,3:0,4:0,5:0},
            "D":{1:0,2:0,3:0,4:0,5:0},
            "E":{1:0,2:0,3:0,4:0,5:0}}


total_votes= {"A":{1:0,2:0,3:0,4:0,5:0},
            "B":{1:0,2:0,3:0,4:0,5:0},
            "C":{1:0,2:0,3:0,4:0,5:0},
            "D":{1:0,2:0,3:0,4:0,5:0},
            "E":{1:0,2:0,3:0,4:0,5:0}}

student_dict={}
admin_dict={}

def survey ():
    global student_votes
    global admin_votes
    global student_dict
    global admin_dict
    global total_votes
    check=False
    while not check:
        school_id=(input(" Enter your identification number: "))
        try :
            school_id=int(school_id)
            check=True
        except:
            print("please use a number")

    student=False
    admin=False

    while school_id in student_dict or school_id in admin_dict:
        print ("This id has already been used")
        school_id=int(input("Enter your identification number: "))

    if 1<=school_id<=150:
        student_dict[school_id]=[0,0,0,0,0]
        student=True
    elif 151<=school_id<=170:
        admin_dict[school_id]=[0,0,0,0,0]
        admin=True
    if school_id<=0 or school_id>=171 :
        print ("please use correct id")
        school_id=int(input(" Enter your identification number: "))


    #Explanation of survey
    print (""" You will be presented several options, for each option, assign a value depending on how interested you are.

    1 means you strongly agree and 5 means you strongly disagree""")

    #Question 1
    print (" Option A: Start at 8:00- Finish at 15:00 ")
    answer=int(input("""How much do you agree with this schedule?
    """))

    while 1>answer or answer>5:
        print ("Error: please choose a real option")
        print (" Option A: Start at 8:00- Finish at 15:00 ")
        answer=int(input("""How much do you agree with this schedule?
    """))

    if student:
        student_votes ["A"][answer]=+1
        total_votes ["A"][answer]=+1
        (student_dict [school_id][0])= answer
    if admin:
        admin_votes ["A"][answer]=+1
        total_votes ["A"][answer]=+1
        (admin_dict [school_id][0])=answer
        
    #Question 2 
    print (" Option B: Start at 8:20- Finish at 15:20 ")
    answer=int(input("""How much do you agree with this schedule?
    """))

    while 1>answer or answer>5:
        print ("Error: please choose a real option")
        print (" Option B: Start at 8:20- Finish at 15:20 ")
        answer=int(input("""How much do you agree with this schedule?
    """))

    if student:
        student_votes ["B"][answer]=+1
        total_votes ["B"][answer]=+1
        (student_dict [school_id][1])= answer
    if admin:
        admin_votes ["B"][answer]=+1
        total_votes ["B"][answer]=+1
        (admin_dict [school_id][1])=answer

    #Question 3
    print (" Option C: Start at 8:40- Finish at 15:40 ")
    answer=int(input("""How much do you agree with this schedule?
    """))

    while 1>answer or answer>5:
        print ("Error: please choose a real option")
        print (" Option C: Start at 8:40- Finish at 15:40 ")
        answer=int(input("""How much do you agree with this schedule?
    """))

    if student:
        student_votes ["C"][answer]=+1
        total_votes ["C"][answer]=+1
        (student_dict [school_id][2])= answer
    if admin:
        admin_votes ["C"][answer]=+1
        total_votes ["C"][answer]=+1
        (admin_dict [school_id][2])=answer

    #Question 4
    print (" Option D: Start at 9:00- Finish at 16:00 ")
    answer=int(input("""How much do you agree with this schedule?
    """))

    while 1>answer or answer>5:
        print ("Error: please choose a real option")
        print (" Option D: Start at 9:00- Finish at 16:00 ")
        answer=int(input("""How much do you agree with this schedule?
    """))

    if student:
        student_votes ["D"][answer]=+1
        total_votes ["D"][answer]=+1
        (student_dict [school_id][3])= answer
    if admin:
        admin_votes ["D"][answer]=+1
        total_votes ["D"][answer]=+1
        (admin_dict [school_id][3])=answer

    #Question 5
    print (" Option E: Start at 9:20- Finish at 16:20 ")
    answer=int(input("""How much do you agree with this schedule?
    """))

    while 1>answer or answer>5:
        print ("Error: please choose a real option")
        print (" Option E: Start at 9:20- Finish at 16:20 ")
        answer=int(input("""How much do you agree with this schedule?
    """))

    if student:
        student_votes ["E"][answer]=+1
        total_votes ["E"][answer]=+1
        (student_dict [school_id][4])= answer
    if admin:
        admin_votes ["E"][answer]=+1
        total_votes ["E"][answer]=+1
        (admin_dict [school_id][4])=answer
    print("Thanks for taking the survey")
    print("""

    



""")
    status = 2
    if student:
        status=1
    if admin:
        status=0
    final_list=[status,school_id]
    return final_list
retvalues=survey()

redo=input("""Press 1 to submit another response
Press 2 to see the results
Press 3 to stop

""")

if redo==("1"):
     survey()
elif redo==("2"):
    if retvalues[0]==1:
        print ("Your results: ",student_dict [retvalues[1]])
    elif retvalues[0]==0:
        print ("Your results: ",admin_dict [retvalues[1]])
    print(f"""


Students:
Option A: {student_votes["A"]}
Option B: {student_votes["B"]}
Option C: {student_votes["C"]}
Option D: {student_votes["D"]}
Option E: {student_votes["E"]}

Staff:
Option A: {admin_votes["A"]}
Option B: {admin_votes["B"]}
Option C: {admin_votes["C"]}
Option D: {admin_votes["D"]}
Option E: {admin_votes["E"]}

Total:
Option A: {total_votes["A"]}
Option B: {total_votes["B"]}
Option C: {total_votes["C"]}
Option D: {total_votes["D"]}
Option E: {total_votes["E"]}

""")

elif redo==("3"):
    print ("")
else :
    print ("please use 1,2 or 3")
        
