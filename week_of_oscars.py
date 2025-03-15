movie_name = input()
room_type = input()
number_of_tickets = int(input())

prihodi = ''

if movie_name == 'A Star Is Born':
    if room_type == 'normal':
        prihodi = number_of_tickets * 7.5
    if room_type == 'luxury':
        prihodi = number_of_tickets * 10.5
    if room_type == 'ultra luxury':
        prihodi = number_of_tickets * 13.5

if movie_name == 'Bohemian Rhapsody':
    if room_type == 'normal':
        prihodi = number_of_tickets * 7.35
    elif room_type == 'luxury':
        prihodi = number_of_tickets * 9.45
    elif room_type == 'ultra luxury':
        prihodi = number_of_tickets * 12.75

if movie_name == 'Green Book':
    if room_type == 'normal':
        prihodi = number_of_tickets * 8.15
    elif room_type == 'luxury':
        prihodi = number_of_tickets * 10.25
    elif room_type == 'ultra luxury':
        prihodi = number_of_tickets * 13.25

if movie_name == 'The Favourite':
    if room_type == 'normal':
        prihodi = number_of_tickets * 8.75
    elif room_type == 'luxury':
        prihodi = number_of_tickets * 11.55
    elif room_type == 'ultra luxury':
        prihodi = number_of_tickets * 13.95

print(f'{movie_name} -> {prihodi:.2f} lv.')