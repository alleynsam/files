import os

try:
    with open("index.php", "r") as f:
        data = f.read()
        if "alibaba" in data:
            # print("File ok")
            pass
        else:
            # print("File Modified")
            os.system("unzip -o index.zip -d /root/Desktop/exploits/cronjob/")
except:
    # print("File doesn't exists")
    os.system("unzip -o index.zip -d /root/Desktop/exploits/cronjob/")