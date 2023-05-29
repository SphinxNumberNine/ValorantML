import easyocr
import time
# this needs to run only once to load the model into memory
reader = easyocr.Reader(['en'], gpu=True)

print(str(round(time.time() * 1000)))
result = reader.readtext('assets\\test_killfeed.png')
print(result)
print(str(round(time.time() * 1000)))
