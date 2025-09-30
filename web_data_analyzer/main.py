from data_processing.file_reader import read_data
from data_processing.web_fetcher import fetch_user_data
import os

def main():
    file_path = os.path.join(os.path.dirname(__file__), "data.txt")
    try:
        file_records = read_data(file_path)
    except Exception as e:
        print("Error reading file:", e)
        return

    try:
        web_users = fetch_user_data()
    except Exception as e:
        print("Error fetching web data:", e)
        web_users = []

    print("Data from file (name, age):")
    for name, age in file_records:
        print(f" - {name}: {age}")

    print("\nUser names fetched from JSONPlaceholder:")
    for name in web_users:
        print(f" - {name}")

if __name__ == "__main__":
    main()
