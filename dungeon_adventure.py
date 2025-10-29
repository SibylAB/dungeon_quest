import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
setup_player = input("Enter Your name: ")
print(f"Welcome, {setup_player}")
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"

setup_player = {
    "name": "",
    "health": 100,
    "inventory": []
}

        # TODO: Return the dictionary

def setup_player():
    setup_player = {
        "name": "",
        "health": 10,
        "inventory":[]
    }

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasures = {
                    "gold coin": 5,
                    "ruby": 10,
                    "talisman": 7,
                    "amethyst": 8,
                    "copper ring": 2
}
        # TODO: Return the dictionary
def treasures():
    treasures = {
        "gold coin": 5,
        "ruby": 10,
        "talisman": 7,
        "amethyst": 8,
        "copper ring": 2
    }
    return treasures


    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above

def display_room_menu(room_number):
    print(f"You are in room {room_number}.")
    print("What would you like to do?")
    print("1. Search for treasure")
    print("2. Move to the next room")
    print("3. Check health and inventory")
    print("4. Quit the game")


    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened
def get_outcome():
    outcome = random.choice(["treasure, trap"])
    return outcome

def handle_outcome(outcome):
    if outcome == "treasure":
        print("You have found hidden treasure!")
    elif outcome == "trap":
        print("Uh oh! You fell into a trap.")
    else:
        print("Something went wrong...")

        print(f"\n Update Stats: {setup_player}")

setup_player = {
    "health": 100,
    "gold": 0
}

def handle_outcome(outcome, stats):
    if outcome == "treasure":
        stats["gold"] += 50
        print("You have found hidden treasure!")
    elif outcome == "trap":
        stats["health"]-= 20
        print("Uh oh! You fell into a trap.")
    else:
        print("Something went wrong...")

print(f"\nUpdated Stats: Health = {setup_player['health']} , Gold = {setup_player['gold']}")


def check_status(player): 
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health

        print("Check your status...\n")

        health = player.get("health", 0)

        if health > 80:
            print(f" Health: {health} - You're doing great!")
        elif health > 50:
            print(f"Health: {health} - Stay cautious, player!")
        elif health > 0:
            print(f" Health: {health} - You're badly injured. Seek help!")
        else:
            print(f"Health: {health} - You have died...")
                

        # TODO: If the inventory list is not empty, print items joined by commas
inventory = setup_player.get("inventory", [])
if inventory:
    print("\n Inventory contains:")
    for item in inventory:
        print(f" -{item}")

        # TODO: Otherwise print “You have no items yet.”

else:
    print("\n Inventory is empty.Time to find loot!")

print("\n Status check complete.\n")

def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures

def display_treasure_value(total_value):
 print(f"\n Total Treasure Value: {total_value} gold coins")

        # TODO: Print final health, items, and total value

health = setup_player.get("health", 0)
print(f"Final Health: {health}")

inventory = setup_player.get("inventory", [])
if inventory:
    print("\n Final Inventory:")
    for item in inventory:
        print(f" - {item}")

        # TODO: End with a message like "Game Over! Thanks for playing."

print("Thanks for playing!\n")

def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)

        room_count = 0
        max_rooms = 5

        while room_count < max_rooms:
            print(f"\n Room {room_count + 1} - Choose your path (1-5) or type 'quit' to exit.")
            choice = input("Enter room number (1-5) or 'quit' : ").strip().lower()

if 'choice' == 'quit':
    print('You ended early. Come back later.')
    

if 'choice' not in ["1", "2", "3", "4", "5"]:
        print("Please, pick a number between 1-5")
   
       

else:
        print(f"You picked option {choice}. Let's continue!")

def enter_room():
    choice = input("Enter a room number: ").strip()

    room_number = int('choice')
    print(f"\n You enter room {'room_number'}")
    return room_number

if 'room_number' == '1':
    print("A drunken dwarf cleric heals you and gives you a amethyst.")
    player["health"] += 10
    player["inventory"].append("amethyst")
elif 'room_number' == '2':
    print("A surprised attack from a goblin. You nearly made it.")
    player["health"] -= 20
elif 'room_number' == '3':
    print("You found the treasure chest with 250 gold!")
    treasures.append({"name": "Chest of Coins", "value": 200})
elif 'room_number' == '4':
    print("A spider lunge at you! You lose 10 health.")
    player["health"] -= 10
elif 'room_number' == '5':
    print("You discovered a secret map and a talisman.")
    player["inventory"].extend(["talisman", "secret map"])
else:
    print("Invalid choice. Please pick a room number between 1 and 5.")

def next_room(current_room):
    current_room += 1
    print(f"You have move to room {current_room}")
    return current_room

    room_number = 1
    room_number = next_room(room_number)
    
    items - ", ".join(setup_player['inventory'])
print(f"\n Health: {setup_player['health']} | Inventory:  {'items'}")
if setup_player["health"] < 0:
    print("You have died")
    
inventory = setup_player.get('inventory', [])
if inventory:
    print("\n Final Inventory:")
    for item in inventory:
        print(f"- {item}")

else:
    print("\n Inventory: Empty")

def calculate_total_value(treasure):
    return sum(t.get("value", 0) for t in treasures)

print(f"]n Total Treasure Value: {'total_value'} gold coins")
print("\n Your quest is complete. Thanks for playing!\n")

player = {
    "health": 10,
    "inventory":[]
}
treasures = []

run_game_loop(player, treasures)

        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored

if __name__ == "__main__":
    main()

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
