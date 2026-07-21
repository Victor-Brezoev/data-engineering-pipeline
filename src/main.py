from extract import extract_data

def main():
    users = extract_data()
    print(f"extract {len(users)} users")
    print(users[0])


if __name__=="__main__":
    main()