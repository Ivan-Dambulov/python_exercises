from math import floor

korab_shirina = float(input())
korab_duljina = float(input())
korab_visochina = float(input())
sredna_visochina_astronavt = float(input())


korab_obem = korab_visochina * korab_duljina * korab_shirina
staia_obem = (sredna_visochina_astronavt + 0.4) * 2 * 2
broi_choveka = floor(korab_obem / staia_obem)

if 3 <= broi_choveka <= 10:
    print(f'The spacecraft holds {broi_choveka} astronauts.')

elif broi_choveka < 3:
    print('The spacecraft is too small.')

else:
    print('The spacecraft is too big.')

