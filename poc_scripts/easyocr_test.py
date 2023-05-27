import easyocr
import time
# this needs to run only once to load the model into memory

print(str(round(time.time() * 1000)))
result = reader.readtext('assets\\killfeed_examples\\2.png')
print(result)
print(str(round(time.time() * 1000)))
