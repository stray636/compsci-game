import random

# this is the name
userName = input("Please enter your name: ")
print("this is a stupid assignment and I hate the teacher")

play = str(input("would you like to play? yes or no:  ")).capitalize()   #asking if they want to play

wallet = int(input("How much money will you gamble with today?  "))
print("wallet  ",wallet)
print("")


while play != "No":     #game running as long as they say yes
  bet = int(input("how much would you like to wager?    "))
  input("hit enter to roll")    #asking them to roll/start the game
  print("")
  dice1 = random.randint(1,6)  #rolling my dice
  dice2 = random.randint(1,6)
  total = dice1 + dice2
  print(dice1,dice2,"total",total)   #
  if total == 7:
    print("win!")
    wallet = wallet + bet
  elif(total == 11):
    wallet = wallet + bet
    print ("win!")  
  elif(total == 2):
    print ("lose")
    wallet = wallet - bet
  elif(total == 3):
    print ("lose")
    wallet = wallet - bet
  elif(total == 12):
    print ("lose")
    wallet = wallet - bet
  else:
    play2 = total   #setting target variable
    loop = 0     #reseting my loop variable
    print ("Your target is:  ", play2)
    while loop < 1:   # game running intill or target
      input("hit enter to roll")
      dice1 = random.randint(1,6)
      dice2 = random.randint(1,6)
      total = dice1 + dice2
      print(dice1,dice2,"total",total)
      if total == play2:
        wallet = wallet + bet
        print ("win!")
        loop = 1
      elif (total == 7):
        wallet = wallet - bet
        print ("lose!")
        loop = 1
  print("wallet", wallet)
  play = str(input("would you like to keep playing?    ")).capitalize()

print ("goodbye")




#add - a bet vs how much in wallet calculator, a "you are broke" game stop, a win vs loss calculator that either laughs at you or congradulates you, 
