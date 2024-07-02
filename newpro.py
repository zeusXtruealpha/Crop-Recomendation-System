"""
Crop Recommendation System

This program implements a Crop Recommendation System that suggests suitable crops to grow based on environmental conditions
such as pH, temperature, rainfall, and nutrient levels. It allows users to create accounts, log in, enter environmental data,
and receive crop recommendations.

The system consists of the following classes:
1. TrieNode: Represents a node in the trie data structure used for storing user information.
2. UserNode: Represents a node in the linked list storing user data.
3. User: Represents a user account with a username, password, and optional environmental data.
4. Trie: Implements a trie data structure to store user accounts efficiently.
5. CropRecommendationPlanner: Manages user interactions, stores crop recommendations, and provides recommendation functions.

The CropRecommendationPlanner class includes methods for:
- Creating user accounts
- Logging in and out
- Entering environmental data
- Recommending crops based on environmental conditions

The recommendation algorithm considers pH, temperature, rainfall, and nutrient levels (nitrogen, phosphorus, potassium)
to suggest suitable crops with or without the need for fertilizers.

Example usage:
The main block provides a command-line interface for users to interact with the system.

"""

# Define the TrieNode class representing a node in the trie data structure
class TrieNode:
    def __init__(self):
        # Initializes a TrieNode with children dictionary, end of word flag, and linked list head.
        self.children = {}
        self.is_end_of_word = False
        self.user_data_head = None  # Head of the linked list

# Define the UserNode class representing a node in the linked list storing user data
class UserNode:
    # Initializes a UserNode with user object and reference to the next node.
    def __init__(self, user):
        self.user = user
        self.next = None

# Define the User class representing a user account
class User:
    # Initializes a User with username, password, and optional environment data.
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.environment_data = None

# Define the Trie class implementing a trie data structure for efficient user account storage
class Trie:
    # Initializes a Trie with a root node.
    def __init__(self):
        self.root = TrieNode()

    def insert(self, username, password):
        # Inserts a new user into the trie.
        node = self.root
        for char in username:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if not node.is_end_of_word:
            node.is_end_of_word = True
            node.user_data_head = UserNode(User(username, password))
        else:
            # Traverse the linked list to find the last node
            current = node.user_data_head
            while current.next:
                current = current.next
            current.next = UserNode(User(username, password))

    def search(self, username):
        # Searches for a user in the trie.
        node = self.root
        for char in username:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.user_data_head if node.is_end_of_word else None

# Define the CropRecommendationPlanner class managing user interactions and crop recommendations.
class CropRecommendationPlanner:
    def __init__(self):
        # Initializes a CropRecommendationPlanner with user trie, current user, crop suggestions, and nutrient requirements.
        self.users = Trie()
        self.current_user = None
        # Data for the pH_requirments
        self.pH_requirements = {
            (5.5, 7.0): ["Rice"],
            (6.0, 7.5): ["Peas", "Maize"],
            (6.0, 7.0): ["Wheat", "Okra", "Groundnut", "Garlic"],
            (6.0, 6.8): ["Okra", "Brinjal (Eggplant)"],
            (5.5, 8.0): ["Sugarcane"],
            (6.5, 7.5): ["Cucumber", "Watermelon", "Soybean", "Banana", "Mustard", "Tomato", "Citrus (Orange/Lemon)", "Grape", "Chilli", "Papaya"],
            (5.0, 7.5): ["Cotton"],
            (5.5, 7.5): ["Mango", "Banana", "Citrus (Orange/Lemon)", "Onion", "Radish"],
            (4.8, 5.4): ["Potato"],
            (4.0, 8.5): ["Guava"],
            (5.0, 6.0): ["Pineapple"],
            (7.0, 8.0): ["Barley"],
            (5.5, 6.0): ["Beans"],
            (5.5, 6.5): ["Cauliflower", "Cabbage"],
        }

        # Data for the npk_requirments
        self.npk_requirements = {
            "Rice": {"N": (80, 120), "P": (20, 40), "K": (40, 60)},
            "Peas": {"N": (40, 80), "P": (40, 80), "K": (40, 80)},
            "Wheat": {"N": (80, 120), "P": (40, 60), "K": (40, 80)},
            "Okra": {"N": (100, 150), "P": (50, 80), "K": (50, 100)},
            "Maize": {"N": (100, 150), "P": (50, 100), "K": (50, 100)},
            "Brinjal (Eggplant)": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Sugarcane": {"N": (100, 200), "P": (50, 100), "K": (100, 200)},
            "Cucumber": {"N": (100, 150), "P": (50, 80), "K": (100, 150)},
            "Cotton": {"N": (100, 200), "P": (40, 80), "K": (50, 100)},
            "Watermelon": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Groundnut": {"N": (40, 80), "P": (40, 80), "K": (40, 80)},
            "Mango": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Soybean": {"N": (80, 120), "P": (40, 80), "K": (40, 80)},
            "Banana": {"N": (100, 200), "P": (50, 100), "K": (100, 200)},
            "Mustard": {"N": (40, 80), "P": (40, 80), "K": (40, 80)},
            "Pineapple": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Potato": {"N": (100, 150), "P": (80, 120), "K": (120, 180)},
            "Guava": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Tomato": {"N": (100, 150), "P": (80, 120), "K": (120, 180)},
            "Citrus (Orange/Lemon)": {"N": (100, 200), "P": (50, 100), "K": (100, 200)},
            "Onion": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Grape": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Carrot": {"N": (100, 150), "P": (80, 120), "K": (120, 180)},
            "Cauliflower": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Cabbage": {"N": (100, 150), "P": (80, 120), "K": (120, 180)},
            "Chilli": {"N": (100, 150), "P": (80, 120), "K": (120, 180)},
            "Papaya": {"N": (100, 150), "P": (80, 120), "K": (120, 180)},
            "Barley": {"N": (80, 120), "P": (40, 60), "K": (40, 80)},
            "Garlic": {"N": (100, 150), "P": (80, 120), "K": (120, 180)},
            "Beans": {"N": (80, 120), "P": (40, 80), "K": (80, 120)},
            "Radish": {"N": (80, 120), "P": (40, 80), "K": (80, 120)}
        }

    def create_account(self, username, password):
        # Creates a new user account.
        if self.users.search(username):
            print("Username already exists. Please choose another one.")
        else:
            self.users.insert(username, password)
            print("Account created successfully.")

    def login(self, username, password):
        # Logs in a user.
        user_data = self.users.search(username)
        if user_data and user_data.user.password == password:
            self.current_user = user_data.user
            print(f"Logged in as {username}.\n")
        else:
            print("Invalid username or password.")

    def logout(self):
        # Logs out the current user.
        self.current_user = None
        print("Logged out successfully.")

    def enter_environment_data(self, pH, temperature, rainfall, nitrogen, phosphorus, potassium):
        # Enters environmental data for the current user.
        if self.current_user:
            self.current_user.environment_data = {
                "pH": pH, 
                "temperature": temperature, 
                "rainfall": rainfall,
                "nitrogen": nitrogen,
                "phosphorus": phosphorus,
                "potassium": potassium
            }
            print("Environment data entered successfully. \n")
        else:
            print("Please login to enter environment data.")

    def show_data(self):
        # Shows the data entered by the user
        """Displays the environmental data entered by the current user."""
        if self.current_user and self.current_user.environment_data:
            data = self.current_user.environment_data
            print("Environmental Data:")
            print(f"pH: {data['pH']}")
            print(f"Temperature: {data['temperature']}°C")
            print(f"Rainfall: {data['rainfall']} mm")
            print(f"Nitrogen: {data['nitrogen']} kg/ha")
            print(f"Phosphorus: {data['phosphorus']} kg/ha")
            print(f"Potassium: {data['potassium']} kg/ha")
        else:
            print("No environmental data available.")
    
    def recommend_crops(self):
        #  Recommends crops based on environmental data of the current user.
        if not self.current_user or not self.current_user.environment_data:
            print("Please enter environmental details first.")
            return

        environment_data = self.current_user.environment_data
        pH = environment_data["pH"]
        temperature = environment_data["temperature"]
        rainfall = environment_data["rainfall"]
        nitrogen = environment_data["nitrogen"]
        phosphorus = environment_data["phosphorus"]
        potassium = environment_data["potassium"]

        crops_with_fertilizer = set()
        crops_without_fertilizer = set()
        printed_crops = set()
        for (pH_lower, pH_upper), suggested_crops in self.pH_requirements.items():
            if pH_lower <= pH <= pH_upper:
                for crop in suggested_crops:
                    temp_range = self._get_temperature_range(crop)
                    rain_range = self._get_rainfall_range(crop)
                    npk_range = self._get_npk_range(crop)

                    # Check if current nutrient levels meet the requirements without fertilizer
                    if (temp_range and temp_range[0] <= temperature <= temp_range[1] and rain_range and rain_range[0] <= rainfall <= rain_range[1] and
                        npk_range and
                        npk_range["N"][0] <= nitrogen <= npk_range["N"][1] and
                        npk_range["P"][0] <= phosphorus <= npk_range["P"][1] and
                        npk_range["K"][0] <= potassium <= npk_range["K"][1]):
                        crops_without_fertilizer.add(crop)

                    # Check possibilities by adding fertilizer
                    for i in range(0, 4):  # Iterate through multiples of 20 (0, 20, 40, 60) for nitrogen
                        new_nitrogen = nitrogen + (i * 20)
                        if new_nitrogen <= 200:  # Check if nitrogen limit is not exceeded
                            for j in range(0, 4):  # Iterate through multiples of 20 (0, 20, 40, 60) for phosphorus
                                new_phosphorus = phosphorus + (j * 20)
                                if new_phosphorus <= 120:  # Check if phosphorus limit is not exceeded
                                    for k in range(0, 4):  # Iterate through multiples of 20 (0, 20, 40, 60) for potassium
                                        new_potassium = potassium + (k * 20)
                                        if new_potassium <= 200:  # Check if potassium limit is not exceeded
                                            for crop in suggested_crops:
                                                npk_range = self._get_npk_range(crop)
                                                if (npk_range and npk_range["N"][0] <= new_nitrogen <= npk_range["N"][1] and
                                                    npk_range["P"][0] <= new_phosphorus <= npk_range["P"][1] and
                                                    npk_range["K"][0] <= new_potassium <= npk_range["K"][1]):
                                                    crops_with_fertilizer.add((crop, (i * 20, j * 20, k * 20)))

        if not crops_without_fertilizer:
            print("No crop recommendations available without using fertilizers.\n")
        else:
            print("Crops that can be produced without adding fertilizer:")
            for crop in crops_without_fertilizer:
                print(crop)
                printed_crops.add(crop)

        if crops_with_fertilizer:
            print("\nRecommended crops and minimum fertilizer combinations:")
            for crop, fertilizer in crops_with_fertilizer:
                if crop not in printed_crops:  # Check if crop hasn't been printed yet
                    print(f"{crop} (Minimum Fertilizer: N+{fertilizer[0]} P+{fertilizer[1]} K+{fertilizer[2]})")
                    printed_crops.add(crop)
        else:
            print("No crop recommendations available for the given environmental conditions. \n")

    def show_crop_data(self, crop_name):
        # shows the data of the specified class
        """Displays pH, rainfall, temperature, and NPK values for a given crop."""
        crop_data = self.npk_requirements.get(crop_name)
        if crop_data:
            print(f"Crop: {crop_name}")
            print(f"Temperature Range: {self._get_temperature_range(crop_name)}°C")
            print(f"Rainfall Range: {self._get_rainfall_range(crop_name)} mm")
            print("Nutrient Requirements:")
            print(f"Nitrogen: {crop_data['N'][0]} - {crop_data['N'][1]} kg/ha")
            print(f"Phosphorus: {crop_data['P'][0]} - {crop_data['P'][1]} kg/ha")
            print(f"Potassium: {crop_data['K'][0]} - {crop_data['K'][1]} kg/ha")
        else:
            print("Crop data not available.")

    def _get_temperature_range(self, crop):
        # data for the temperature range.
        temperature_ranges = {
            "Rice": (20, 37),
            "Peas": (10, 25),
            "Wheat": (15, 24),
            "Okra": (21, 35),
            "Maize": (15, 30),
            "Brinjal (Eggplant)": (18, 30),
            "Sugarcane": (20, 30),
            "Cucumber": (20, 30),
            "Cotton": (20, 30),
            "Watermelon": (20, 30),
            "Groundnut": (20, 30),
            "Mango": (24, 30),
            "Soybean": (15, 25),
            "Banana": (15, 35),
            "Mustard": (10, 25),
            "Pineapple": (20, 32),
            "Potato": (15, 20),
            "Guava": (15, 30),
            "Tomato": (15, 30),
            "Citrus (Orange/Lemon)": (15, 30),
            "Onion": (13, 24),
            "Grape": (15, 35),
            "Carrot": (10, 25),
            "Cauliflower": (15, 20),
            "Cabbage": (10, 20),
            "Chilli": (20, 30),
            "Papaya": (21, 33),
            "Barley": (10, 25),
            "Garlic": (12, 24),
            "Beans": (15, 26),
            "Radish": (10, 20),
        }
        return temperature_ranges.get(crop)

    def _get_rainfall_range(self, crop):
        # Data for the rainfall range.
        rainfall_ranges = {
            "Rice": (1000, 2500),
            "Peas": (500, 800),
            "Wheat": (350, 600),
            "Okra": (500, 800),
            "Maize": (500, 1000),
            "Brinjal (Eggplant)": (500, 800),
            "Sugarcane": (1000, 1500),
            "Cucumber": (500, 800),
            "Cotton": (500, 1000),
            "Watermelon": (500, 800),
            "Groundnut": (500, 800),
            "Mango": (600, 2500),
            "Soybean": (500, 1000),
            "Banana": (1000, 2000),
            "Mustard": (500, 750),
            "Pineapple": (1000, 2500),
            "Potato": (400, 600),
            "Guava": (1000, 2000),
            "Tomato": (500, 800),
            "Citrus (Orange/Lemon)": (600, 1500),
            "Onion": (400, 600),
            "Grape": (500, 900),
            "Carrot": (400, 600),
            "Cauliflower": (500, 800),
            "Cabbage": (500, 800),
            "Chilli": (500, 800),
            "Papaya": (1000, 2000),
            "Barley": (400, 600),
            "Garlic": (400, 600),
            "Beans": (500, 800),
            "Radish": (400, 600),
        }
        return rainfall_ranges.get(crop)

    def _get_npk_range(self, crop):
        return self.npk_requirements.get(crop)

# Example usage:
if __name__ == "__main__":
    # Create CropRecommendationPlanner object
    planner = CropRecommendationPlanner()

    # User interaction loop for account management and crop recommendations...
    while True:
        if not planner.current_user:
            print("\n1. Create Account")
            print("2. Login")
        else:
            print("2. Logout")
            print("3. Enter Environment Data")
            print("4. Show environment data")
            print("5. Get Crop Recommendations")
            print("6. Show Crop Data")
        print("7. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            planner.create_account(username, password)

        elif choice == "2":
            if not planner.current_user:
                username = input("Enter username: ")
                password = input("Enter password: ")
                planner.login(username, password)
            else:
                planner.logout()

        elif choice == "3":
            if planner.current_user:
                print("Recomended pH range (4 - 8.5)")
                pH = float(input("Enter pH value: "))
                print("Recomended Temperature range (10°C - 37°C)")
                temperature = float(input("Enter temperature (°C): "))
                print("Recomended Rainfall range (350mm - 2500mm)")
                rainfall = float(input("Enter rainfall (mm): "))
                print("Recomended Nitrogen range (40kg/ha - 200kg/ha)")
                nitrogen = float(input("Enter Nitrogen (kg/ha): "))
                print("Recomended  Phosphorus range (20kg/ha - 120kg/ha)")
                phosphorus = float(input("Enter Phosphorus (kg/ha): "))
                print("Recomended Potassium range (40kg/ha - 200kg/ha)")
                potassium = float(input("Enter Potassium (kg/ha): "))
                planner.enter_environment_data(pH, temperature, rainfall, nitrogen, phosphorus, potassium)
            else:
                print("Please login to enter environment data.")
            
        elif choice == "4":
            if planner.current_user:
                planner.show_data()
            else:
                print("Please login to show data.")

        elif choice == "5":
            if planner.current_user:
                planner.recommend_crops()
            else:
                print("Please login to get crop recommendations.")
        
        elif choice == "6":
            crop_name = input("Enter the crop name: ")
            planner.show_crop_data(crop_name)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")