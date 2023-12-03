import random

def play():
        count1=0
        count2=0
        count3=0
        count4=0
        for i in range(1,100):
                print(f"Your {i} Chance")
                user=input("please select your choice??  For Sissors (S) , For Rock (R)  OR For Paper(P):")
                computer=random.choice(['r','s','p'])
                if user==computer:
                    count1+=1
                    print(f"Your {count1} times Equal to the Computer  ")
                    if count1==3:
                        return("Match Was Tie!!")
                if  win_match(user,computer):
                    count2+=1
                    print(f"You GOt the Score  {count2} ")
                    if count2==3:
                        print("Hey Hey!! Congradulations. You Won the Match")
                        if count4 <=5:
                            return("Your  [A] Grade Winner")
                        elif count4<=8:
                            return("Your [B] Grade Winner")
                        else:
                            return("Your [C] Grade Winner....Your Win is Amost Equal to Lose ")
                elif win_match(computer,user):
                    count3+=1
                    print(f"Computer Got Score  {count3}")
                    if count3==3:

                        return("oops!! Computer Won the Match")

                count4+=1

         
def win_match(player, opponent):
    #r>s ,s>p,p>r
    if (player=="r" and opponent=="s") or (player=="s" and opponent=="p") \
        or (player=="p" and opponent=="r"):
        return True   

print(play())
