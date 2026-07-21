from extract import extract_data
from load import load_raw_data
from transform import transform_data
from load import load_processed_data

def main():
    users = extract_data()
    load_raw_data(users, "data/raw/users.json")
    users_df = transform_data(users)
    load_processed_data(users_df, "data/processed/users.parquet")
    print("Pipeline finished")
    

if __name__=="__main__":
    main()