import importlib.util
import os

module_name = 'b.cpython-313'
module_path = 'b.cpython-313.pyc'  # مسیر فایل pyc

# بارگذاری ماژول
spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)