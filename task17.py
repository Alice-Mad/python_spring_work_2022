# #todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
# Цены хранятся в словаре:
# prices = {
#   "banana": 4,
#   "apple": 2,
#   "orange": 1.5,
#   "pear": 3
# }
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
summ = float()
for key, val in prices.items():
  summ = summ + float(val)
print("Total cost of all purchases is", summ)
