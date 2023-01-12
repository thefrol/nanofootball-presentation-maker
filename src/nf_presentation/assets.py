import importlib.resources as pkg_resources
from .settings import RFS_LOGO_FILE_NAME

def get_rfs_logo():
    return pkg_resources.open_binary(__package__, RFS_LOGO_FILE_NAME)

def get_test_data() -> dict:
    return pkg_resources.open_text(__package__, 'test_data.json',encoding='utf8')

def get_exercise_test_data() -> dict:
    return pkg_resources.open_text(__package__, 'exercise_test_data.json',encoding='utf8')

