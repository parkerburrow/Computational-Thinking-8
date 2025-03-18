###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("summer")

q1 = codesters.Square(100, 100, 200, 'blue')

q2 = codesters.Square(-100,100,200, 'red')

q3 = codesters.Square(-100, -100, 200, 'blue')

q4 = codesters.Square(100, -100, 200, 'red')

s1 = codesters.Sprite("football", 100, 100)

s1.set_size(0.09)

s2 = codesters.Sprite("cardinal", -100, -100)

s2.set_size(0.7)

s3 = codesters.Sprite("Winnie2", 100, -100)

s3.set_size(0.8)

s4 = codesters.Sprite("space needle", -100,100)

s4.set_size(0.6)

message1 = codesters. Text("Parker",0,220,"red")

message2 = codesters. Text("I like food",0,-220,"black")