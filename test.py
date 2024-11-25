import os

files = os.listdir('./infoData')

for file in files:
    pageRaw = file.split(".")
    page = pageRaw[0]

    print(page)
