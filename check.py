import os
with open("Derpibooru.md","r",encoding="utf-8") as f:
    txt = f.read()

for _,_,filename in os.walk('./image/'):
    for file in filename:
        if file not in txt:
            os.remove("image/"+file)