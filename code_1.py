# sqiggly line ~ means we did thatit was completed

# Import libraries random and time ~
# Welcome to virtual pet sim ~
# Make var name that takes user input for the pet’s name ~
# Make vars for the different things that the user will have to care for(happiness, hunger, fatigue, play, bathroom)~
# Make happiness from 1-100, choose a starting level~
# Make hunger a boolean, false to start~
# Make fatigue from 1-20, choose a starting level~
# Make play from 1-10, choose a starting level~
# Make bathroom a boolean, false to start~
# Display all these variables to the user along with instructions on how the game works so they have a jumping off point~
# Make an if statement that asks if hunger is false, if false make true, else leave as is
# Make fatigue increase by 5 each interval
# Make play increase by 1 each interval
# Make an if statement that asks if bathroom is false, if false make true, else leave as is
# Update the user on the new status of their pet
# Ex:
# print(‘Happiness is ‘, happiness, \n’Hunger is ‘, hunger, \n’Fatigue is ‘, fatigue, \n’Need   for play is ‘, play, \n’Need for using the grass is ‘, bathroom)
# Ask the user what they would like to do to improve their pet’s wellbeing, they can answer with a ‘y’ or ‘n’
# Ex:
# Response = input(‘Would you like to play with ‘, name, ‘?’, \n‘Would you like to take ‘, name, ‘ to use the grass?’)
# Make more vars to compare current hunger, bathroom and play levels with the ones before the user improved the wellbeing of their pet to affect fatigue and happiness levels
# If the user is playing with their pet too much then fatigue goes up
# If the user made hunger go down, fatigue/need to play go down and bathroom false then happiness goes up by 15

# The parentheses take in argunments, arguments are bascially variables that are going to be used in the function, there can be as many of these as you need
# def update_status(pls, fix, this):
#  return(pls fix this)
# return value is what comes out of the function
# after the function has been defined(aka everything above), you can give the arguments value for the function to use
# update_status(pls, fix, this)

# response = input('Would you like to play with your pet?)
# \n, 'Would you like to take ', name, ' to use the grass?')


# Virtual Dog
import time
import random

print('Welcome to Virtual Dog Simulator!')

# This takes the input for the name of the dog
petname = input ( 'Enter a Name for Your Dog: ')
print ('Some rules for this game: Your dog will experience several different feelings including, happiness, fatigue, hunger, need to play and need to relieve themselves. It is your job to keep your dog happy, not angry, not fatigued, well fed and played with. As the days progress you will get to pick one action to do every day. You must make careful descions to ensure that your dog is getting the proper care. Each day you get the choice to either let your dog play, rest, eat, or relieve themselves. For each descion you must input a CAPITAL LETTER.')
# This takes the input for the name of the dog

def dogname(petname):
                #defined function serves as a name holder
                return print("GAME OVER!!! your dog " + petname + " needs better care than that!!!")

# happiness is 1-100, hunger is a boolean, fatigue is 1-100, does it need to play is 1-100, does it need to use the bathroom is boolean

#Animal Stats start of game
Animal_stats = {'happiness' : 50,
          'hunger' : False,
          'fatigue' : 40,
          'play' : 60,
          'bathroom' : False,
          'dogAlive' : True,
          'days' : 1}

Options = {'optionA' : 'A',
           'optionB' : 'B',
           'optionC' : 'C',
           'optionD' : 'D',
           'optionI' : 'I',
           'optionX' : 'X',
           }


min = 0

max = 100

#main game loop
while (Animal_stats['dogAlive']):
          print('Hello, today is day', (Animal_stats['days']))
          print('Happiness Level is: ', (Animal_stats['happiness']),'/ 100')
          print('Hunger is: ', (Animal_stats['hunger']))
          print('Fatigue Level is: ', (Animal_stats['fatigue']),'/ 100')
          print('Need to Play Level is: ', (Animal_stats['play']),'/ 100')
          print('Need for the Bathroom is: ', (Animal_stats['bathroom']))


          
          dailyTask = input('''What would you like to do with your dog today?
                            
                            A: Play
                            B: Nap
                            C: Bathroom
                            D: Feed
                           
                            I: info/statistic 
                            # (nerd stuff)
                            input letter of your choice:
                            ''')
                            
                            
          if dailyTask == (Options['optionA']):
            print('You played with your dog!')
            (Animal_stats['play']) -= 10
            (Animal_stats['fatigue']) += 10
            (Animal_stats['happiness']) += 10
          elif dailyTask == (Options['optionB']):
            print('Your dog took a nap!')
            (Animal_stats['fatigue']) -= 10
            (Animal_stats['play']) += 10
          elif dailyTask == (Options['optionC']):
            print('Your dog has relieved itself!')
            (Animal_stats['bathroom']) = False
          elif dailyTask == (Options['optionD']):
            print('You have fed your dog!')
            (Animal_stats['hunger']) = False
          elif dailyTask == (Options['optionI']):
            print('Option A is for playing with the dog. When you play with your dog its need for play decreases, its fatigue increases and its happiness increases.')
            print('Option B is for letting your dog rest. When you let your dog rest its fatigue level decreases and its need for play increases.')
            print('Option C is for letting your dog relieve themseleves. When you let your dog relieve themselves theyre need for the bathroom decreases as well as their anger level')
            print('Option D is for feeding your dog. When you feed you dog its need for the bathroom becomes true and its hunger becomes false')
            print('Option X is to quit the game, this will just end the game')
            print('Option I is obviously for info')
          else:
             GameEnd = dogname(petname)
             break
          
          
          if (Animal_stats['happiness']) > 100:
              (Animal_stats['happiness']) = max
          elif (Animal_stats['happiness']) < 0:
            (Animal_stats['happiness']) = min
          else: 
            (Animal_stats['happiness']) = (Animal_stats['happiness'])

          if (Animal_stats['fatigue']) > 100:
              (Animal_stats['fatigue']) = max
          elif (Animal_stats['fatigue']) < 0:
            (Animal_stats['fatigue']) = min
          else: 
            (Animal_stats['fatigue']) = (Animal_stats['fatigue'])

          if (Animal_stats['play']) > 100:
            (Animal_stats['play']) = max
          elif (Animal_stats['play']) < 0:
            (Animal_stats['play']) = min
          else: 
            (Animal_stats['play']) = (Animal_stats['play'])     
          (Animal_stats['days']) = (Animal_stats['days']) + 1
          
          #Day bathroom cycle (I FIXED THiS or idk FINIHSED IT BUT THIS WORKS NOW)
          if (Animal_stats['fatigue']) > 75 and (Animal_stats['bathroom']) == True and (Animal_stats['hunger']) == True:
            (Animal_stats['happiness']) -= 10
          else:
            (Animal_stats['happiness']) = (Animal_stats['happiness'])
            (Animal_stats['hunger']) = (Animal_stats['hunger']) 

          dividend = (Animal_stats['days'])
          divisor = 2
          Divsum = dividend % divisor
          if Divsum == 1:
             (Animal_stats['hunger']) = True
             (Animal_stats['bathroom']) = True
          else:
            (Animal_stats['hunger']) = (Animal_stats['hunger'])
            (Animal_stats['bathroom']) = (Animal_stats['bathroom'])
          
          # yeah this code is redundant and messy, i just needed an excuse to use the dogAlive dictionary varibale because it is lowkey useless but whatevs
          if (Animal_stats['fatigue']) == 100 or (Animal_stats['play']) == 0:
            (Animal_stats['dogAlive']) = False

          if (Animal_stats['dogAlive']) == False:
            GameEnd = dogname(petname)
             




#def is_dog_alive(Animal_stats):
#          if current_happy < 10 and current_fatigue > 40 and current_anger > 8:
#                    dogAlive = False
#          else:
#            (Animal_stats[dogAlive]) = True
#          return (Animal_stats[dogAlive])

# What would you like to do today? Input the letter to do the action