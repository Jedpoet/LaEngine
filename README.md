# LaEngine

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
