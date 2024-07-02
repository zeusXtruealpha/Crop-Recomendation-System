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
