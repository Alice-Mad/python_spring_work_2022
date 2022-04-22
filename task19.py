# #todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm
#
# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
# "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
# Каждое значение из списка должно находится на отдельной строке.

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori", "EM", "PageRank", "AdaBoost", "kNN",
            "Наивный байесовский классификатор", "CART"]
f = open("algoritm.csv", "w")
k = 1
for s in algoritm:
    obj = str(k) + "," + s + "\n"
    f.write(obj)
    k += 1
f.close()
