from extract import extract_data
from load import load_raw_data
from transform import transform_data

def main():
    users = extract_data()
    load_raw_data(users, "data/raw/users.json")
    users_df = transform_data(users)
    print(users_df.columns)


if __name__=="__main__":
    main()