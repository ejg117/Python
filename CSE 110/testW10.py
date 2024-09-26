# print()
# movies= []
# movies = [
#      'Batman Begins', 
#      'Hulk'
#      ]
# votes = [
#    14,
#    1
# ]

# movies.append('Dune')
# votes.append(7)

# #region 

# # print('Movies by index')
# # for i in range(len(movies)):
# #     print(f'{i} - {movies[i]}')
# # removed=movies.pop(1)
# # # print('Movies:')
# # # for movie in movies: 
# # #     print(f'\t-{movie}')
# # for movie in movies:
# #  print(f'\t- {movie}')

# # print('Movies after changes:')
# # for i in range(len(movies)):
# #     print(f'{i} - {movies[i]}')
# # #Removing items from a list
# # #Remove must have an exact match of a value in the list to sucessfully remove the item
# # #movies.remove('Dune')
# # #Pop removes items based on index
 
# # #Edit a existing item
# #  movies[0] = 'Dark Knight Rises'

# #  #movies.insert(1, 'Mission Impossible') #append might use this: movies.insert(len(movies), "last")
# #endregion 
# print('movies after changes:')
# vote_sum = 0
# for i in range(len(movies)):
#     print(f'{i} - {movies[i]} = {votes[i]}')
# vote_sum += votes[i]

# print(f'Total votes: {vote_sum}')