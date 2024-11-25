users: list = [
    {'name': 'Amelia', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Poznań'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Toruń'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Łódź'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Kielce'},
    {'name': 'Żerom', 'posts': 11, 'city': 'Katowice'},
    {'name': 'Julia', 'posts': 15, 'city': 'Wrocław'},
    {'name': 'Ola', 'posts': 11, 'city': 'Radom'},
    {'name': 'Patrycja', 'posts': 20, 'city': 'Lublin'},
    {'name': 'Patrycja', 'posts': 5, 'city': 'Mińsk Mazowiecki'},

]

print(f'Witaj {users[0]['name']}!!')
for user in users[1:]:
    print(f'twój znajomy {user['name']} z miasta {user['city']}, opublikował {user['posts']} postów')
# for idx, _ in enumerate(users[1:]):
#     print(f'twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
