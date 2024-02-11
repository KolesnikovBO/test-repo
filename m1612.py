
u = int(input('Введите скорость: '))
t = int(input('Введите время в часах: '))

ut = u*t
raz = ut//109
KM = ut - 109*raz
print('Отметка КМ ', KM)

