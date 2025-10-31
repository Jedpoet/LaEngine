# LaEngine

[中文版本](./README_zh.md)

LaEngine is a game engine designed for creating text-based adventure games (AVG) powered by Large Language Models (LLMs).

## Core Features

LaEngine features a hybrid design that separates game structure into **Scenes** and **Story Nodes**. **Scenes** act as the "stages" (locations) which define the environment and atmosphere, while **Story Nodes** represent the "script" of events, dialogue, and choices. This architecture provides a clear framework for developers, supporting both location-based exploration and complex, dialogue-heavy narratives within a single scene.

## TOML Script Format (Tentative)

The core elements of the game—such as plot, world-building, and characters—are defined in a simple, human-readable TOML file.

```toml
# Game Title
title = "Advanced Hybrid Model Example - Time Bomb"

#------------------------------------------------------------------------------
#  Global Settings
#------------------------------------------------------------------------------

[world_setting]
descript = "A world with a futuristic sci-fi feel."

[variables]
# Tracks whether the bomb has been disarmed
bomb_disarmed = false

#------------------------------------------------------------------------------
#  Player Settings
#------------------------------------------------------------------------------

[user_setting]
name = "Agent"
# Player's status values
status = [
  { name = "anxiety", value = 30, max = 100, min = 0 }
]

#------------------------------------------------------------------------------
#  Character Definitions
#------------------------------------------------------------------------------
[[characters]]
id = "unit734"
name = "U-734"
descript = "A holographic AI assistant in the center of the room."
# Role-playing guide for the character
personality = "Speaks in a monotone, logical, and robotic tone. Provides data but no emotional support. Repeats key instructions when the situation is critical."
# Characters can also have their own statuses
status = [
  { name = "operational_integrity", value = 100, max = 100, min = 0 }
]


#------------------------------------------------------------------------------
#  Scene Definitions
#------------------------------------------------------------------------------

[[scenes]]
id = "locked_room"
descript = "A cold, metallic room with no doors or windows. A large screen on the wall displays an ominous red countdown."
# The scene's atmosphere can influence music, UI, or the LLM's tone
atmosphere = "Urgent, Claustrophobic, Tense"

# When entering this scene, the player has only 5 turns (actions)
max_turn = 5
# After time runs out, forcibly jump to the specified story node
when_max_turn = "bomb_explodes"

# Story entry points
story_triggers = [
  # Automatically triggers "start_scenario" when the game starts or upon entering this room
  { on_event = "enter", start_node = "start_scenario" }
]

#------------------------------------------------------------------------------
#  Story Tree
#------------------------------------------------------------------------------

[[story_nodes]]
id = "start_scenario"
descript = "Your mind clears after a moment of dizziness. The voice of AI U-734 sounds: 'Agent, welcome back. Situation analysis: An active bomb has been detected. Immediate action is advised.'"
choices = [
  { text = "'U-734, report the situation.'", goto = "ai_report" },
  { text = "'Rush to inspect the bomb directly.'", goto = "inspect_bomb" }
]

[[story_nodes]]
id = "ai_report"
descript = "'The bomb will detonate when the countdown ends. Scans indicate that disarming requires cutting one of three wires. A wrong choice will lead to immediate detonation.'"
# Hidden description visible only to the LLM, used to enrich content
hide_descript = "The AI's hologram flickers for a moment, as if hinting at information not explicitly stated."
choices = [
  { text = "'Which three wires?'", goto = "inspect_bomb" },
  { text = "'What do you suggest?'", goto = "ai_suggestion" }
]

[[story_nodes]]
id = "ai_suggestion"
descript = "'My database lacks critical information on this model of bomb. However, thermal scans show the blue wire's temperature is slightly higher than the other two.'"
choices = [
  { text = "'Inspect the bomb.'", goto = "inspect_bomb" }
]

[[story_nodes]]
id = "inspect_bomb"
descript = "You approach the bomb and open its panel. Inside are three wires: red, yellow, and blue. You must make a choice."
# Story effect: Increase the player's anxiety
on_enter = { set_status = "anxiety", to = 70 }
choices = [
  { text = "'Cut the red wire.'", goto = "bomb_explodes" },
  { text = "'Cut the yellow wire.'", goto = "bomb_explodes" },
  { text = "'Cut the blue wire.'", goto = "disarm_success" }
]

[[story_nodes]]
id = "disarm_success"
descript = "With a trembling hand, you cut the blue wire. The countdown stops. U-734's voice sounds: 'Threat neutralized. Well done, Agent.'"
# Story effects: Update global variables and player status
on_enter = [
    { set_variable = "bomb_disarmed", to = true },
    { set_status = "anxiety", to = 10 }
]
choices = [
  { text = "'(Collapse on the floor)'" }
]

[[story_nodes]]
id = "bomb_explodes"
# This node has no description because the game ends after the explosion
hide_descript = "This is the failure ending, triggered when the player makes a wrong choice or runs out of time."
# Story effect: Set anxiety to maximum
on_enter = { set_status = "anxiety", to = 100 }
# Game over flag; the engine will end the game upon seeing this
game_over = true
choices = []
```

## Roadmap

- [x] Parse TOML files to establish the world, story nodes, and character settings. (Data structures defined with type hints in `data_models.py`)
- [ ] Create a Minimum Viable Product (MVP) that runs in a command-line interface (CLI).
- [ ] Optimize the dialogue history and memory system.
- [ ] Develop a Graphical User Interface (GUI) to lower the barrier to entry.
- [ ] Support exporting game settings to TOML files.
- [ ] Create a platform for sharing and downloading TOML scripts.
- [ ] Provide functionality to package the game into a standalone executable.

## Step 1 Breakdown: Parsing the TOML Script

The goal of this step is to transform the `.toml` script file into data structures that the program can easily access and manipulate.

1.  **Install a TOML library:** For Python 3.11+, the built-in `tomllib` can be used. For older versions, a third-party library like `tomli` is needed. This dependency should be added to `pyproject.toml`.

2.  **Define Data Structures:** (Completed in `data_models.py`) Use Python's `dataclasses` to define the core game objects with type hints. This makes the code cleaner and less error-prone. Based on the TOML format, we'll need:
    *   `WorldSetting`: To store the world description, nouns, etc.
    *   `UserSetting`: To store the player's name, description, and initial status.
    *   `StoryNode`: To store node descriptions, next nodes, conditions, etc.
    *   `Character`: To store NPC names, descriptions, and statuses.
    *   `GameData`: A top-level container to hold all the above objects.

3.  **Implement Loading and Parsing:** Create a function like `load_game_from_toml(file_path)` that reads the TOML file and uses the chosen library to parse it into a Python dictionary.

4.  **Map Dictionary to Data Structures:** Create a converter function that takes the dictionary from the previous step and populates the data classes defined in step 2. This is also the stage to perform data validation to ensure all required fields are present and correctly formatted.

5.  **Integrate and Test:** In `main.py`, call the `load_game_from_toml()` function with a sample TOML file. Print the contents of the resulting `GameData` object to verify that all data has been loaded correctly.