# Gemini Project Guide: LaEngine

本文件提供 Gemini AI 助理關於如何協助 LaEngine 專案開發的指引。

## 1. 專案簡介

LaEngine 是一個使用 Python 開發、基於大型語言模型（LLM）的文字冒險遊戲（AVG）引擎。它使用 TOML 檔案來定義遊戲劇本。

## 2. 專案結構

-   `pyproject.toml`: 管理專案的元數據和依賴項。請使用 `uv` 來安裝與管理。
-   `main.py`: 應用程式的主要進入點。
-   `*.toml`: 遊戲劇本檔案，用於定義世界觀、角色和劇情節點。
-   `README.md` / `README_zh.md`: 專案說明文件。當新增功能時，請保持這兩個檔案的同步更新。

## 3. 開發工作流程

開發計畫已明列於 `README.md` 的 `Roadmap` (開發藍圖) 中。請隨時參考該處以了解下一步的開發方向。

**當前任務：第一步 - 解析 TOML 檔案**

詳細步驟請參考 `README.md` 中的「第一步拆解」：

1.  **安裝依賴項：** 如果 Python 版本低於 3.11，需要將 `tomli` 加入 `pyproject.toml`。
2.  **定義資料結構：** 在一個新檔案中 (例如 `engine/data_models.py`)，為 `WorldSetting`, `UserSetting`, `StoryNode`, `Character`, 和 `GameData` 建立 dataclass。
3.  **實作讀取器：** 在一個新檔案中 (例如 `engine/toml_loader.py`)，建立 `load_game_from_toml(file_path)` 函式。
4.  **對應資料：** 實作將解析後的字典對應到 dataclass 的邏輯。
5.  **在 `main.py` 中測試：** 使用 `main.py` 來測試讀取流程並印出結果以進行驗證。

## 4. 編碼慣例

-   **語言：** Python
-   **風格：** 遵循 PEP 8 指導原則。
-   **型別提示：** 所有函式簽名和變數都應使用型別提示 (Type Hints)。
-   **資料結構：** 優先使用 `@dataclass` 來定義資料物件。
-   **模組化：** 為不同的功能建立獨立的檔案和模組（例如，一個模組放資料模型，另一個放 TOML 讀取器），避免將所有程式碼都放在 `main.py` 中。

## 5. 如何執行

本專案可直接使用 Python 解譯器執行。

```bash
# 安裝/更新依賴項
uv pip install -r requirements.txt

# 執行主程式
python main.py
```

## 6. 如何測試

(目前尚未設定測試框架)

當新增功能時，請一併加入對應的單元測試。我們可以使用 `unittest` 或 `pytest` 框架，並將測試檔案建立在 `tests/` 目錄下。
