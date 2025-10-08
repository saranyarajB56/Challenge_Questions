# Mini RPG Battle Simulator

import random

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        reduced = max(0, damage - self.defense)
        self.hp -= reduced
        print(f"{self.name} takes {reduced} damage (reduced from {damage})!")

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(f"{self.name} HP: {self.hp}/{self.max_hp}")

def player_turn(player, enemy):
    print("\nYour turn:")
    choice = input("Choose action (attack/defend): ").lower()
    if choice == "attack":
        base_damage = random.randint(player.attack // 2, player.attack)
        crit = random.random() < 0.2
        damage = base_damage * 2 if crit else base_damage
        print(f"{player.name} attacks with {damage} damage!" + (" 💥 Critical hit!" if crit else ""))
        enemy.take_damage(damage)
    elif choice == "defend":
        player.defense += 2
        print(f"{player.name} raises defense to {player.defense} for this turn.")
    else:
        print("Invalid action. Turn skipped.")

def enemy_turn(enemy, player):
    print("\nEnemy's turn:")
    action = random.choice(["attack", "attack", "defend"])  # more likely to attack
    if action == "attack":
        damage = random.randint(enemy.attack // 2, enemy.attack)
        print(f"{enemy.name} attacks with {damage} damage!")
        player.take_damage(damage)
    else:
        enemy.defense += 2
        print(f"{enemy.name} raises defense to {enemy.defense} for this turn.")

def battle():
    player = Character("Hero", hp=100, attack=20, defense=5)
    enemy = Character("Dark Wolf", hp=100, attack=18, defense=4)

    print("🔥 Battle Begins 🔥")
    while player.is_alive() and enemy.is_alive():
        player.show_status()
        enemy.show_status()
        player_turn(player, enemy)
        if enemy.is_alive():
            enemy_turn(enemy, player)

    print("\n🏁 Battle Over 🏁")
    if player.is_alive():
        print("🎉 You are victorious!")
    else:
        print("💀 You have been defeated...")

# Start the game
battle()