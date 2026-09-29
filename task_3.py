world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
country = 'Италия'
world_champions [2022] = 'Аргентина'
for i, j in world_champions.items():
    print (i, '-', j)
if 'Италия' in world_champions.values():
    print ('Италия становилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')