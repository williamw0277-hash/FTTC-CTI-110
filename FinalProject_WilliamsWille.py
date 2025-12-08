# Willie Williams
# Date: 12/08/2025
# Assignment Name: CTI 110 Final Project - Text Adventure Game
# Brief description of program:
#   This program is a simple text-based adventure game. The player creates a hero
#   character and explores a small world, encountering random events and enemies.
#   The game uses functions, dictionaries, random events, and timed pauses to
#   simulate a basic game loop until the player chooses to quit or is defeated.

import random
import time


def slow_print(text, delay=0.03):
    """Print text one character at a time to make the game feel more animated."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()


def build_player():
    """
    Create the main player character and return it as a dictionary.

    Returns:
        dict: Player information including name, role, stats, and inventory.
    """
    slow_print("Welcome to the Realm of Pythonia! 🐍")
    name = input("What is your hero's name? ")

    # Simple role selection that influences stats
    roles = {
        "1": ("Warrior", 30, 6, 3),
        "2": ("Rogue", 24, 7, 2),
        "3": ("Mage", 22, 8, 1),
    }

    print("\nChoose a class for your hero:")
    print("1) Warrior ⚔️  (Balanced health and damage)")
    print("2) Rogue 🗡️   (Higher damage, lower health)")
    print("3) Mage 🔮    (Highest damage, lowest health)")

    choice = ""
    while choice not in roles:
        choice = input("Enter 1, 2, or 3: ").strip()

    role_name, hp, attack, defense = roles[choice]

    # Player dictionary required by the assignment
    player = {
        "name": name,
        "role": role_name,
        "max_hp": hp,
        "hp": hp,
        "attack": attack,
        "defense": defense,
        # Optional inventory dictionary
        "inventory": {
            "potions": 2,
            "gold": 0,
        },
        "wins": 0,
    }

    slow_print(f"\nWelcome, {player['name']} the {player['role']}! ✨")
    return player


def build_enemy():
    """
    Create and return a random enemy as a dictionary (non-player character).
    """
    enemy_types = [
        ("Slime", 14, 4, 1),
        ("Goblin", 18, 5, 2),
        ("Skeleton", 20, 6, 2),
        ("Shadow Wolf", 22, 7, 3),
    ]

    name, hp, attack, defense = random.choice(enemy_types)
    enemy = {
        "name": name,
        "hp": hp,
        "max_hp": hp,
        "attack": attack,
        "defense": defense,
    }
    return enemy


def display_character(character):
    """
    Non-value returning function that prints a character's information.
    Works for both player and enemy dictionaries.
    """
    print("-" * 40)
    print(f"Name:   {character['name']}")
    role = character.get("role")
    if role:
        print(f"Class:  {role}")
    print(f"HP:     {character['hp']} / {character['max_hp']}")
    print(f"ATK:    {character['attack']}")
    print(f"DEF:    {character['defense']}")
    if "inventory" in character:
        inv = character["inventory"]
        print(f"Gold:   {inv.get('gold', 0)}")
        print(f"Potions:{inv.get('potions', 0)}")
        print(f"Wins:   {character.get('wins', 0)}")
    print("-" * 40)


def calculate_damage(attacker, defender):
    """
    Value-returning function that calculates how much damage an attacker deals
    to a defender. Uses randomness for variety.

    Returns:
        int: The final damage value (never less than 1).
    """
    # Base damage is attack minus defense plus a small random variance
    variance = random.randint(-1, 3)
    raw_damage = attacker["attack"] - defender["defense"] + variance
    damage = max(1, raw_damage)
    return damage


def use_potion(player):
    """Allow the player to use a potion to heal."""
    potions = player["inventory"].get("potions", 0)
    if potions <= 0:
        print("You do not have any potions left!")
        return

    if player["hp"] == player["max_hp"]:
        print("You are already at full health.")
        return

    player["inventory"]["potions"] -= 1
    heal_amount = random.randint(6, 12)
    player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
    print(f"You drink a potion and recover {heal_amount} HP! ❤️")
    print(f"Current HP: {player['hp']} / {player['max_hp']}")


def combat(player, enemy):
    """
    Run the combat loop between the player and a single enemy.
    Returns True if player wins, False if the player is defeated.
    """
    slow_print(f"\nA wild {enemy['name']} appears! 👾")
    time.sleep(0.5)
    display_character(enemy)

    while enemy["hp"] > 0 and player["hp"] > 0:
        print("\nWhat will you do?")
        print("1) Attack")
        print("2) Use potion")
        print("3) Attempt to run")
        choice = input("Choose an action (1-3): ").strip()

        if choice == "1":
            # Player attacks
            dmg = calculate_damage(player, enemy)
            enemy["hp"] -= dmg
            print(f"\nYou strike the {enemy['name']} for {dmg} damage! 💥")
            if enemy["hp"] <= 0:
                slow_print(f"The {enemy['name']} is defeated!")
                player["wins"] += 1
                gold_found = random.randint(5, 15)
                player["inventory"]["gold"] += gold_found
                slow_print(f"You find {gold_found} gold coins. 💰")
                # Chance to get another potion
                if random.random() < 0.3:
                    player["inventory"]["potions"] += 1
                    slow_print("You also find a healing potion! 🧪")
                return True

        elif choice == "2":
            use_potion(player)
        elif choice == "3":
            if random.random() < 0.5:
                slow_print("You successfully escape the battle! 🏃")
                return True
            else:
                slow_print("You fail to escape!")
        else:
            print("Invalid choice. You hesitate...")

        # Enemy turn if it is still alive
        if enemy["hp"] > 0:
            time.sleep(0.5)
            dmg = calculate_damage(enemy, player)
            player["hp"] -= dmg
            print(f"The {enemy['name']} hits you for {dmg} damage!")
            print(f"Your HP: {player['hp']} / {player['max_hp']}")

            if player["hp"] <= 0:
                slow_print("You have been defeated... Game Over. 💀")
                return False

    return player["hp"] > 0


def town_menu(player):
    """
    Simple "town" where the player can rest, view stats, or visit the shop.
    """
    while True:
        print("\n🏘️  You are in the town of Pyville.")
        print("1) Venture into the wilds")
        print("2) View character")
        print("3) Rest at the inn (restore HP for 5 gold)")
        print("4) Visit the shop")
        print("5) Quit game")

        choice = input("Choose an action (1-5): ").strip()

        if choice == "1":
            # Exploration leads to combat or a random find
            explore(player)
            if player["hp"] <= 0:
                return  # Player died during exploration
        elif choice == "2":
            display_character(player)
        elif choice == "3":
            rest(player)
        elif choice == "4":
            shop(player)
        elif choice == "5":
            slow_print("Thanks for playing! Goodbye, hero. 👋")
            break
        else:
            print("Please choose a valid option.")


def explore(player):
    """Handle a simple exploration event with a random outcome."""
    slow_print("\nYou walk beyond the town gates and into the forest...")
    time.sleep(0.7)

    event_roll = random.random()
    if event_roll < 0.6:
        enemy = build_enemy()
        combat(player, enemy)
    elif event_roll < 0.85:
        gold_found = random.randint(5, 20)
        player["inventory"]["gold"] += gold_found
        slow_print(f"You find a small chest containing {gold_found} gold! 💰")
    else:
        slow_print("The forest is quiet. Nothing happens this time.")


def rest(player):
    """Allow the player to rest and restore HP at the cost of gold."""
    if player["inventory"]["gold"] < 5:
        print("You do not have enough gold to rest at the inn (costs 5).")
        return

    confirm = input("Resting costs 5 gold. Rest and restore all HP? (y/n): ").strip().lower()
    if confirm == "y":
        player["inventory"]["gold"] -= 5
        player["hp"] = player["max_hp"]
        slow_print("You rest at the inn and feel completely refreshed. 😌")
    else:
        print("You decide not to rest right now.")


def shop(player):
    """Simple shop interface where player can buy potions."""
    slow_print("\nYou enter the small item shop.")
    while True:
        print(f"\nGold: {player['inventory']['gold']}")
        print("1) Buy healing potion (cost: 8 gold)")
        print("2) Leave shop")
        choice = input("Choose an action (1-2): ").strip()

        if choice == "1":
            if player["inventory"]["gold"] >= 8:
                player["inventory"]["gold"] -= 8
                player["inventory"]["potions"] += 1
                print("You purchase a healing potion. 🧪")
            else:
                print("You do not have enough gold.")
        elif choice == "2":
            slow_print("You leave the shop and return to town.")
            break
        else:
            print("Please choose a valid option.")


def main():
    """Main function that starts and runs the game."""
    player = build_player()
    town_menu(player)


# This check makes sure main() only runs when this file is executed directly.
if __name__ == "__main__":
    main()
