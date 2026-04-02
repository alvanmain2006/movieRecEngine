import pandas as pd
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.") # check if the file exists before loading 
    
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        raise e

if __name__ == "__main__":

    dir = "data/raw/ml-latest-small/"
    links_file = os.path.join(dir, "links.csv")
    movies_file = os.path.join(dir, "movies.csv")
    ratings_file = os.path.join(dir, "ratings.csv")
    tags_file = os.path.join(dir, "tags.csv")

    link_df = load_data(links_file)
    movies_df = load_data(movies_file)
    ratings_df = load_data(ratings_file)
    tags_df = load_data(tags_file)
    print(link_df.head())  # Print the first few rows of the loaded data

    # dir = "data/raw/ml-latest-small/"
    # links_file = os.path.join(dir, "links.csv")
    # movies_file = os.path.join(dir, "movies.csv")
    # ratings_file = os.path.join(dir, "ratings.csv")
    # tags_file = os.path.join(dir, "tags.csv")
    
    # files = ["links.csv", "movies.csv", "ratings.csv", "tags.csv"]
    # df_list = [None] * len(files)
    # for i, file in enumerate(files):
    #     file_path = os.path.join(dir, file)
    #     if not os.path.exists(file_path):
    #         print(f"Warning: The file {file} does not exist in the directory {dir}. Please check the path and try again.")
    #     else:
    #         df_list[i] = load_data(file_path)

    # print(df_list[0].head())