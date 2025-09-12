import csv
import os

# #creating the genre hash map
# def genre_mapping(path=r".\Data\raw\u.genre"):
#     genre_map = {}
    
#     with open(path, 'r') as f :
#         for line in f:
#             if line.strip():
#                 x = line.strip().split('|')
#                 genre_map[int(x[1])] = x[0]
#     print(genre_map)
#     return genre_map

# #parse the item file and create a movies.csv file
# def create_movies_file():
#     genre_map = genre_mapping()
#     #items column names
#     columns = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL']
#     genre_cols = []
#     for i in range(len(genre_map)):
#         genre_cols[i] = genre_map[i]
    
#     columns.extend(genre_cols)
    
#     return columns

# x = create_movies_file()
# print(x)
    
def genre_list_creator(file='Data/raw/u.genre'):
    genre_list = []
    with open(file, 'r') as f:
        for line in f:
            genre , idx = line.strip().split('|')
            genre_list.insert(int(idx),genre)
    return genre_list

#extracting the genre file
def extract_genre_file(input_path='./Data/raw/u.genre', output_path='./Data/extracted/genre.csv'):
    with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['genre', 'index'])  # Header

        for line in infile:
            if line.strip():
                genre, idx = line.strip().split('|')
                writer.writerow([genre, idx])
                

#extracting the items file
def extract_item_file(input_path='./Data/raw/u.item', output_path='./Data/extracted/movies.csv'):
    with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
        genre_list = genre_list_creator()
        writer = csv.writer(outfile)
        writer.writerow(['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL']+genre_list)
        
        for line in infile:
            writer.writerow(line.strip().split('|'))

#extracting the data file
def extract_data_file(input_path='./Data/raw/u.data', output_path='./Data/extracted/ratings.csv'):
    with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['user_id', 'movie_id', 'rating', 'timestamp'])
        
        for line in infile:
            writer.writerow(line.strip().split('\t'))

extract_genre_file()            
extract_item_file()
extract_data_file()