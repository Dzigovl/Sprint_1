s = '1h 45m,360s,25m,30m 120s,2h 60s'
minutes = 0
sec = 0
for i in s.replace(',', ' ').split():
    if 'h' in i:
        minutes += int(i[:-1])*60
    elif 'm' in i:
        minutes += int(i[:-1])
    elif 's' in i:
        minutes += int(i[:-1])//60
        sec += int(i[:-1])%60
minutes = minutes + sec//60
print('Общее число минут:', minutes)