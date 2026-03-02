#DiceRoll.py
#Name: Nathan Heavican
#Date: 3/1/26
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
  #find the sum total of the two dice
    total = dice1 + dice2
    rolls[total - 2] = rolls[total - 2] + 1
  #print statictics for dice rolls
  dice = 2
  for count in rolls:
    percent = round((count / 10000) * 100, 1)
    print(f"{dice}: {count} {percent}%")
    dice = dice + 1

if __name__ == '__main__':
  main()
