# LaEngine

[English Version](./README.md)

LaEngine 是一個專為開發基於大型語言模型（LLM）的文字冒險遊戲（AVG）所設計的遊戲引擎。

## 核心特色

LaEngine 獨創地結合了「劇情節點」與「LLM 生成對話」兩種模式。這種設計不僅確保了遊戲擁有穩定的主線劇情架構，同時也賦予玩家與遊戲世界無限互動的自由，帶來每一次都獨一無二的遊戲體驗。

## TOML 劇本格式（暫定）

遊戲的劇情、世界觀與角色等核心元素，都將透過簡單易讀的 TOML 檔案進行定義。

```toml
# 遊戲標題
title = "遊戲名稱"

# 世界觀設定
[world_setting]
# 關於這個世界的宏觀描述
descript = ""
# 遊戲中的專有名詞，幫助 LLM 更精準地生成內容
nouns = ""

# 玩家角色設定
[user_setting]
# 玩家姓名
name = ""
# 玩家的背景故事或描述
descript = ""
# 玩家的狀態值
status = ["health", "money", "atk"]

# 劇情節點：醒來
[node.wake_up]
type = "node"
# 此節點的場景描述
descript = "你從床上醒來，陽光從窗戶灑進房間。"
# 可能的下一個節點
next_node = ["a_node", "b_node"]
# 觸發下一個節點的條件
next_condition = ["玩家走出房門", "玩家選擇結束遊戲"]
# 在此節點的最大互動次數
max_turn = 10
# 到達最大次數時觸發的事件
when_max_turn = "媽媽催促玩家"

# NPC 角色：媽媽
[chara.mom]
type = "chara"
name = "媽媽"
# 角色的背景或性格描述
descript = "一位慈祥但有點嘮叨的母親。"
# 角色的狀態值
status = ["mood", "health"]
```

## 開發藍圖 (TODO)

- [ ] 讀取 TOML 檔案並建立世界觀、劇情節點與角色設定
- [ ] 建立可在終端機 (CLI) 執行的最小可行性產品 (MVP)
- [ ] 優化對話歷史與記憶系統
- [ ] 開發圖形化使用者介面 (GUI) 以降低使用門檻
- [ ] 支援將遊戲設定導出為 TOML 檔案
- [ ] 建立一個分享與下載 TOML 劇本的平台
- [ ] 提供將遊戲打包成獨立執行檔的功能

## 第一步拆解：解析 TOML 劇本

此步驟的目標是將 `.toml` 劇本檔案的內容，轉換成程式內部可以輕易取用和操作的資料結構。

1.  **安裝 TOML 解析函式庫：** Python 3.11 以上版本內建了 `tomllib`。若為舊版，則需安裝如 `tomli` 的第三方函式庫，並將其加入 `pyproject.toml`。

2.  **定義資料結構：** 使用 Python 的 `dataclasses` 或一般類別來定義遊戲物件，例如：
    *   `WorldSetting`: 存放世界觀描述、專有名詞。
    *   `UserSetting`: 存放玩家姓名、描述、初始狀態。
    *   `StoryNode`: 存放劇情節點描述、下一個節點、觸發條件等。
    *   `Character`: 存放 NPC 姓名、描述、狀態。
    *   `GameData`: 一個頂層容器，用來存放所有遊戲資料。

3.  **實作讀取與解析：** 建立一個函式如 `load_game_from_toml(file_path)`，讀取 TOML 檔案並將其內容解析成 Python 字典。

4.  **將字典對應到資料結構：** 建立一個轉換函式，接收上一步的字典，並將其內容填入第二步定義的資料類別中。此階段需進行資料驗證，確保欄位無遺漏且格式正確。

5.  **整合與測試：** 在 `main.py` 中呼叫 `load_game_from_toml()`，並印出載入完成的 `GameData` 物件內容，以確認資料讀取無誤。
