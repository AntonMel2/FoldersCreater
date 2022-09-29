import os

class FolderCr:

    def __init__(self, folder_name, path, folder_exp="Export", folder_pho="Phoenix"):
        self.folder_name = folder_name
        self.path = path
        self.folder_exp = folder_exp
        self.folder_pho = folder_pho

    def create_folder(self, count_part):
        if not (os.path.exists(self.path + '/' + self.folder_name)):
            os.chdir(self.path)
            os.mkdir(self.folder_name)
            os.chdir(self.path + '/' + self.folder_name)
            os.mkdir(self.folder_exp)
            os.mkdir(self.folder_pho)
            os.chdir(self.path + '/' + self.folder_name + '/' + self.folder_exp)
            for i in range(count_part):
                os.mkdir("P" + str(i + 1) + "_exp")
            os.chdir(self.path + '/' + self.folder_name + '/' + self.folder_pho)
            for i in range(count_part):
                os.mkdir("P" + str(i + 1) + "_phoenix")
            return True
        else:
            print("Папка с именем " + self.folder_name + " уже существует, используйте другое имя")
            return False








