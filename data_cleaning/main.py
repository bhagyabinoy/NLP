import pandas as pd
import json

try:
    
    df = pd.read_csv('movies.csv')
    genres = df['genres'].apply(json.loads)
    data_list = []
    for genre_list in genres:
        for genre in genre_list:
            data_list.append([genre['id'], genre['name']])
    genre_df = pd.DataFrame(data_list, columns=['Id', 'Name'])
    genre_df.to_csv('movies_cleaned.csv', index=False)
    print("Success: Dataset cleaned and saved as 'movies_cleaned.csv'.")

except FileNotFoundError:
    print("Error: File 'movies.csv' not found.")
except (KeyError, json.JSONDecodeError):
    print("Error: Failed to parse the file.")
except Exception as e:
    print("An unexpected error occurred:", str(e))

