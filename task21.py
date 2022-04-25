# #todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# # заполненный шаблон записать в файл index.html
#
page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}
template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">

  <p>?</p>

 </body>
</html>
"""
f = open("text.txt", mode="w")
f.write(template)
f.close()
new_line = str()
flag = int()
g = str()
f = open("text.txt")
while True:
    line = f.readline()
    if line == "":
        break
    line = line[0:(len(line) - 1)]
    for j in line:
        if j == "?":
            flag = 1
    if flag == 0:
        print(line)
        continue
    for key, val in page.items():
        i = 0
        while True:
            h = 0
            if line[i:(i+len(key))] == key:
                for k in line:
                    if k == "?":
                        new_line = line[0:h] + val + line[h+1:]
                    h += 1
                print(new_line)
                break
            if i >= len(line):
                break
            i += 1
f.close()
