# LaEngine

[中文版本](./README_zh.md)

LaEngine is a game engine designed for creating text-based adventure games (AVG) powered by Large Language Models (LLMs).

## Core Features

LaEngine uniquely combines "Story Nodes" with "LLM-Generated Dialogue". This design ensures a stable main storyline while giving players the freedom to interact with the game world limitlessly, leading to a unique experience every time you play.

## TOML Script Format (Tentative)

The core elements of the game—such as plot, world-building, and characters—are defined in a simple, human-readable TOML file.

```toml
# Game Title
title = "Secret Garden"

#------------------------------------------------------------------------------
#  Global Settings
#------------------------------------------------------------------------------

[world_setting]
# A macro description of this world
descript = "A world where modernity and fantasy intertwine."
# Proper nouns in the game to help the LLM generate more accurate content
nouns = "Magic, Runes, Adventurer's Guild"

[variables]
# Global variables for tracking key events or states
has_met_king = false
power_is_on = false

#------------------------------------------------------------------------------
#  Player Settings
#------------------------------------------------------------------------------

[user_setting]
name = "Alan"
descript = "A young person full of curiosity about the world."
# Player's status values, 'value' is the initial value
status = [
  { name = "health", value = 100, max = 100, min = 0 },
  { name = "mana",   value = 50,  max = 50,  min = 0 },
  { name = "money",  value = 10,  max = 9999, min = 0 }
]

#------------------------------------------------------------------------------
#  Story Nodes
#------------------------------------------------------------------------------

[[nodes]]
id = "wake_up"
descript = "You wake up from a soft bed, warm sunlight streaming through the window."
# Hidden information known only to the LLM, used to enrich responses
hide_descript = "This is a room on the second floor, with a quiet street outside the window."
# Scene atmosphere hints for the LLM
atmosphere = "Cozy, Calm, Safe"

# Objects in this scene
objects = [
  { name = "Desk", detail = "A wooden desk with a few books on it.", location = "In the corner of the room" },
  { name = "Notebook", detail = "An old-looking leather-bound notebook.", location = "In the desk drawer", properties = { takable = true } }
]

# Conditions for node transition
next = [
  { condition = { event = "action", detail = "walk out the door" }, goto = "kitchen" },
  { condition = { event = "action", detail = "jump out the window" }, goto = "dead_end_fall" }
]

# Special event triggers within the node
triggers = {}

max_turn = 10
when_max_turn = "Mom's voice comes from downstairs: 'Alan, hurry down for breakfast!'"

[[nodes]]
id = "kitchen"
descript = "You arrive in the kitchen. Mom is preparing breakfast, and the air is filled with the aroma of bread."
atmosphere = "Warm, Lively"

objects = [
  { name = "Fruit Knife", detail = "A sharp fruit knife.", location = "On the counter", properties = { takable = true, use_on = ["Apple"] } },
  { name = "Apple", detail = "A bright red apple.", location = "In the fruit basket on the table", properties = { takable = true } }
]

next = [
  { condition = { event = "talk", detail = "talk to Mom" }, goto = "breakfast_dialogue" }
]

triggers = { on_enter = "Mom smiles and greets you: 'Dear, you're awake!'" }


#------------------------------------------------------------------------------
#  Characters
#------------------------------------------------------------------------------

[[characters]]
id = "mom"
name = "Mom"
descript = "A kind but sometimes nagging mother."
# A dedicated 'role-playing guide' for the LLM to ensure a consistent character persona
personality = "Always calls the player 'dear', is concerned about the player's health, and loves to share neighborhood gossip."

# Character's status values
status = [
  { name = "mood", value = 80, max = 100, min = -100 }
]
```

## Roadmap

- [ ] Parse TOML files to establish the world, story nodes, and character settings.
- [ ] Create a Minimum Viable Product (MVP) that runs in a command-line interface (CLI).
- [ ] Optimize the dialogue history and memory system.
- [ ] Develop a Graphical User Interface (GUI) to lower the barrier to entry.
- [ ] Support exporting game settings to TOML files.
- [ ] Create a platform for sharing and downloading TOML scripts.
- [ ] Provide functionality to package the game into a standalone executable.

## Step 1 Breakdown: Parsing the TOML Script

The goal of this step is to transform the `.toml` script file into data structures that the program can easily access and manipulate.

1.  **Install a TOML library:** For Python 3.11+, the built-in `tomllib` can be used. For older versions, a third-party library like `tomli` is needed. This dependency should be added to `pyproject.toml`.

2.  **Define Data Structures:** Use Python's `dataclasses` or regular classes to define the core game objects. This makes the code cleaner and less error-prone. Based on the TOML format, we'll need:
    *   `WorldSetting`: To store the world description, nouns, etc.
    *   `UserSetting`: To store the player's name, description, and initial status.
    *   `StoryNode`: To store node descriptions, next nodes, conditions, etc.
    *   `Character`: To store NPC names, descriptions, and statuses.
    *   `GameData`: A top-level container to hold all the above objects.

3.  **Implement Loading and Parsing:** Create a function like `load_game_from_toml(file_path)` that reads the TOML file and uses the chosen library to parse it into a Python dictionary.

4.  **Map Dictionary to Data Structures:** Create a converter function that takes the dictionary from the previous step and populates the data classes defined in step 2. This is also the stage to perform data validation to ensure all required fields are present and correctly formatted.

5.  **Integrate and Test:** In `main.py`, call the `load_game_from_toml()` function with a sample TOML file. Print the contents of the resulting `GameData` object to verify that all data has been loaded correctly.