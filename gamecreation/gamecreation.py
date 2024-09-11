import random
whichgame=random.randint(1,2)

#gs=guessed  crt=correct   pre=predetermined   pw=password   no=numberof   ans=answer  tof=ture or false

if whichgame==1:

    print("task 1")
    print("First a wild monkey appears and you cannot pass until five fruits have been guessed!")
    state_task1=False #pass task1 or not
    all_fruit_pre=["banana","apple","orange","blueberry","strawberry"] #pre=predetermined
    while state_task1==False:
        all_fruit_gs=[] #gs=guess
        print("you will guess 5 different fruits")
        while len(all_fruit_gs)<5:
            all_fruit_gs.append(input("guess a fruit"))
        crt_fruit_gs=[] #crt=correct
        for fruit_gs in all_fruit_gs:
            for fruit_pre in all_fruit_pre:
                if fruit_gs==fruit_pre:
                    crt_fruit_gs.append(fruit_gs)
        if len(crt_fruit_gs)==0:
            print("all wrong")
        elif len(crt_fruit_gs)==5:
            print("all correct")
            state_task1=True
        else:
            print(crt_fruit_gs,"are correct")

    print("task 2")
    print("there is a hungry tiger, and the only way out is the nearest that needs you to cross a river. You need to input height; if too short ,drown and if too tall, too easily spotted and will be hunted down.")
    state_task2=False
    while state_task2==False:
        height=int(input("input a height in cm"))
        if height<=160:
            print("you drown")
        elif height>180:
            print("the tiger spots you too easily and you die.")
        else:
            print("you live")
            state_task2=True
    
    print("task 3")
    print("there is a door that requires a password to unlock- it is a series of four numbers. You have 10 chances to guess the password")
    state_task3=False
    no_chances_used=0
    pw_pre=str(1121) #pw=password
    while state_task3==False:
        no_crt_numbers=0 #no=number of
        if no_chances_used==10:
            print("wasted")
            break
        pw_gs=str(input("input 4 numbers"))
        for i in range(4):
            if pw_gs[i]==pw_pre[i]:
                no_crt_numbers+=1
        no_chances_used+=1
        if no_crt_numbers==4:
            print("correct")
            state_task3=True
        else:
            print(no_crt_numbers,"numbers are correct")

elif whichgame==2:
    print("python quiz")
    state_play=True
    while state_play==True:
        state_finish=False
        while state_finish==False:
            score_quiz=0
            list_of_incorrect=[]
# set, print, define a vareble, import random, .py, for loop

            for x in range(6):
                if x==0:
                    print("1.how to define a empty set called 'myset'")
                    print("A.myset={}  B.myset=set  C.myset=[]  D.myset=set()")
                    ans_q1=input("your answer is")
                    ans_q1.upper()
                    tof_q1=False
                    if ans_q1=="D":
                        score_quiz+=1
                        tof_q1=True
                if x==1:
                    print("2.how to output 'Helloworld'")
                    print("A.print 'Helloworld'  B.ourput(Helloworld)  C.print('Helloworld')  D.print(Helloworld)")
                    ans_q2=input("your answer is")
                    ans_q2.upper()
                    tof_q2=False
                    if ans_q2=="C":
                        score_quiz+=1
                        tof_q2=True
                if x==2:
                    print("3.how to define a varable called 'x' in int form and give it a value 5")
                    print("A.x=5  B.'x'=5  C.x==5  D.x='5'")
                    ans_q3=input("your answer is")
                    ans_q3.upper()
                    tof_q3=False
                    if ans_q3=="A":
                        score_quiz+=1
                        tof_q3=True
                if x==3:
                    print("4.how to import random module")
                    print("A.input random module   B.import random   C.import random module   D.input random")
                    ans_q4=input("your answer is")
                    ans_q4.upper()
                    tof_q4=False
                    if ans_q4=="B":
                        score_quiz+=1
                        tof_q4=True
                if x==4:
                    print("5.if you want to write a project with python, what should you add after the name of the file")
                    print("A..py   B.py  C..python   D.python")
                    ans_q5=input("your answer is")
                    ans_q5.upper()
                    tof_q5=False
                    if ans_q5=="A":
                        score_quiz+=1
                        tof_q5=True
                if x==5:
                    print("6.what can str also be treated")
                    print("A.int  B.set  C.list  D.loop")
                    ans_q6=input("your answer is")
                    ans_q6.upper()
                    tof_q6=False
                    if ans_q6=="C":
                        score_quiz+=1
                        tof_q6=True
            print("your score is",score_quiz)
            if score_quiz<4:
                print("there is still a long way for you to go before you can use python well")
            elif score_quiz<6:
                print("well-done!")
            else:
                print("Excellent!")
            if tof_q1==False:
                list_of_incorrect.append("1")
            if tof_q2==False:
                list_of_incorrect.append("2")
            if tof_q3==False:
                list_of_incorrect.append("3")
            if tof_q4==False:
                list_of_incorrect.append("4")
            if tof_q5==False:
                list_of_incorrect.append("5")
            if tof_q6==False:
                list_of_incorrect.append("6")
            print("questions you get wrong are",list_of_incorrect)
            state_finish=True
        ans_again=input("do you want to play again (yes or no)")
        ans_again.lower()
        if ans_again=="no":
            state_play=False
        
    