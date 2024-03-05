import marshal
with open('my_function.marshal', 'rb') as file:
    decoded_function = marshal.loads(file.read())
def new_function():
    pass
new_function.__code__ = decoded_function
new_function()