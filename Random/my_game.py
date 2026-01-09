'''You have two sides:
Player
Opponent

Each has:
health points (HP)
hit chance / dodge
damage range

And:

a while loop that runs as long as someone has HP > 0

random, żeby było losowo

Game logic (step by step)

Start:
Player has 100 HP
Opponent has 100 HP

Round:
Player attacks
you roll: hit / miss
if hit → you roll damage
subtract opponent's HP

Opponent attacks (same)

Display:
damage
current HP of both sides
Loop ends when:
Player's HP ≤ 0 or
Opponent's HP ≤ 0'''


import random

# HP gamer
player_hp = 100
enemy_hp = 100

# Damage gamer 

player_damage = (5, 15)
enemy_damage = (7, 20)

player_hit_chance = 70
enemy_hit_chance = 60

round_number = 1

# Core Game

while player_hp > 0 and enemy_hp > 0:
    print(f"you survive we go to the next round.Round: {round_number}")

# Player Attack

    if random.randint(1, 100) <= player_hit_chance:
        dmg = random.randint(*player_damage)
        enemy_hp -= dmg 
        print(f"Player hit: {dmg}")
    else:
        print(f"Player Miss. Your hit 0 damage.")
     

    if enemy_hp <= 0:
        print("Enemy is death.You win.")
        break

# Enemy attack 
    if random.randint(1, 100) <= enemy_hit_chance:
        dmg = random.randint(*enemy_damage)
        player_hp -= dmg 
        print(f"Enemy hit: {dmg}")
    else:
        print(f"Enemy Miss. Your hit 0 damage.")

    if player_hp <= 0:
        print("Player is death.You win.")
        break     


    round_number = round_number + 1
    

# Output fight
    print(f"Player attack: {player_damage}")
    print(f"Player HP: {player_hp}")
    print(f"Enemey attack: {enemy_damage}")
    print(f"Enemy HP: {enemy_hp}")





