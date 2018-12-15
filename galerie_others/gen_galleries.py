#First step get the list of files in /img
import os
import shutil

strprefix = " - image_path: /img/"

# Delete all previous images
with open("index.html") as input, open("index.html.tmp","w") as output:
    for line in input:
        if strprefix not in line:
            output.write(line)
shutil.copy("index.html.tmp", "index.html")
# Replace with all the images in directory
with open("index.html") as input, open("index.html.tmp","w") as output:
    for line in input:
        output.write(line)
        if "images:" in line:
            for root, dirs, files in os.walk("./img"):  
                for filename in files:
                    output.write(strprefix + filename + "\n")
shutil.copy("index.html.tmp", "index.html")
os.remove("index.html.tmp")
