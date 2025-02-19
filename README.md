# Проект распознавания кратеров на снимках поверхности Луны

**Описание проекта:**

Данный проект представляет собой программу ***распознавания кратеров на снимках поверхности Луны*** 
при помощи языка программирования ***Python*** с использованием дополнительных библиотек. 
Нужен он, в первую очередь тем, кто занимается геоморфологией и исследованием лунной поверхности, 
а так же тем, кто прямо или косвенно связан с лунными кратерами. 
Возможен запуск программы и для других небесных тел, однако точность и достоверность обнаружения, 
всвязи с различным строением поверхности, может быть низкой.	
Основных библиотек в проекте 3, это ***PySide2***, ***gdal*** и ***cv2***. 
Библиотека PySide2 использована для реализации графического пользовательского интерфейса программы.
Алгоритмическая часть построена на двух других:
Cv2 (OpenCV) используется для непосредственно обнаружения кругов. 
Gdal используется для чтения геотифа, который является исходным типом файлов для программы и для создания, 
записи и чтения шейп файла, который содержит обнаруженные кратеры с их характеристиками.

**Основные требования к геотифу:**

1. Проекция файла должна быть без искажений углов, в идеале, с центром проеции в центре файла.
2. Это должна быть именно ЦМР, c координатами высот.
	
**Установка:**

1. Почти все основные библиотеки устанавливаются командой:
	pip install -r requirements.txt
Почти, потому как бинарная библиотека gdal устанавливается отдельно.
Рекомендуем в начале установить её, и уже после все остальные библиотеки
командой, приведённой выше.

2. Установка gdal для Windows. 
Перейдите на сайт: 
	https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal 
и выберите подходящую версию библиотеки исходя из:
GDAL-[версия GDAL]-cp[версия python]-none-[архитектура системы].whl
Скачайте нужную вам версию и переместите в корневую папку, 
где планируете развернуть проект. Затем командой:
	python -m pip install GDAL-[и тд.].whl
проведите её установку.

**Первичный запуск и использование:**

1. Запустите скрипт интерфейса в консоли командой:
	python craters_recognition_interface.py
2. В открывшемся окне интерфейса нажмите кнопку "Open tiff file".
3. В открывшемся диалоговом окне выберите файл для обработки.
4. В правой части окна интерфейса откроется мозаика выбранного вами файла.
Имя shp файла, куда будут записаны данные, после детектирования кратеров
сгенерируется автоматически в строке "Choose shp file name". 
Вы можете изменить название файла в этой строке на любое другое, удобное вам.
5. Запуск алгоритма детектирования осуществляется кнопкой "Сircles calculation".
Все необходимые для расчёта параметры заданы по-умолчанию, но
вы можете изменить их по свому усмотрению.
6. После нажатия кнопки "Сircles calculation" запустится алгоритм детектирования кратеров. 
Это может занять некоторое время в зависимости от параметров ваше операционной системы.
По завершении обработки в правой части экрана откроется отмывка изображения с определёнными на ней кратерами в виде окружностей. 
Данные детектированных окружностей запишутся в shp файл автоматически.

Примечание: Вместе с shp файлом автоматически создадутся еще несколько файлов с расширениями: *.dbf, *.prj, *.shx. 
Это сопутсвующие файлы, необходимые для корректного открытия и использования shp файла в других программах.

**Сообщения об ошибках:**

Если что-то пойдёт не так, сообщение об ошибках появится в текстовом поле "Program messages"
в левой нижней части окна интерфейса.

