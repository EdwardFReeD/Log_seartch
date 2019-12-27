import os
import datetime


text = 'usu'
path = r"C:\Users\grachev.ea\Desktop\1"
file_list = os.listdir(path)
full_list = [os.path.join(path, i) for i in file_list]
time_sorted_list = sorted(full_list, key=os.path.getmtime)
time_sorted_list.reverse()

data = '13-12-2019'
data = str(data).split('-')
data1 = data[2]
data2 = data[1]
data3 = data[0]
data = data1 + '-' + data2 + "-" + data3
file = []


for i in time_sorted_list:
    if ".txt" in str(i).lower() or ".log" in str(i).lower() or  ".xml" in str(i).lower()\
            or  ".doc" in str(i).lower() or  ".docx" in str(i).lower():

        watch = datetime.datetime.fromtimestamp(os.path.getmtime(i))

    if self.checkBox.isChecked():
        watc = str(watch).split(' ')
        if str(watch[0]) == data:
            file.append(watc[0] + ' ' + watc[1] + ' | ' + i)
    else:
        file.append(str(watch) + ' | ' + i)

if file == []:
    return QMessageBox.warning(self, "Ошибка", '\nФайлы с имеющимися форматами не найдены!')
if file_data == []:
    return QMessageBox.warning(self, "Ошибка", '\nФайлы с имеющимися форматами или\n файлы за указанную дату не найдены!')


dd = []

if file != []:
    for i in range(len(file)):
      dd.append(i)
    d = dd[-1] + 1

file = str(file).split(" | ")

print(file)
c = 1
seartch_file = []
for i in dd:
    clvo_pov = 0
    with open(file[c], "r", encoding='utf-8') as file:
        for line in file:
            if str(text).lower() in str(line).lower():
                    clvo_pov += 1
                    self.listWidget.addItem()
    c += 1



print(file)
print(file_data)