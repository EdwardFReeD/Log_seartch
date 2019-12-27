if 'directory' not in globals():
    self.progressBar.hide()
    return QMessageBox.warning(self, "Ошибка", "Не выбрана директория")

if self.lineEdit.text() == '':
    self.progressBar.hide()
    return QMessageBox.warning(self, "Ошибка", "Не указано что искать!")

if len(self.lineEdit_2.text()) < 8 or '-' not in self.lineEdit_2.text():
    self.progressBar.hide()
    return QMessageBox.warning(self, "Ошибка", "Указана не корректная дата!")

self.progressBar.show()
text = self.lineEdit.text()
text = chardet.detect(text)
files = os.listdir(directory)

value = 0
self.progressBar.setProperty("value", value)
self.listWidget.clear()

director = (str(directory) + '/')
data = self.lineEdit_2.text()
data = str(data).split('-')
data1 = data[2]
data2 = data[1]
data3 = data[0]
data = data1 + '-' + data2 + "-" + data3
file = []
file_data = []

if self.checkBox.isChecked():
    try:
        value1 = []
        value2 = 100
        for i in files:
            if ".txt" in str(i).lower() or ".rtf" in str(i).lower() or ".doc" in str(i).lower() or ".docx" in str(
                    i).lower() \
                    or ".html" in str(i).lower() \
                    or ".odt" in str(i).lower() or ".xlsx" in str(i).lower() or ".xml" in str(i).lower() \
                    or ".py" in str(i).lower() or ".log" in str(i).lower():
                file.append(i)
        if file == []:
            return QMessageBox.warning(self, "Ошибка", '\nФайлы с имеющимися форматами не найдены!')
        for i in file:

            watch = datetime.datetime.fromtimestamp(os.path.getmtime(director + i))
            watch = str(watch).split(' ')
            if str(watch[0]) == data:
                g = str(watch[0] + '--' + i)
                file_data.append(g + '--' + watch[0] + ' ' + watch[1])

        if file_data == []:
            self.progressBar.hide()
            return QMessageBox.warning(self, "Ошибка", "\nФайлы за эту дату не найдены!")
        else:

            dd = []
            dd2 = []
            for ss in file_data:
                ss = ss.split('--')
                dd.append(ss[1])
                dd2.append(ss[2])

            for i in range(len(dd)):
                value1.append(i)
            d = value1[-1] + 1

            value3 = value2 / d
            w = 0
            www = 0
            seartch_file = []

            for i in dd:
                direсt = str(director + i)
                clvo_pov = 0
                with open(direсt, "r", encoding='utf-8') as file:
                    for line in file:
                        if str(text).lower() in str(line).lower():
                            clvo_pov += 1
                            seartch_file.append(
                                '╔============================================================================================╗\n' + '║Кол-во повторений искомого текста: ' + str(
                                    clvo_pov) + '\n║' + dd2[
                                    www] + ' | Файл: ' + direсt + '\n╚============================================================================================╝')

                            self.listWidget.addItem(seartch_file[w])
                            w += 1
                file.close()
                www += 1
                value += value3
                self.progressBar.setProperty("value", value)
            self.progressBar.hide()
            if seartch_file == []:
                return QMessageBox.warning(self, "Совпадения не найдены")
    except:
        return QMessageBox.warning(self, "Ошибка",
                                   "Произошла ошибка! \nЯ не знаю что это за ошибка, но проверьте кодировку файла, мне нравиться только utf-8")
else:
    try:
        file_wat = []
        for i in files:

            if ".txt" in str(i).lower() or ".rtf" in str(i).lower() or ".doc" in str(i).lower() or ".docx" in str(
                    i).lower() \
                    or ".html" in str(i).lower() \
                    or ".odt" in str(i).lower() or ".xlsx" in str(i).lower() or ".xlsm" in str(i).lower() \
                    or ".py" in str(i).lower() or ".log" in str(i).lower() or ".hml" in str(i).lower() or ".xml" in str(
                i).lower():
                watch = datetime.datetime.fromtimestamp(os.path.getmtime(director + i))
                file_wat.append(str(watch))
                file.append(i)

        if file == []:
            return QMessageBox.warning(self, "Ошибка", 'Файлы с имеющимися форматами не найдены!')
        seartch_file = []
        director = (str(directory) + '/')

        value1 = []
        value2 = 100

        for i in range(len(file)):
            value1.append(i)
        d = value1[-1] + 1

        value3 = value2 / d
        w = 0
        fff = 0
        for i in file:
            direсt = str(director + i)
            clvo_pov = 0
            with open(direсt, "r", encoding='utf-8') as file:
                for line in file:
                    if str(text).lower() in str(line).lower():
                        clvo_pov += 1
                        seartch_file.append(
                            '╔============================================================================================╗\n' + '║Кол-во повторений искомого текста: ' + str(
                                clvo_pov) + '\n║' + file_wat[
                                fff] + ' | Файл: ' + direсt + '\n╚============================================================================================╝')
                        self.listWidget.addItem(seartch_file[w])
                        w += 1
            file.close()
            fff += 1
            value += value3
            self.progressBar.setProperty("value", value)
        self.progressBar.hide()
        if seartch_file == []:
            return QMessageBox.warning(self, "Совпадения не найдены")
    except:
        return QMessageBox.warning(self, "Ошибка",
                                   "Произошла ошибка!\n Я не знаю что это за ошибка, но проверьте кодировку файла, мне нравиться только utf-8")