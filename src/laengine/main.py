import toml_loader


def main():
    print("Hello from laengine!")
    toml_loader.load_game_from_toml("./examples/example.toml")


if __name__ == "__main__":
    main()
