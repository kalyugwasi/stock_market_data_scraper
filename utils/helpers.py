import pandas as pd
import os

def save_data(df, filepath):
    """
    Saves a Pandas DataFrame to a CSV file.
    Creates directories if they don't exist.
    """
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Data saved to: {filepath}")

# You can add more helper functions here later
#u
