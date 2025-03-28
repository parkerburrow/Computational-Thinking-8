# Beginning: create variables
summer_points = 0
winter_points = 0


answer = input("on a trip would you rather A) go to the beach, or B) go to a mountain?")
if answer == "A":
        summer_points += 1
elif answer == "B":
        winter_points += 1


answer = input("Are you A) going to a pool, or B) going skiing?")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1


answer + input("on the weekend would you rather A) go ice skating, or B) go fishing")  
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1



answer + input("Are you A) like summer, or B) like winter?")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1



answer = input ("Are you A) a hot tub guy, or B) a cold plunge guy?")
if answer =="A" :
    winter_points += 1
elif answer == "B":
    summer_points += 1

 # End: determine results
if winter_points > summer_points:
    print("you are winter person")
elif summer_points > winter_points :
    print("you are summer person")
elif winter_points == summer_points:
    print("you like winter and summer the same") 