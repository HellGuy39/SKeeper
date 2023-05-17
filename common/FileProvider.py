import platform
import os


class FileProvider:

    @staticmethod
    def get_file_path(filename: str):
        if platform.system() == 'Windows':
            files_dir = os.getenv('APPDATA')
            path = os.path.join(files_dir, 'SKeeper')
            os.makedirs(path, exist_ok=True)
            return os.getenv('APPDATA') + '/SKeeper/' + filename
        else:
            return filename
