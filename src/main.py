from extract import extract_data
from load import load_raw_data

def main():
    users = extract_data()
    load_raw_data(users, "data/raw/users.json")
    print("data loaded")


if __name__=="__main__":
    main()