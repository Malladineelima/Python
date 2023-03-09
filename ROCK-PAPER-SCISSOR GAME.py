#rock,paper,scissors game
import random
arr=["rock","paper","scissor"]
c_score=0
u_score=0
for i in range(5):
    c_choice=random.randint(0,2)
    c_choice=arr[c_choice]
    u_choice=input("enter choice:").lower()
    if u_choice not in arr:
         print("invaid")
    if c_choice=="rock" and u_choice=="scissors":
        print("computer won")
        c_score+=1
    elif c_choice=="paper" and u_choice=="rock":
        print("computer won")
        c_score+=1
    elif c_choice=="scissors" and u_choice=="paper":
        print("computer won")
        c_score+=1
    elif c_choice==u_choice:
         print("draw match")
    else:
        print("user won")
        u_score+=1
    print(f"comp:{c_score},user:{u_score}")
if c_score> u_score:
    print("computer won")
elif u_score> c_score:
    print("user won")
elif c_score==u_score:
    print("draw match")
   
