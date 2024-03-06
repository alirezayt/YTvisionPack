import importlib.util

module_name = 'file'
module_path = 'file.pyc'

spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)