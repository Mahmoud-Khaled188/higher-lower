from art import logo
from art import vs
from game_data import data
import random
from replit import clear
def compare(A,B,choice,score):
  
  if A['follower_count']>B['follower_count']:
    if choice=='a':
      
      print(f"you're right. your score is {score}")  
      return A    
    else:
        score-=1
        print(f"you're wrong. your score is {score}")
        return False
  elif A['follower_count']<B['follower_count']:
    if choice=='b':
        
        print(f"you're right. your score is {score}")
        return B
    else:
        score-=1
        print(f"you're wrong. your score is {score}")
        return False

def account(A):
    B=random.choice(data)
    while A==B:
      B=random.choice(data)
      if A !=B:
        break
    return B


        



def game():
  print(logo)
  score=0
  A=random.choice(data)
  cont=True
  while cont==True:
    
    B=account(A) 
    print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
    print(vs)
    print(f"compare B:{B['name']}, {B['description']}, {B['country']}")
    choice=input("Who has more followers? Type 'A' or 'B' ").lower()
    score+=1
    clear()
    print(logo)
    A=compare(A, B, choice,score)
    if A==False:
      break
    
game()