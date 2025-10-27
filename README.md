# LaEngine

[中文版本](./README_zh.md)

LaEngine is a game engine designed for creating text-based adventure games (AVG) powered by Large Language Models (LLMs).

## Core Features

LaEngine uniquely combines "Story Nodes" with "LLM-Generated Dialogue". This design ensures a stable main storyline while giving players the freedom to interact with the game world limitlessly, leading to a unique experience every time you play.

## TOML Script Format (Tentative)

The core elements of the game—such as plot, world-building, and characters—are defined in a simple, human-readable TOML file.

```toml
# Game Title
title = "Game Name"

# World Setting
[world_setting]
# A macro description of this world
descript = ""
# Proper nouns in the game to help the LLM generate more accurate content
nouns = ""

# Player Character Setting
[user_setting]
# Player's name
name = ""
# Player's backstory or description
descript = ""
# Player's status values
status = ["health", "money", "atk"]

# Story Node: wake_up
[node.wake_up]
type = "node"
# Scene description for this node
descript = "You wake up from your bed, sunlight streaming through the window."
# Possible next nodes
next_node = ["a_node", "b_node"]
# Conditions to trigger the next node
next_condition = ["Player walks out the door", "Player chooses to end the game"]
# Maximum number of interactions in this node
max_turn = 10
# Event triggered when max_turn is reached
when_max_turn = "Mom urges the player"

# NPC: Mom
[chara.mom]
type = "chara"
name = "Mom"
# Character's background or personality description
descript = "A kind but somewhat nagging mother."
# Character's status values
status = ["mood", "health"]
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