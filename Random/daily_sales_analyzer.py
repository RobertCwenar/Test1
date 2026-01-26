# You simulate daily sales for a small shop.
# There are 3 product categories:
# food
# electronics  # type: ignore
# clothes
#
# Each category has:
## probability of being sold
## base price
#
# Each sale price should vary by ±15% (use a function like your find_approximate_value).
#
# You have 7 days.
#
# Each day:
## either a sale happens or not
## if a sale happens, choose a product category
## add the sale price to total revenue
## At the end, print:  # type: ignore
## total revenue
## number of sales per category

import random
from enum import Enum

def find_aproximate_value(value):
    lowest_value = int(value - value * 0.15)
    highest_value = int(value + value * 0.15)
    return random.randint(lowest_value, highest_value)


event = Enum('Event', ['Sales', 'Empty'])
lose_chance = {event.Chest: 0.6,
            event.Empty: 0.4}


categories = Enum ('Shop',{'food': 'groceries',
              'electronics': 'phone and TV',
              'clothes': 'sport'
              })



