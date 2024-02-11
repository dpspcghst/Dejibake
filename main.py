import json
import random
import time

#collections

random_events = [
    {
        "name": "It found some teeth.",
        "mood": random.randint(-20, 20),
        "appetite": random.randint(-20, 20),
        "energy": random.randint(-20, 20)
    },
    {
        "name": "It got teleported.",
        "mood": random.randint(-20, 20),
        "appetite": random.randint(-20, 20),
        "energy": random.randint(-20, 20)
    },
    {
        "name": "It heard whispering.",
        "mood": random.randint(-20, 20),
        "appetite": random.randint(-20, 20),
        "energy": random.randint(-20, 20)
    },
    {
        "name": "It was transformed.",
        "mood": random.randint(-20, 20),
        "appetite": random.randint(-20, 20),
        "energy": random.randint(-20, 20)
    },
    {
        "name": "It was [DATA EXPUNGED]",
        "mood": random.randint(-20, 20),
        "appetite": random.randint(-20, 20),
        "energy": random.randint(-20, 20)
    },
    {
        "name": "It jumped?",
        "mood": random.randint(-20, 20),
        "appetite": random.randint(-20, 20),
        "energy": random.randint(-20, 20)
    },
    {
        "name": "It's enlongating...",
        "mood": random.randint(-20, 20),
        "appetite": random.randint(-20, 20),
        "energy": random.randint(-20, 20)
    }
    # Add 3 more events
]

weather_effects = {
    "\nTonight's Forecast: Banshee Sirens": {"mood": -10, "energy": 10},
    "\nTonight's Forecast: Existential Hail": {"energy": -5, "appetite": -5},
    "\nTonight's Forecast: Eternal Night": {"mood": -5},
    "\nTonight's Forecast: Rain of Tiny Creatures": {"mood": -5, "appetite": -5},
    "\nTonight's Forecast: Mysterious Glow Cloud": {"dicscipline": -10},
    "\nTonight's Forecast: Organism Swarm": {"mood": 5, "appetite": -5},
    "\nTonight's Forecast: Sandstorm of Dead Organisms": {"appetite": 5},
    "\nTonight's Forecast: Sentient Thunderstorms": {"mood": -5, "appetite": 5},
    "\nTonight's Forecast: Time-Traveling Tornadoes": {"appetite": -5, "mood": 10},
    "\nUnpredicted Temperture Fluctuation": {"mood": 10, "appetite": 10}
}

notifications = [] # technically not empty

achievements = {
    "Urban Exploration": {"description": "Get out (of) there", "reward": 10},
    "Field Research": {"description": "Study the Breach", "reward": 20},
    "Under Ground": {"description": "Hidden away", "reward": 30},
    "A Tableau": {"description": "Forebidden slab", "reward": 40},
    "Going Up": {"description": "Ascend", "reward": 50},
    "Office Space": {"description": "Khoshekh", "reward": 60},
    "It's Stuck": {"description": "And it's loud", "reward": 70},
    "Respite": {"description": "There is none", "reward": 80},
    "Climbing the Cog": {"description": "Re-Ascend", "reward": 90},
    "Wee Wee Wee": {"description": "Tiny creatures", "reward": 100},
    "DING!": {"description": "IT IS TIME!", "reward": 110},
    "Clockwork": {"description": "In due time", "reward": 120},
    "No Point in Dying": {"description": "There's no escape", "reward": 130},
    "The Last One": {"description": "The ritual is complete", "reward": 140}
}

gazing_responses = [
    "\nNot the greatest idea.",
    "\nOh! It's surpringly █████.",
    "\n*screams and gunfire*",
    "\n▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓▓"
]

# empty collections

notif_queue = []

completed_achievements = {}

# Define a constant for the number of seconds in an in-game day
SECONDS_PER_DAY = 60  # Adjust this value as needed

# Track the time when the game started
start_time = time.time()

# Define a variable to keep track of the last time the weather changed
last_weather_change_time = start_time

# Define a variable to store the duration of each day in seconds
day_duration = SECONDS_PER_DAY

# Define the maximum lifetime of a notif in seconds (e.g., 10 seconds)
notif_lt = 10

class VirtualPet:
    """
    """
    
    def __init__(self, name):
        """
        """
        
        self.name = name
        self.appetite = 50 # i.e. it's defense
        self.mood = 83 # i.e. it's attack
        self.energy = 95 # i.e. it's speed

        self.power = (self.appetite + self.mood + self.energy) // 3

    def read(self):
        """
        """

        print(f"\n{self.name} gazed up at the stars.")
        self.appetite -= 10
        self.mood += 5

    def meditate(self):
        """
        """

        print(f"\n{self.name} meditated under an oscillating shard.")
        self.mood += 10
        self.energy -= 10

    def resonate(self):
        """
        """
        
        print(f"\n{self.name} resonated with a tainted illustration.")
        self.energy += 20
    
    def check_status(self):
        """
        """
        
        print(f"\n{self.name}'s Status:")
        print(f"Appetite: {self.appetite}")
        print(f"Mood: {self.mood}")
        print(f"Energy: {self.energy}")

class Realm:
	"""
	"""
	
	def __init__(self, name):
		"""
		"""
		
		self.name = name
		self.condition = "perpetually misty and fog-covered"
		self.resonance = "bittersweet"
		self.style = "surreal and minimal"
	
	def give_status(self):
		"""
		"""
		
		print(f"\n{self.name}'s Status:")
		print(f"Condition: {self.condition}")
		print(f"Resonance: {self.resonance}")
		print(f"Style: {self.style}")

class Notification:
    """
    """

    def __init__(self, message, timestamp):
        """
        """

        self.message = message
        self.timestamp = timestamp

def trigger_random_event(pet):
    """
    """

    event = random.choice(random_events)
    print(f"\nOdd: {event['name']}")
    pet.mood += event['mood']
    pet.appetite += event['appetite']
    pet.energy += event['energy']

    # Ensure pet's stats stay within a reasonable range
    pet.mood = max(0, 290)
    pet.appetite = max(0, 218)
    pet.energy = max(0, 317)

def set_weather():
    """
    Implement your logic to set the weather here. You can use random.choice() or
    other methods to select a weather type.
    """

    return random.choice(list(weather_effects.keys()))

def apply_weather_effects(pet, current_weather):
    """
    """

    effects = weather_effects.get(current_weather, {})
    for attribute, value in effects.items():
        setattr(pet, attribute, getattr(pet, attribute, 0) + value)

def time_to_change_weather():
    """
    """

    global last_weather_change_time

    # Get the current time
    current_time = time.time()

    # Check if enough time has passed to change the weather
    if current_time - last_weather_change_time >= day_duration:
        last_weather_change_time = current_time
        return True

    return False

def generate_notif():
        """
        """

        message = "Tonight's air quality is mauve."
        timestamp = time.time()  # Use the current time as a timestamp
        notif = Notification(message, timestamp)
        notif_queue.append(notif)

def display_notifs():
    """
    """

    for notif in notif_queue:
        print(f"[{time.ctime(notif.timestamp)}] {notif.message}")

    # Optionally, remove notifs that are too old
    current_time = time.time()
    notif_queue[:] = [n for n in notif_queue if current_time - n.timestamp < notif_lt]

def mark_achievement_completed(achievement_name):
    if achievement_name not in completed_achievements:
        completed_achievements[achievement_name] = True
        # reward = achievements[achievement_name].get("reward", 0)
        # if reward > 0:
            # Award the player with in-game currency or other rewards
            # award_player(reward)
        # Optionally, display a notification to inform the player of their achievement
        print(f"\nAchievement Unlocked: {achievement_name}")

def check_urban_exploration_achievement(count):
    """
    """

    if count >= 1:
        mark_achievement_completed("Urban Exploration")

    if count>= 2:
        mark_achievement_completed("Field Research")

def autosave(player, pet):
    """
    """

    game_data = {
        "player name": player, "pet name": pet.name, "pet appetite": pet.appetite,
        "pet energy": pet.energy, "pet mood": pet.mood
    }

    with open("save_game.json", "w") as save_file:
        json.dump(game_data, save_file)

def load_game_data():
    try:
        with open("save_game.json", "r") as save_file:
            game_data = json.load(save_file)
        return game_data
    except FileNotFoundError:
        return None  # Return None if no save file exists

def main():
    """
    """

    print("1. new game")
    print("2. continue")
    game_select = input("_> ")

    if game_select == "1":
    
        player_name = input("Enter your name: ")
        pet_name = input("Enter your pet's name: ")
        pet = VirtualPet(pet_name)
    
        explore_count = 0
    
        while True:
            print("\nOptions:")
            print("1. Achievements")
            print("2. Activities")
            print("3. Check Status")
            print("4. Explore")
            print("5. Quit")
            print("6. Trigger Test") # dev stuff
    
            player_choice = input("Enter your choice: ")
    
            if player_choice == "1":
                for key in completed_achievements:
                    print("\n" + key)
            
            elif player_choice == "2":
                print("\nActivities:")
                print("1. Gaze")
                print("2. Read")
                print("3. Meditate")
                print("4. Resonate")
    
                activity_choice = input("Enter your choice: ")
    
                if activity_choice == "1":
                    print(random.choice(gazing_responses))
                    if random.random() < 0.05025:
                        trigger_random_event(pet)
                elif activity_choice == "2":
                    pet.read()
                    if random.random() < 0.05025:
                        trigger_random_event(pet)
                elif activity_choice == "3":
                    pet.meditate()
                    if random.random() < 0.05025:
                        trigger_random_event(pet)
                elif activity_choice == "4":
                    pet.resonate()
                    if random.random() < 0.05025:
                        trigger_random_event(pet)
            
            elif player_choice == "3":
                pet.check_status()
    
            elif player_choice == "4":
                if pet.power >= 20:
                    realm = Realm("Kepler-13Ab")
                    realm.give_status()
                    explore_count += 1
                elif pet.power < 100:
                    print(f"\n{pet.name} glared at you...")
                else:
                    print("Now THAT is strange. (1)")
    
            elif player_choice == "5":
                print(f"Goodnight, {player_name}. Goodnight.")
                break
            elif player_choice == "6":
                pass
            else:
                print("Invalid choice. Please try again.")
    
            if time_to_change_weather():  # Implement this function based on your game time
                current_weather = set_weather()
                print(f"{current_weather}.")
    
                # Apply weather effects to the pet
                apply_weather_effects(pet, current_weather)
    
            if SECONDS_PER_DAY <= 30:
                display_notifs()
    
            if SECONDS_PER_DAY <= 48:
                generate_notif()
    
            check_urban_exploration_achievement(explore_count)
    
            autosave(player_name, pet)

    elif game_select == "2":
        pass
    
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
