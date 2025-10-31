from dataclasses import dataclass
from typing import Any


# 世界觀
@dataclass
class WorldSetting:
    descript: str  # 世界觀描述
    noums: dict[str, str]  # 專有名詞解釋


# 全域變數
@dataclass
class Variables:
    var: dict[str, Any]


# 玩家設定
@dataclass
class UserSetting:
    user_name: str
    status: dict[str, Any]  # 玩家狀態欄


# NPC設定
@dataclass
class Character:
    id: str
    name: str
    discript: str
    personality: str  # 給LLM更好模擬NPC性格的prompt
    status: dict[str, Any]  # NPC 狀態欄


# 場景設定
@dataclass
class Scene:
    id: str
    name: str
    discript: str
    atmosphere: str  # 給LLM更好營造場景氛圍的promopt
    objs: dict[str, Any]  # 可互動的物件
    story_triggers: dict[str, Any]  # 進入場景時的劇情觸發器


# 故事節點設定
@dataclass
class StoryNode:
    id: str
    name: str
    discript: str
    hide_discript: str  # 給LLM提供的隱藏資訊，玩家一開始不知
    on_enter: dict[str, Any]  # 進入劇情節點時觸發的劇情
    choice: dict[str, Any]  # 觸發這些條件就可以進入下個節點


@dataclass
class GameData:
    world: WorldSetting
    var: Variables
    user: UserSetting
    charas: list[Character]
    scenes: list[Scene]
    nodes: list[StoryNode]
