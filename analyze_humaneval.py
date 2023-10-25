import json
import os
import fire


def jsonl_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

def clear_terminal():
    os.system('clear')  # For Linux/Mac
    # os.system('cls')  # For Windows

def main(path=""):
    jsonl_file_path = path
    print("\033[1m\033[94mJSONL Data Viewer\033[0m")

    for data in jsonl_generator(jsonl_file_path):
        clear_terminal()
        print("\033[1m\033[92mDictionary\033[0m")
        for key, value in data.items():
            print("\033[1m\033[94m================\033[0m")
            if isinstance(value, list):
                print("\033[1m\033[91m-----------------\033[0m")
                for item in value:
                    print(f"\033[0m {item}")
            else:
                print(f"\033[96m{key}:\033[0m {value}")

        input("\033[1m\033[93mPress Enter to continue to the next dictionary...\033[0m")


if __name__ == '__main__':
    fire.Fire(main)
