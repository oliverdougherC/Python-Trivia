import random

EQues = ["What color is the sky? ", "How many states are in the US? ", "What is the atomic number for hydrogen? ", "Who was the first president of the USA? ", "Did Lee Harvey Oswald act alone? ", "What country did Russia invade in 2022? ", "Was 9/11 an inside job? ", "The American 1920's are typically refered to as the '_______ 20's' ", "The island prison of Alcatraz resides in the bay of which city? ", "Which country has the largest population in the world? "]
EAns = ["blue", "50", "1", "george washington", "no", "ukraine", "yes", "roaring", "san francisco", "china"]
MQues = ["In what year did the United States become an independent country? ", "Who invented the light bulb? ", "Who has the most home runs in MLB history? ", "What is 'I' in spanish? ", "What is the radius of a circle: x^2+y^2=16? ", "What compound are clouds made out of? (answer in molecular format) ", "What is the capital of Germany? ", "What year did WWI start? ", "What science is thermodynamics a branch of? ", "What unit of speed is used for nautical purposes? (answer in singular form) "]
MAns = ["1776", "thomas edison", "barry bonds", "yo", "4", "h2o", "berlin", "1914", "physics", "knot"]
HQues = ["If the velocity of an object remains at a constant 196.7 m/s, what is the magnetude of the net force acting on the object? ", "What is the last name of the man who assassinated James A. Garfield? ", "What was the first developed country to default? ", "How many types of ways can you shuffle a deck of cards? (Express your answer as a mathematical function) ", "How many times has France surrendered since 1900? ", "What year was JFK assassinated? ", "Which statement is true: 1) Forces exist in pairs, equal in magnetude and opposite in direction. 2) Torque is the cross product of force and the radius at which it is applied. ", "Who killed MLK Jr.? (Probably) ", "What is the greek letter that represents a friction coeffient? (Phyics) ", "True or False: Washington Mutuals neglect of mortgage bonds caused the 2008 housing crisis. "]
HAns = ["0", "guiteau", "greece", "52!", "1", "1963", "both", "james earl ray", "mu", "false"]
Ques = EQues + MQues + HQues
Ans =  EAns + MAns + HAns
ExtremeQues = ["What musical term is indicates a chord where the notes are played one after another rather than all together? ", "In which sport are barani, rudolph, and randolph all techniques? ", "What color does gold leaf appear if you hold it up to the light? ", "What is the capital city of Paraguay? ", "What is the family name of the ruling dynasty of Monaco? ", "Who collaborated with Karl Marx to produce 'The Communist Manifesto'? ", "In which branch of the arts is Katherine Dunham famous? ", "Which architect designed the Woolworth Building in New York City? ", "In which country is the Troi-Rivieres bridge? ", "Ken Thompson and Dennis Ritchie co-created which operating system? "]
ExtremeAns = ["arpeggio", "trampolining", "green", "asuncion", "grimaldi", "friedrich engels", "Ballet", "gilbert cass", "canada", "Unix"]

streak = 0
correct = True


def askTrivE ():
 if len(EQues) == 0:
    print ("No more questions left! Pick another difficulty.")
    bigd = input("What difficulty, (E)asy, (M)edium, (H)ard, (R)andom? ")
 else:
    r = random.randint(0, (len(EQues)-1))
 if (input(EQues[r])).lower() == EAns[r]:
    print ("Correct!")
    global streak
    streak = streak + 1
    print ("Streak: " + str(streak))
 else:
    print ("Incorrect!")
    print ("The correct answer was: " + EAns[r])
    global correct
    correct = False
    print ("Your streak was: " + str(streak))
    Rank()
 del EQues[r]
 del EAns[r]

def askTrivM ():
 if len(MQues) == 0:
    print ("No more questions left! Pick another difficulty.")
    bigd = input("What difficulty, (E)asy, (M)edium, (H)ard, (R)andom? ")
 else:
    r = random.randint(0, (len(HQues)-1))
 if (input(MQues[r])).lower() == MAns[r]:
    print ("Correct!")
    global streak
    streak = streak + 1
    print ("Streak: " + str(streak))
 else:
    print ("Incorrect!")
    print ("The correct answer was: " + MAns[r])
    global correct
    correct = False
    print ("Your streak was: " + str(streak))
    Rank()
 del MQues[r]
 del MAns[r]

def askTrivH ():
 if len(HQues) == 0:
    print ("No more questions left! Pick another difficulty.")
    bigd = input("What difficulty, (E)asy, (M)edium, (H)ard, (R)andom? ")
 else:
    r = random.randint(0, (len(HQues)-1))
 if (input(HQues[r])).lower() == HAns[r]:
    print ("Correct!")
    global streak
    streak = streak + 1
    print ("Streak: " + str(streak))
 else:
    print ("Incorrect!")
    print ("The correct answer was: " + HAns[r])
    global correct
    correct = False
    print ("Your streak was: " + str(streak))
    Rank()
 del HQues[r]
 del HAns[r]

def askTrivR ():
 r = random.randint(0, (len(Ques)-1))
 if (input(Ques[r])).lower() == Ans[r]:
    print ("Correct!")
    global streak
    streak = streak + 1
    print ("Streak: " + str(streak))
 else:
    print ("Incorrect!")
    print ("The correct answer was: " + Ans[r])
    global correct
    correct = False
    print ("Your streak was: " + str(streak))
    Rank()
 del Ques[r]
 del Ans[r]

def askTrivExtreme ():
   r = random.randint(0, (len(ExtremeQues)-1))
   if (input(ExtremeQues[r])).lower() == ExtremeAns[r]:
      print ("Correct!")
      global streak
      streak = streak + 1
      print ("Streak: " + str(streak))
   else:
      print ("Incorrect!")
      print ("The correct answer was: " + ExtremeAns[r])
      global correct
      correct = False
      print ("Your streak was: " + str(streak))
      RankE()
   del ExtremeQues[r]
   del ExtremeAns[r]

def askTriv (diff):
 diff = diff.lower()
 if diff == "e":
    if len(EQues) == 0:
       print ("No more questions left! Pick another difficulty.")
       bigd = input("What difficulty, (E)asy, (M)edium, (H)ard, (R)andom? ")
    else: 
       askTrivE()
 if diff == "m":
    if len(MQues) == 0:
       print ("No more questions left! Pick another difficulty.")
       bigd = input("What difficulty, (E)asy, (M)edium, (H)ard, (R)andom? ")
    else: 
       askTrivM()
 if diff == "h":
    if len(HQues) == 0:
       print ("No more questions left! Pick another difficulty.")
       bigd = input("What difficulty, (E)asy, (M)edium, (H)ard, (R)andom? ")
    else: 
       askTrivH()
 if diff == "r":
    if len(Ques) == 0:
       print ("No more questions left!")
       global correct 
       correct = False
    else: 
       askTrivR()
 if diff == "x":
      if len(ExtremeQues) == 0:
         print ("No more questions left!")
         bigd = input("What difficulty, (E)asy, (M)edium, (H)ard, (R)andom? ")
      else: 
         askTrivExtreme()

def Rank ():
      global streak
      if streak == 0:
         print ("Rank: Disgrace to your family")
      if streak <= 5 and streak > 0:
         print ("Rank: Idiot")
      if streak <= 10 and streak > 5:
         print ("Rank: Eh")
      if streak <= 15 and streak > 10:
         print ("Rank: Mediocre")
      if streak <= 20 and streak > 15:
         print ("Rank: Decent")
      if streak <= 25 and streak > 20:
         print ("Rank: Solid")
      if streak <= 30 and streak > 25:
         print ("Rank: Good")
      if streak <= 35 and streak > 30:
         print ("Rank: Great")
      if streak <= 40 and streak > 35:
         print ("Rank: Jeapordy Contestant")
      if streak <= 45 and streak > 40:
         print ("Rank: Certified Genius")
      if streak > 45:
         print ("Rank: Diety of Trivia")

def RankE ():
      global streak
      if streak == 0:
         print ("Rank: Youll get em next time")
      if streak <= 5 and streak > 0:
         print ("Rank: Solid")
      if streak <= 10 and streak > 5:
         print ("Rank: Good")
      if streak <= 15 and streak > 10:
         print ("Rank: Really Good")
      if streak <= 20 and streak > 15:
         print ("Rank: Great")
      if streak <= 25 and streak > 20:
         print ("Rank: Amazing")
      if streak <= 30 and streak > 25:
         print ("Rank: You should seriously go on Jeapordy")
      if streak <= 35 and streak > 30:
         print ("Rank: Be honest, did you google these?")
      if streak <= 40 and streak > 35:
         print ("Rank: Did you write these questions?")
      if streak <= 45 and streak > 40:
         print ("Rank: Pope of Trivianity")
      if streak > 45:
         print ("Rank: Vengeful Sun God of Trivia")


bigd = input("What difficulty, (E)asy, (M)edium, (H)ard, or (R)andom? ")

while correct == True:
 askTriv(bigd)