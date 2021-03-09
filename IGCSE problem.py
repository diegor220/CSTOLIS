#IGCSE problem
#Diego Rodríguez & Dom dom

options= {"A":{1:0,
               2:0,
               3:0,
               4:0,
               5:0},
         "B":{1:0,
               2:0,
               3:0,
               4:0,
               5:0},
         "C":{1:0,
               2:0,
               3:0,
               4:0,
               5:0},
         "D":{1:0,
               2:0,
               3:0,
               4:0,
               5:0},
         "E":{1:0,
               2:0,
               3:0,
               4:0,
               5:0}}

student_dict={}
admin={}
check=False
while not check:
    student_id=(input(" Enter your identification number: "))
    try :
        student_id=int(student_id)
        check=True
    except:
        print("please use a number")
        
if 0<student_id<150:
    student_dict[student_id]=[0,0,0,0,0]
elif student_id<0 or student_id>150:
    print ("please use correct id")
    student_id=(input(" Enter your identification number: "))
    

print (""" You will be presented several options, for each option, assign a value depending on how interested you are.

1 means you strongly agree and 5 means you strongly disagree""")

print (" Option A: Start at 8:00- Finish at 15:00 ")
answer=int(input("""How much do you agree with this schedule?
"""))

if 1>answer or answer>5:
    print ("Error: please choose a real option")
    print (" Option A: Start at 8:00- Finish at 15:00 ")
    answer=int(input("""How much do you agree with this schedule?
"""))
 
#if answer == 5:
 #   options["A"][5]=+1
#print(options)

options ["A"][answer]=+1
print (options)

