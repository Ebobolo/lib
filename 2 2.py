coast = float(1)
rub = 0,89

while int(coast) != 0:
  coast = float(input('Введите стоимость товара  доллорах: '))
  rub = round((coast * 1.25) * 100, 2)
  if coast > 0:
    print('Стоимость товара в рублях составила:', rub)
    break