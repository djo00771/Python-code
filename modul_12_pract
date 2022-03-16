text = "Вы хотите расчитать % по вкладу?, введите да/нет!: "
active = True
while active:
    capital = input(text)
    if capital == 'да':
        print('Ну что ж....')
        break
    else:
        print(f"{capital} Подумайте еще раз!")
money = int(input('Введите сумму вклада: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for i in per_cent:
    deposit.append(per_cent[i] * money / 100)
max_deposit = max(deposit)
min_deposit = min(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать: " + str(max_deposit))
print("Минимальная сумма, которую вы можете заработать: " + str(min_deposit))
