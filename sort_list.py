import os
from os import path
# open file and read in movie names
f = open("movie_list.txt", "r")

movie_list = f.readlines()

print(len(movie_list))

# sort movie list
sorted_movie_list = sorted(movie_list)

# clear file and write movies in order
print(len(sorted_movie_list))
out = open("output.txt", "w+")

for movie in sorted_movie_list:
    out.write(movie)

f.close()
out.close()


