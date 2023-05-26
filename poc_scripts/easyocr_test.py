import easyocr
# this needs to run only once to load the model into memory
reader = easyocr.Reader(['en'], gpu=True)
result = reader.readtext('killfeed\\4.png')
print(result)
