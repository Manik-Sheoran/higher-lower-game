import random

from art import logo, vs
from data import dataset
from replit import clear

score = 0
ans = True
a = random.choice(dataset)
while(ans == True):
  print(logo)
  b = random.choice(dataset)
  if a==b:
    b = random.choice(dataset)
  
  aname = a["name"]
  adisc = a['description']
  acountry = a['country']
  afollower= a['follower_count']
  
  bname = b["name"]
  bdisc = b['description']
  bcountry = b['country']
  bfollower= b['follower_count']
  
  print(f"A: {aname}, {adisc}, from {acountry}")
  print(vs)
  print(f"B: {bname}, {bdisc}, from {bcountry}")
  
  cans = 'a' if afollower > bfollower else 'b' 
  ans = input("Who has more followers A or B: ").lower()

  if(ans == cans):
    ans = True
    score+=1
    clear()
    a=b

print(f"your score is {score}")

