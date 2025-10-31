import data_models


def load_game_from_toml(file_path):
    # TODO:
    # 讀取toml並輸出，測試是否有全部讀取
    # 將讀取到的資料填入dataclass裡面
    print("lunch loader")
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
