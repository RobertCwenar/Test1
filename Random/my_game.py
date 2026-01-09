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
player_hp = 500
enemy_hp = 500

# Damage gamer 

player_damage = (5, 15)
enemy_damage = (7, 20)

player_hit_chance = 70
enemy_hit_chance = 60

add_weapons = {"Weapon Bow": (30, 60),
             "Weapon Sword": (25, 75),
             "Weapon Degger": (20, 50),
             "Weapon AX": (15, 35),
            "Weapon magic staff": (20, 25)}

def attack(player_base_damage, weapon_range, hit_chance):
        if random.randint(1,100) <= hit_chance:
            base_dmg = random.randint(*player_base_damage)
            weapon_dmg = random.randint(*weapon_range)
            total_dmg = base_dmg + weapon_dmg
            return total_dmg
        else:
            return 0
                          
round_number = 1


# Core Game

while player_hp > 0 and enemy_hp > 0:
    print(f"You survived we went to the next round. Round: {round_number}")

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

    chosen_weapons = random.choice(list(add_weapons.keys()))
    weapon_range = (add_weapons[chosen_weapons])
    dmg = attack(player_damage, weapon_range, player_hit_chance)
    enemy_hp -= dmg
    print(f"Player hits with {chosen_weapons} for {dmg} damage")

# Enemy attack 
    if random.randint(1, 100) <= enemy_hit_chance:
        dmg = random.randint(*enemy_damage)
        player_hp -= dmg 
        print(f"Enemy hit: {dmg} and {chosen_weapons}")
    else:
        print(f"Enemy Miss. Your hit 0 damage.")
    
    chosen_weapons = random.choice(list(add_weapons.keys()))
    weapon_range = (add_weapons[chosen_weapons])
    dmg = attack(enemy_damage, weapon_range, enemy_hit_chance)
    player_hp -= dmg
    print(f"Enemy hits with {chosen_weapons} for {dmg} damage")

    if player_hp <= 0:
        print("You lose.")
        break     

    round_number = round_number + 1
    

# Output fight
    print(f"Player HP: {player_hp}")
    print(f"Enemy HP: {enemy_hp}")

    # Ask player if they want to continue
    choice = input("Continue to next round? (y/n): ").lower()
    if choice != 'y': 
        print("Game stopped player escape.")
        break

print("Game over")




