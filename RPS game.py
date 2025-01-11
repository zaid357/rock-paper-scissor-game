import random
choices = ('r', 'p', 's')

while True:
 user_choice = input('Rock, Paper, Scissors? (r/p/s): ').lower()

 if user_choice not in choices:
   print('Invalid choice')
 computer_choice = random.choice(choices)
 print(f'you chose {user_choice}')
 print(f'computer chose {computer_choice}')

 if user_choice == computer_choice:
   print("match tie")

 elif (
       (user_choice == 'r' and computer_choice == 's') or
       (user_choice == 's' and computer_choice == 'p') or
       (user_choice == 'p' and computer_choice == 'r')):
       print("you win")
 else:
       print("you lose")

 should_continue = input('Do you want play again? (y/n): ').lower()
 if should_continue == 'n':
   break