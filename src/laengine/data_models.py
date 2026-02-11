from dataclasses import dataclass
from typing import Any, Type, TypeVar

# TypeVar 用於泛型型別提示，表示 'T' 是一個 Dataclass 類型
T = TypeVar("T")


# 輔助函式
def dict_to_dataclass(data: dict[str, Any], dataclass_type: Type[T]) -> T:
    """將字典轉換為給定的 dataclass 類型實例"""
    # 這是處理簡單且欄位名稱完全匹配的轉換
    return dataclass_type(**data)


# 世界觀
@dataclass
class WorldSetting:
    description: str  # 世界觀描述
    nouns: dict[str, str]  # 專有名詞解釋


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
    description: str
    personality: str  # 給LLM更好模擬NPC性格的prompt
    status: dict[str, Any]  # NPC 狀態欄


# 場景設定
@dataclass
class Scene:
    id: str
    name: str
    description: str
    atmosphere: str  # 給LLM更好營造場景氛圍的promopt
    objs: dict[str, Any]  # 可互動的物件
    story_triggers: dict[str, Any]  # 進入場景時的劇情觸發器


# 故事節點設定
@dataclass
class StoryNode:
    id: str
    name: str
    description: str
    hidden_description: str  # 給LLM提供的隱藏資訊，玩家一開始不知
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

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        # TODO: 讀取並轉換
        #  傳回 GameData 實例
        return cls(
            world=world, var=var, user=user, charas=charas, scenes=scenes, nodes=nodes
        )


@dataclass
class GameState:
    game: GameData
    now_scene: Scene
    now_node: StoryNode

    def save_game(self, path: str):
        """將目前遊戲狀態保存到檔案"""
        pass

    @classmethod
    def load_game(cls, path: str):
        """從檔案讀取遊戲狀態"""
        pass


@dataclass
class AIResponse:
    narrative: str  # AI 講的故事
    var_change: dict[str, Any]  # 全域變數變化
    user_change: dict[str, Any]  # 玩家數值變化
