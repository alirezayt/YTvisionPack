import importlib.util

module_name = 'pack.cpython-38'  # نام ماژول بدون پسوند
module_path = 'pack.cpython-38.pyc'  # مسیر فایل pyc

spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)