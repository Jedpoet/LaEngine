import laengine.data_models as data_models
import tomllib
import logging as log


def load_game_from_toml(file_path: str) -> data_models.GameData:
    """
    讀取 TOML 檔案並將其轉換為 GameData 實例。
    """
    log.info("Launching toml loader")
    try:
        with open(file_path, "rb") as file:
            data = tomllib.load(file)
            log.debug(f"Loaded raw data: {data}")
            
            # 使用 GameData.from_dict 進行結構化轉換
            game_data = data_models.GameData.from_dict(data)
            return game_data

    except FileNotFoundError:
        log.error(f"Error: The file {file_path} was not found.")
        raise
    except Exception as e:
        log.error(f"An error occurred during TOML loading: {e}")
        raise
