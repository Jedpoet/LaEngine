# LaEngine

[English Version](./README.md)

LaEngine 是一個專為開發基於大型語言模型（LLM）的文字冒險遊戲（AVG）所設計的遊戲引擎。

## 核心特色

LaEngine 的核心為一個混合式架構，它將遊戲結構清晰地劃分為 **場景 (Scenes)** 與 **劇情節點 (Story Nodes)**。**場景** 扮演著定義環境氛圍的「舞台」角色，而 **劇情節點** 則是事件、對話與選擇的「劇本」。這種架構為開發者提供了清晰的藍圖，能同時支援以地點為中心的探索玩法，以及在單一場景中展開的複雜分支敘事。

## TOML 劇本格式（暫定）

遊戲的劇情、世界觀與角色等核心元素，都將透過簡單易讀的 TOML 檔案進行定義。

## 專案結構

- `pyproject.toml`: 管理專案的元數據和依賴項。請使用 `uv` 來安裝與管理。
- `src/laengine/main.py`: 應用程式的主要進入點。
- `src/laengine/data_models.py`: 定義遊戲資料結構 (dataclasses)。
- `src/laengine/toml_loader.py`: 負責讀取和解析 TOML 遊戲劇本檔案。
- `examples/*.toml`: 遊戲劇本檔案，用於定義世界觀、角色和劇情節點。
- `README.md` / `README_zh.md`: 專案說明文件。當新增功能時，請保持這兩個檔案的同步更新。

```toml
# 遊戲標題
title = "高級混合模型範例 - 限時拆彈"

#------------------------------------------------------------------------------
#  全域設定 (Global Settings)
#------------------------------------------------------------------------------

[world_setting]
descript = "一個充滿未來科技感的世界。"

[variables]
# 記錄炸彈是否已被拆除
bomb_disarmed = false

#------------------------------------------------------------------------------
#  玩家設定 (Player Settings)
#------------------------------------------------------------------------------

[user_setting]
name = "探員"
# 玩家的狀態值
status = [
  { name = "anxiety", value = 30, max = 100, min = 0 }
]

#------------------------------------------------------------------------------
#  角色定義 (Character Definitions)
#------------------------------------------------------------------------------
[[characters]]
id = "unit734"
name = "U-734"
descript = "房間中央的全息投影 AI 助理。"
# 角色的扮演指南
personality = "以單調、邏輯、機械的語氣說話。只提供數據，不提供情感支持。在情況緊急時，會重複關鍵指令。"
# 角色也可以有自己的狀態
status = [
  { name = "operational_integrity", value = 100, max = 100, min = 0 }
]


#------------------------------------------------------------------------------
#  地點定義 (Scene Definitions)
#------------------------------------------------------------------------------

[[scenes]]
id = "locked_room"
descript = "一個冰冷的金屬房間，沒有門窗。牆上的一個巨大螢幕顯示著不祥的紅色倒數計時。"
# 場景的氛圍，可以影響音樂、UI 或 LLM 的語氣
atmosphere = "緊急, 幽閉, 緊張"

# 當進入此場景時，玩家只有 5 個回合（行動次數）的時間
max_turn = 5
# 時間耗盡後，強制跳轉到指定的劇情節點
when_max_turn = "bomb_explodes"

# 劇情入口
story_triggers = [
  # 遊戲開始或進入此房間時，自動觸發 "start_scenario"
  { on_event = "enter", start_node = "start_scenario" }
]

#------------------------------------------------------------------------------
#  劇情樹 (Story Tree)
#------------------------------------------------------------------------------

[[story_nodes]]
id = "start_scenario"
descript = "你的大腦一陣暈眩後恢復了意識。AI U-734 的聲音響起：『探員，歡迎回來。情況分析：偵測到一枚即將引爆的炸彈。建議立即處理。』"
choices = [
  { text = "「U-734，報告情況。」", goto = "ai_report" },
  { text = "直接衝向炸彈進行檢查", goto = "inspect_bomb" }
]

[[story_nodes]]
id = "ai_report"
descript = "『倒數計時結束後，炸彈將引爆。根據掃描，拆除需要剪斷三條引線中的一條。錯誤的選擇將導致立即引爆。』"
# 只有 LLM 可見的隱藏描述，用於豐富生成內容
hide_descript = "AI 的全息投影閃爍了一下，似乎在暗示有什麼資訊沒有直接說出來。"
choices = [
  { text = "「哪三條引線？」", goto = "inspect_bomb" },
  { text = "「你有什麼建議？」", goto = "ai_suggestion" }
]

[[story_nodes]]
id = "ai_suggestion"
descript = "『我的數據庫中缺少關於此型號炸彈的關鍵資訊。但是，熱掃描顯示藍色引線的溫度略高於其他兩條。』"
choices = [
  { text = "檢查炸彈", goto = "inspect_bomb" }
]

[[story_nodes]]
id = "inspect_bomb"
descript = "你來到炸彈前，打開了面板。裡面有三條線：紅色、黃色和藍色。你必須做出選擇。"
# 劇情效果：增加玩家的焦慮值
on_enter = { set_status = "anxiety", to = 70 }
choices = [
  { text = "剪斷紅色引線", goto = "bomb_explodes" },
  { text = "剪斷黃色引線", goto = "bomb_explodes" },
  { text = "剪斷藍色引線", goto = "disarm_success" }
]

[[story_nodes]]
id = "disarm_success"
descript = "你用顫抖的手剪斷了藍色引線。倒數計時停止了。U-734 的聲音響起：『威脅已解除。做得好，探員。』"
# 劇情效果：更新全域變數和玩家狀態
on_enter = [
    { set_variable = "bomb_disarmed", to = true },
    { set_status = "anxiety", to = 10 }
]
choices = [
  { text = "（癱倒在地）" }
]

[[story_nodes]]
id = "bomb_explodes"
# 這個節點沒有描述，因為爆炸後遊戲就結束了
hide_descript = "當玩家選擇錯誤或時間耗盡時，會跳轉到這裡。這是一個失敗結局。"
# 劇情效果：將焦慮值設為最大
on_enter = { set_status = "anxiety", to = 100 }
# 遊戲結束標記，引擎看到後會結束遊戲
game_over = true
choices = []
```

## 開發藍圖 (TODO)

- [x] 讀取 TOML 檔案並建立世界觀、劇情節點與角色設定 (已在 `data_models.py` 中使用型別提示定義資料結構)
- [ ] 建立可在終端機 (CLI) 執行的最小可行性產品 (MVP)
- [ ] 優化對話歷史與記憶系統
- [ ] 開發圖形化使用者介面 (GUI) 以降低使用門檻
- [ ] 支援將遊戲設定導出為 TOML 檔案
- [ ] 建立一個分享與下載 TOML 劇本的平台
- [ ] 提供將遊戲打包成獨立執行檔的功能

## 安裝與使用

本專案使用 `uv` 來管理虛擬環境與依賴項。`uv` 會讀取 `pyproject.toml` 檔案來確保開發環境的一致性。

### 1. 環境設定

如果您尚未安裝 `uv`，請參考 [uv 官方文件](https://github.com/astral-sh/uv) 進行安裝。

### 2. 執行遊戲引擎

推薦使用 `uv run` 指令來執行主程式。這個指令會自動使用虛擬環境中的 Python，並確保所有依賴項都已安裝：

```bash
uv run src/laengine/main.py
```

### 3. 管理依賴項

若要為專案加入新的套件，請使用 `uv add` 指令。`uv` 會自動將套件安裝到虛擬環境，並更新 `pyproject.toml` 和 `uv.lock` 檔案。

```bash
uv add <package_name>
```

## 第一步拆解：解析 TOML 劇本

此步驟的目標是將 `.toml` 劇本檔案的內容，轉換成程式內部可以輕易取用和操作的資料結構。

1.  **安裝 TOML 解析函式庫：** Python 3.11 以上版本內建了 `tomllib`。若為舊版，則需安裝如 `tomli` 的第三方函式庫，並將其加入 `pyproject.toml`。（已使用python 3.14）

2.  **定義資料結構：** (已在 `data_models.py` 中完成) 使用 Python 的 `dataclasses` 來定義核心遊戲物件並加入型別提示。這將使程式碼更清晰且不易出錯。根據 TOML 格式，我們需要：
    *   `WorldSetting`: 存放世界觀描述、專有名詞。
    *   `UserSetting`: 存放玩家姓名、描述、初始狀態。
    *   `StoryNode`: 存放劇情節點描述、下一個節點、觸發條件等。
    *   `Character`: 存放 NPC 姓名、描述、狀態。
    *   `GameData`: 一個頂層容器，用來存放所有遊戲資料。

3.  **實作讀取與解析：** 建立一個函式如 `load_game_from_toml(file_path)`，讀取 TOML 檔案並將其內容解析成 Python 字典。

4.  **將字典對應到資料結構：** 建立一個轉換函式，接收上一步的字典，並將其內容填入第二步定義的資料類別中。此階段需進行資料驗證，確保欄位無遺漏且格式正確。

5.  **整合與測試：** 在 `main.py` 中呼叫 `load_game_from_toml()`，並印出載入完成的 `GameData` 物件內容，以確認資料讀取無誤。
