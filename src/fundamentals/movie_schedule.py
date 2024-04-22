
current_movies = {'Grinch': '08:00am',
                  'Rudolph': '09:00am',
                  'Frosty': '10:00am',
                  'XMas Vaca': '11:00am'}

print('Movies')
for key in current_movies:
    print(key)

movie = input('Movie?\n')

showtime = current_movies.get(movie)

if (not showtime):
    print('Not showing')
else:
    print(movie, 'showing at', showtime)
