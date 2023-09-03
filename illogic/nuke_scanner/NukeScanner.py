import _MODELS
import re
import os
from common.utils import *
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# ######################################################################################################################

_PREFIX_TO_DELETE = "_TO_DELETE_"

# ######################################################################################################################

class ConfirmationNukeScanner(QDialog):
    def __init__(self,render_out_folder, data_renaming_folder, parent=None):
        super(ConfirmationNukeScanner, self).__init__(parent)

        # Model attributes
        self.__render_out_folder = render_out_folder
        self.__data_renaming_folder = data_renaming_folder

        # UI attributes
        self.__ui_width = 550
        self.__ui_height = 400
        self.__ui_min_width = 300
        self.__ui_min_height = 300
        self.__ui_pos = QDesktopWidget().availableGeometry().center() - QPoint(self.__ui_width, self.__ui_height) / 2
        self.__tab_widget = None

        # name the window
        self.setWindowTitle("Confirmation Nuke Scanner")
        # make the window a "tool" in Maya's eyes so that it stays on top when you click off
        self.setWindowFlags(QtCore.Qt.Tool)
        # Makes the object get deleted from memory, not just hidden, when it is closed.
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.__create_ui()
        self.__refresh_ui()

    def __create_ui(self):
        """
        Create the ui
        :return:
        """
        # Reinit attributes of the UI
        self.setMinimumSize(self.__ui_min_width, self.__ui_min_height)
        self.resize(self.__ui_width, self.__ui_height)
        self.move(self.__ui_pos)

        # Main Layout
        main_lyt = QVBoxLayout()
        self.setLayout(main_lyt)
        main_lyt.setContentsMargins(5, 8, 5, 8)

        title = QLabel("Are you sure you want to mark all these files for later deletion?")
        main_lyt.addWidget(title, alignment=Qt.AlignCenter)

        self.__ui_list_folders = QListWidget()
        main_lyt.addWidget(self.__ui_list_folders)

        btn_lyt = QHBoxLayout()
        main_lyt.addLayout(btn_lyt)

        close_btn = QPushButton("Cancel")
        close_btn.clicked.connect(self.close)
        btn_lyt.addWidget(close_btn)
        accept_btn = QPushButton("Accept")
        accept_btn.clicked.connect(self.accept)
        btn_lyt.addWidget(accept_btn)

    def __refresh_ui(self):
        """
        Refresh the ui according to the model attribute
        :return:
        """
        self.__ui_list_folders.clear()
        for path in self.__data_renaming_folder.keys():
            self.__ui_list_folders.addItem(QListWidgetItem(path))


class NukeScanner:
    def __init__(self):
        """
        Constructor
        """
        self.__files = []
        self.__folders = []
        self.__retrieve_shot()
        if self.__shot_dir is not None:
            self.__retrieve_files()
        else:
            print("SHOT DIR NOT FOUND")

    def __retrieve_shot(self):
        """
        Retrieve the current shot
        :return:
        """
        self.__compo_filepath = nuke.root()['name'].value().replace("\\", "/")
        match = re.match(r"^(.+)/compo/\w*\.nk$", self.__compo_filepath)
        if match:
            self.__shot_dir = match.group(1)
        else:
            self.__shot_dir = None

    def __retrieve_files(self):
        """
        Retrieve all the files
        :return:
        """
        read_nodes = nuke.allNodes("Read")
        for node in read_nodes:
            file_path = node["file"].value()
            # Test if in render_out
            if not file_path.startswith(self.__shot_dir):
                continue
            folder = os.path.dirname(file_path)
            if folder in self.__folders:
                continue
            self.__folders.append(folder)

    def __check_folder_recursive(self, folder, check_folder=True):
        """
        Check the files recursively to output folder not used
        :param folder
        :param check_folder
        :return: folder is used, not used folders
        """
        not_used_folders = []
        is_used = True if not check_folder else folder.replace("\\", "/") in self.__folders
        for child in os.listdir(folder):
            path = os.path.join(folder, child)
            if not os.path.isdir(path):
                continue
            is_subfolder_used, not_used_in_subfolder = self.__check_folder_recursive(path)
            is_used = is_used or is_subfolder_used
            not_used_folders.extend(not_used_in_subfolder)

        if not is_used:
            return is_used, [folder]
        else:
            return is_used, not_used_folders

    def run(self):
        """
        Run the Nuke Scanner
        :return:
        """
        if self.__shot_dir is None: return
        render_out_folder = self.__shot_dir + "/render_out"
        is_used, folders_to_delete = self.__check_folder_recursive(render_out_folder, False)
        dict_rename_folders = {}
        for folder_path in folders_to_delete:
            folder_path= folder_path.replace("\\", "/")
            dirname, basename = os.path.split(folder_path)
            if not basename.startswith(_PREFIX_TO_DELETE):
                new_path = os.path.join(dirname, _PREFIX_TO_DELETE + basename).replace("\\", "/")
                dict_rename_folders[folder_path] = new_path

        if len(dict_rename_folders)>0:
            if ConfirmationNukeScanner(render_out_folder, dict_rename_folders).exec_():
                for folder_path,new_path in dict_rename_folders.items():
                    os.rename(folder_path, new_path)
                    print(folder_path + "\n\t--> " + new_path)

def main():
    NukeScanner().run()

if __name__ == '__main__':
    main()