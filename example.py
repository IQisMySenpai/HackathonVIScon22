import os
import shutil

files = os.listdir("/home/alisot2000/Desktop/lecturer")
ext = []

for file in files:
    ex = os.path.splitext(file)[1]

    if ex not in ext:
        ext.append(ex)

print(ext)