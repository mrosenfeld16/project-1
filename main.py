score = 50

health = 10

x = 0

if health <= 2:
  print('Your health is dangerously low. Get questions right to bring it back up!')

while x != 1:
  if score <= 0:
    print('Sorry, you lost, your score has dropped to 0 because you answered too many questions wrong')
    break
  x = 1

name = input('What is your name? \n')
ans = input('Hi ' + name + ', do you want to play an animal trivia game? Y or N? \n')

if ans == 'N':
  print('TOO BAD\n')

print('Your starting score is 50, your starting health is 10\n')

Q1 = input('Is a spider an insect? Y or N\n')
Q1 = Q1.upper()
if Q1 == "Y":
  print('Sorry, you are wrong. Your score is now 45 and health is now 9\n')
  score = 45
  health = 9  
elif Q1 ==  'N':
  print('Congratulations ' + name + ' you are correct. Your score is now 55, your health stays at 10\n')
  score = 55
  health = 10

Q2 = input('There is a type of immortal jellyfish. T or F.\n')
Q2 = Q2.upper()
if Q2 == 'T':
  score = score + 5
  if health < 10:
    health = health + 1
  print('Yay, you got it right! Your score is ' + str(score) + ' and your health is ' + str(health))
elif Q2 == 'F':
  score = score - 5
  health = health - 1
  print('Sorry, you are wrong. Your score is now ' + str(score) + 'and your health is ' + str(health))

print('\nNo need to answer on this one.\n Did you know that there is a type of worm with a growth on its back that looks suspiciously like a baby christmas tree? Google it. They are ADORABLE\n')

Q3 = input('The Giant Squid is larger than the Colossal Squid. T or F?')
Q3 = Q3.upper()
if Q3 == 'T':
  score = score - 5
  health = health - 1
  print("Sorry, you're wrong. Your score is now " + str(score) + " and your health is now " + str(health))
elif Q3 == 'F':
  score = score + 5
  if health < 10:
    health = health + 1
  print("Yay you got it right! Your score is now " + str(score) + ' and your health is ' + str(health))

Q4 = input('The most poisonous aquatic animal is the Luna Lionfish. T or F?')
Q4 = Q4.upper()
if Q4 == 'T':
  score = score - 5
  health = health - 1
  print('You are incorrect, the most venemous aquatic animal is the Sea Wasp Box Jellyfish. It has 0.5 million stinging cells on each tentacle, each cell killing theoretically up to 60 people.')
  print('Your score is now' + str(score) + 'and your health is now' + str(health))
if Q4 == 'F':
  score = score + 5
  health = health + 1
  print('Yay you got it right. The most venemous aquatic animal is the Sea Wasp Box Jellyfish. It has 0.5 million stinging cells on each tentacle, each cell killing theoretically up to 60 people.')
  print(' Your score is now ' + str(score) + ' and your health is now ' + str(health))