import pandas as pd

def transform_data(data):
    df = pd.json_normalize(data)
    df = df[
        [
            "id",
            "name",
            "email",
            "address.city",
            "address.zipcode",
            "company.name"
        ]
    ]

    df = df.rename(
        columns={
            "address.city": "city",
            "address.zipcode": "zipcode",
            "company.name": "company_name"
        }
    )
    
    return df