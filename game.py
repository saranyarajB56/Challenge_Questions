#  Mini RPG Battle Simulator

import random

# Basic character setup
player = {
    "name": "Hero",
    "hp": 100,
    "attack": 15
}

enemy = {
    "name": "Goblin",
    "hp": 100,
    "attack": 10
}

# Game loop
print("⚔️ A wild Goblin appears!")
while player["hp"] > 0 and enemy["hp"] > 0:
    print(f"\n{player['name']} HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")
    action = input("Choose action (attack): ").lower()

    if action == "attack":
        damage = random.randint(5, player["attack"])
        enemy["hp"] -= damage
        print(f"You hit the Goblin for {damage} damage!")

    if enemy["hp"] > 0:
        damage = random.randint(5, enemy["attack"])
        player["hp"] -= damage
        print(f"Goblin hits you for {damage} damage!")

# Outcome
if player["hp"] > 0:
    print("\n🎉 You defeated the Goblin!")
else:
    print("\n💀 You were defeated...")
