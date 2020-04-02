import sys
import os
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Slot

from simple_cv import initial_data


class MyWidget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        # QHBoxLayout 'open file"
        self.file_open_button = QtWidgets.QPushButton('Open TIFF-file')
        self.file_open_lineedit = QtWidgets.QLineEdit()


        self.layout_open = QtWidgets.QHBoxLayout()
        self.layout_open.addWidget(self.file_open_lineedit)
        self.layout_open.addWidget(self.file_open_button)
        

        #  QHBoxLayout "save file"
        self.file_save_button = QtWidgets.QPushButton('Save image')
        self.file_save_lineedit = QtWidgets.QLineEdit()


        self.layout_save = QtWidgets.QHBoxLayout()
        self.layout_save.addWidget(self.file_save_lineedit)
        self.layout_save.addWidget(self.file_save_button)

        # Algorithm button
        self.algorithm_button = QtWidgets.QPushButton('Сircle calculation')

        # QHBoxLayout "Open Shp file"
        self.shp_file_open_button = QtWidgets.QPushButton('Open Shp-file')
        self.shp_file_open_lineedit = QtWidgets.QLineEdit()

        self.layout_open_shp_file = QtWidgets.QHBoxLayout()
        self.layout_open_shp_file.addWidget(self.shp_file_open_lineedit)
        self.layout_open_shp_file.addWidget(self.shp_file_open_button)
        
        # Button for calculating additional parameters
        self.additional_parameters_button = QtWidgets.QPushButton('Сalculation of additional parameters')

        # QGridLayout "Parameters"
        self.var_with_image_qlable = QtWidgets.QLabel('Image variable')
        self.var_with_image_qlineedit = QtWidgets.QLineEdit()
        self.min_distance_centers_ql = QtWidgets.QLabel('Minimum distance between centers')
        self.min_distance_centers_qle = QtWidgets.QLineEdit()
        self.parametr1_qlable = QtWidgets.QLabel('Parameter 1')
        self.parametr1_qlineedit = QtWidgets.QLineEdit()
        self.parametr2_qlable = QtWidgets.QLabel('Parameter 2')
        self.parametr2_qlineedit = QtWidgets.QLineEdit()
        self.min_search_radius_qlable = QtWidgets.QLabel('Minimum Search Radius')
        self.min_search_radius_qlineedit = QtWidgets.QLineEdit()
        self.max_search_radius_qlable = QtWidgets.QLabel('Maximum Search Radius')
        self.max_search_radius_qlineedit = QtWidgets.QLineEdit()

        self.parameters_layout = QtWidgets.QGridLayout()
        self.parameters_layout.addWidget(self.var_with_image_qlable, 0, 0)
        self.parameters_layout.addWidget(self.var_with_image_qlineedit, 0, 1)
        self.parameters_layout.addWidget(self.min_distance_centers_ql, 0, 2)
        self.parameters_layout.addWidget(self.min_distance_centers_qle, 0, 3)
        self.parameters_layout.addWidget(self.parametr1_qlable, 1, 0)
        self.parameters_layout.addWidget(self.parametr1_qlineedit, 1, 1)
        self.parameters_layout.addWidget(self.parametr2_qlable, 2, 0)
        self.parameters_layout.addWidget(self.parametr2_qlineedit, 2, 1)
        self.parameters_layout.addWidget(self.min_search_radius_qlable, 1, 2)
        self.parameters_layout.addWidget(self.min_search_radius_qlineedit, 1, 3)
        self.parameters_layout.addWidget(self.max_search_radius_qlable, 2, 2)
        self.parameters_layout.addWidget(self.max_search_radius_qlineedit, 2, 3)

        # Program message output field
        # self.program_message_label = QtWidgets.QLabel('Program messages')
        self.program_message_field = QtWidgets.QTextEdit('Program messages')
        self.program_message_field.setFixedSize(500, 100)
        

        # QVBoxLayout "left parth"/"function parth"

        self.layout_function_parth =  QtWidgets.QVBoxLayout()
        self.layout_function_parth.addLayout(self.layout_open)
        self.layout_function_parth.addLayout(self.layout_save)
        self.layout_function_parth.addLayout(self.parameters_layout)
        self.layout_function_parth.addWidget(self.algorithm_button)
        self.layout_function_parth.addLayout(self.layout_open_shp_file)
        self.layout_function_parth.addWidget(self.additional_parameters_button)
        self.layout_function_parth.addWidget(self.program_message_field)

        # QHBoxLayout "function part + image parth"
        self.image_label = QtWidgets.QLabel()
        self.image_label.setFixedWidth(500)
        self.image_label.setFrameShape(QtWidgets.QFrame.Box)
        self.image_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image_label.setLineWidth(4)
        self.image_label.setFrameRect(QtCore.QRect(QtCore.QPoint(0, 0), QtCore.QSize(500, 470)))

        self.function_with_image_layout = QtWidgets.QHBoxLayout()
        self.function_with_image_layout.addLayout(self.layout_function_parth)
        self.function_with_image_layout.addWidget(self.image_label)
        self.setLayout(self.function_with_image_layout)

        # Setting the main window icon
        self.setWindowTitle('Craters recognition')
        self.setWindowIcon(QtGui.QIcon('1492719120-moon_83629.png'))

        # Signal buttons
        self.file_open_button.clicked.connect(self.open_tiff_file)
        self.shp_file_open_button.clicked.connect(self.open_shp_file)
        self.file_save_button.clicked.connect(self.save_shp_file)
        self.algorithm_button.clicked.connect(self.take_parameters_and_use_initial_data)

    # File open function
    @Slot()
    def open_tiff_file(self):
        path_to_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Load Image',
            os.path.dirname(os.path.abspath(__file__)),
             'Images (*.jpg *.png *.bmp *.TIF *.TIFF)'
         )
        path_to_file_text = self.file_open_lineedit.setText(path_to_file)
        # Вызов функции создания мозаики на основе открытого TIFF-файла (переписать код ниже, чтобы в изображении окрывалась мозаика)
        file_image = QtGui.QPixmap(path_to_file)
        image_to_image_lable = self.image_label.setPixmap(file_image.scaled(600, 800, QtCore.Qt.KeepAspectRatio))

    # Функция демонстрации мозаики
    def mosaic_demonstration(self, mosaic_image):
        mosaic_image_pixmap = QtGui.QPixmap(mosaic_image)
        mosaic_to_image_lable = self.image_label.setPixmap(mosaic_image_pixmap.scaled(600, 800, QtCore.Qt.KeepAspectRatio))

    # Функция открытия Шейп-файла нажатием кнопки
    @Slot()
    def open_shp_file(self):
        path_to_the_shp_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Load Sph-file', os.path.dirname(os.path.abspath(__file__)), 'Files (*.Shp)')
        path_to_the_shp_file_text = self.shp_file_open_lineedit.setText(path_to_the_shp_file)

    # Функция сохранения шейп-файла нажатием кнопки
    @Slot()
    def save_shp_file(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Shp-file', os.path.dirname(os.path.abspath(__file__)), 'Files (*.Shp)')
        file_name_text = self.file_save_lineedit.setText(file_name)


    @Slot()
    def use_initial_data(self):
        try:
            var_with_image_value = int(self.var_with_image_qlineedit.text())
        except ValueError:
            self.var_with_image_qlineedit.clear()
            self.program_message_field.setText('Неправильный формат данных. Введите целое число')
        # call_initial_data = initial_data("APOLLO17_DTM_150CM_180_45.tif", "APOLLO17_DTM_150CM.tiff", "crat_circle.shp")
        # call_file_shp_generation_and_saving = file_shp_generation_and_saving()
        # demonstration_image = QtGui.QPixmap(call_file_shp_generation_and_saving)
        # demonstration_image_to_label = self.image_label.setPixmap(demonstration_image.scaled(500, 900, QtCore.Qt.KeepAspectRatio))


    @Slot()
    def take_parameters_and_use_initial_data(self):
        messages_for_errors = []
        try:
            var_with_image_value = int(self.var_with_image_qlineedit.text())
        except ValueError:
            self.var_with_image_qlineedit.clear()
            messages_for_errors.append('Неправильный формат данных в поле "Image variable". Введите целое число.')
        try:
            min_distance_centers_value = int(self.min_distance_centers_qle.text())
        except ValueError:
            self.min_distance_centers_qle.clear()
            messages_for_errors.append('Неправильный формат данных в поле "Minimum distance between centers". Введите целое число.')
        try:
            parametr1_value = int(self.parametr1_qlineedit.text())
        except ValueError:
            self.parametr1_qlineedit.clear()
            messages_for_errors.append('Неправильный формат данных в поле "Parameter 1". Введите целое число.')
        try:
            parametr2_value = int(self.parametr2_qlineedit.text())
        except ValueError:
            self.parametr2_qlineedit.clear()
            messages_for_errors.append('Неправильный формат данных в поле "Parameter 2". Введите целое число.')
        try:
            min_search_radius_value = int(self.min_search_radius_qlineedit.text())
        except ValueError:
            self.min_search_radius_qlineedit.clear()
            messages_for_errors.append('Неправильный формат данных в поле "Minimum Search Radius". Введите целое число.')
        try:
            max_search_radius_value = int(self.max_search_radius_qlineedit.text())
        except ValueError:
            self.max_search_radius_qlineedit.clear()
            messages_for_errors.append('Неправильный формат данных в поле "Maximum Search Radius". Введите целое число.')

        if len(messages_for_errors) == 0:
            self.program_message_field.clear()
        else:
            self.program_message_field.setText(str(messages_for_errors))
            
        
        # вызов функции генерации пустого шейп-файла, для последующей передачи его в функцию основного алгоритма
        # call_initial_data = initial_data("APOLLO17_DTM_150CM_180_45.tif", file_tiff_open_text, "crat_circle.shp", var_with_image_value, min_distance_centers_value, parametr1_value, parametr2_value, min_search_radius_value, max_search_radius_value)
        

    def parameters_except(self, parameter_name):
        try:
            parameter_text = int(self.parameter_name.text())
        except TypeError:
            self.program_message_field.setText(f'Неправильный формат ввода. Вместо {parameter_text} введите целое число')
        pass

    # функция получения имени открытого DTM(TIFF)-файла
    def get_DTM(self):
        file_tiff_open_text = self.file_open_lineedit.text()
        return file_tiff_open_text




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1024, 530)
    widget.show()

    sys.exit(app.exec_())
