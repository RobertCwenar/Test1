# Write a short game where you have 5 moves each way to the Chamber of Secrets.
# Every time you have chance find box or nothing. 
# You have a box, and the color of the box determines its frequency:
# green - 60%
# orange - 25%
# purple - 10%
# gold - 4%
# diamond -1%

# Assume you have a 40% chance of nothing and a 60% chance of something else.
# Gold from different boxes:
# green - 1000
# orange - 3000
# purple - 7000
# gold -14000
# diamond - 25000

# Remeber about:
#1) Clear code 
#2) Define good variables 
#3) Write program in english language

import random
from enum import Enum 

def find_approximate_value(value):
    lowest_value = int(value - 0.1 * value)
    highest_value = int(value + 0.1 * value)
    return random.randint(lowest_value, highest_value)

event = Enum('Event', ['Chest', 'Empty'])
lose_chance = {event.Chest: 0.6,
            event.Empty: 0.4}



available_boxes = Enum ('Colors',{'green': 'zielony', 
                'orange': 'pomarańczowy', 
                'purple': 'purpurowy', 
                'gold': 'złoty', 
                'diamond': 'diamentowy'
})


colours_dictionary = {available_boxes.green: 0.6,
                     available_boxes.orange: 0.25,
                     available_boxes.purple: 0.10,
                     available_boxes.gold: 0.04,
                     available_boxes.diamond: 0.01
                     }

rewards_for_chests = {available_boxes.green: 1000,
                     available_boxes.orange: 3000,
                     available_boxes.purple: 7000,
                     available_boxes.gold: 14000,
                     available_boxes.diamond: 25000
                     }



event_list = tuple(lose_chance.keys())
event_probability = tuple(lose_chance.values())

game_length = 5
gold_acquired = 0


print("Welcome to my game!")
print("---SECRETS BOXES ---")
print("You have only 5 moved to find a gold from boxes. ")

while game_length > 0:
    gamer_answer = input("Do you want to continue? y/n: ").lower()
    if gamer_answer != 'y':
        print("Game stopped!")
        break
    
    drawn_event = random.choices(event_list, event_probability)[0]
    if drawn_event == event.Chest:
        print("You have  drawn a Chest")
        drawn_colour = random.choices(list(colours_dictionary.keys()), list(colours_dictionary.values()))[0]
        print(f"The chest color is {drawn_colour.value}")
        gamer_rewards = find_approximate_value(rewards_for_chests[drawn_colour])
        gold_acquired_from_box = gamer_rewards
        gold_acquired = gamer_rewards + gold_acquired
        print(f"Congratulations you draw {drawn_colour.value} and we add {gold_acquired_from_box} to your wallet.")
    elif drawn_event == event.Empty:
        print("You have drawn nothing/ You are unlucky guy")
    
    game_length = game_length - 1 


print(f"Congratulations, you have acquried {gold_acquired} gold.")
