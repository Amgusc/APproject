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


# happiness is 1-100, hunger is a boolean, fatigue is 1-50, does it need to play is 1-10, does it need to use the bathroom is boolean, anger is 1-10

#Animal Stats start of game
Animal_stats = {'happiness' : 50,
          'hunger' : False,
          'fatigue' : 5,
          'play' : 5,
          'bathroom' : False,
          'anger' : 2,
          'dogAlive' : True,
          'days' : 1}

Options = {'optionA' : 'A',
           'optionB' : 'B',
           'optionC' : 'C',
           'optionD' : 'D',
           'optionX' : 'X',
           }


#print((Animal_stats['happiness']))
#if (Animal_stats['days']) is even:

while (Animal_stats['dogAlive']):
          print('Hello, today is day', (Animal_stats['days']))
          print('Happiness Level is: ', (Animal_stats['happiness']))
          print('Hunger is: ', (Animal_stats['hunger']))
          print('Fatigue Level is: ', (Animal_stats['fatigue']))
          print('Need to Play Level is: ', (Animal_stats['play']))
          print('Need for the Bathroom is: ', (Animal_stats['bathroom']))
          print('Anger Level is: ', (Animal_stats['anger']))
          dailyTask = input('''What would you like to do with your dog today?
                            
                            A: Play
                            B: Nap
                            C: Bathroom
                            D: Feed
                           
                            input letter of your choice:
                            ''')
                            
                            
          if dailyTask == (Options['optionA']):
            print('You played with your dog!')
            (Animal_stats['play']) -= 1
            (Animal_stats['fatigue']) += 5
          elif dailyTask == (Options['optionB']):
            print('Your dog took a nap!')
            (Animal_stats['fatigue']) -= 5
            (Animal_stats['play']) += 1
          elif dailyTask == (Options['optionC']):
            print('Your dog has relieved itself!')
            (Animal_stats['bathroom']) = False
            (Animal_stats['anger']) -= 1
          elif dailyTask == (Options['optionD']):
            print('You have fed your dog!')
            (Animal_stats['hunger']) = False
          else:
            print('Game Over! your dog died stupidhead')
            break
          (Animal_stats['days']) = (Animal_stats['days']) + 1
            
if (Animal_stats['fatigue']) > 40 and (Animal_stats['bathroom']) == True and (Animal_stats['hunger']) == True:
     (Animal_stats['anger']) = (Animal_stats['anger']) + 1
else:
     (Animal_stats['happiness']) = (Animal_stats['hunger'])
     (Animal_stats['hunger']) = (Animal_stats['hunger']) 

            

#def is_dog_alive(Animal_stats):
#          if current_happy < 10 and current_fatigue > 40 and current_anger > 8:
#                    dogAlive = False
#          else:
#            (Animal_stats[dogAlive]) = True
#          return (Animal_stats[dogAlive])

# What would you like to do today? Input the letter to do the action

# Dog: happiness(x) Hunger(x)  Hygiene(x) Ect. (the x is in place for the level of that variable)

# A: play
# B: Take a nap
# C: shower
# D: feed dog
# X: quit game 