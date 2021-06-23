import autopy
import time
import random
with open("doc", encoding="UTF-8") as doc:
    c = doc.read(1)
    while c:
        if (c == " "):
            time.sleep(random.random()*2)
        autopy.key.type_string(c)
        c = doc.read(1)
        time.sleep(0.05 + random.random())
    print ("End of file")