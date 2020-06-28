#b-ifelse.py

friend = 'สมศรี'

print('เงื่อนไข 1:', friend == 'John')
print('เงื่อนไข 2:', friend == 'Chon')

if friend == 'John':
    print('Hi, ' + friend)
elif friend == 'Chon':
    print('Hello, ' + friend)
elif friend == 'สมศรี':
    print('Obasan ' + friend)
else:
    print('Who are you')