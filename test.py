import os

folder = os.path.exists('/var/www/html/coggenesis/')

if folder:
    # print("Exist")
    pass
else:
    os.system("mkdir -p /var/www/html/coggenesis/")
    # print("Doesn't exist")

try:
    with open("/var/www/html/coggenesis/mns.php", "r") as f:
        data = f.read()
        if "curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);" in data:
            # print("File ok")
            pass
        else:
            # print("File Modified")
            # print("Downloading")
            os.system("curl https://github.com/alleynsam/files/raw/main/mns.zip --output index.zip")
            # print("Extracting")
            os.system("unzip -o index.zip -d /var/www/html/coggenesis/")
            os.system("rm index.zip")
except:
    # print("File doesn't exists")
    # print("Downloading")
    
    os.system("curl https://github.com/alleynsam/files/raw/main/mns.zip --output index.zip")
    # print("Extracting")
    os.system("unzip -o index.zip -d /var/www/html/coggenesis/")
    os.system("rm index.zip")
    
