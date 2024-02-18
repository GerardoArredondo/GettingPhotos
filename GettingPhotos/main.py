from selenium import webdriver
import requests
import io
from PIL import Image

#PATH = "/home/gerotota/Udemy/Python/Projects/GettingPhotos/chromedriver.exe"

wd = webdriver.Chrome()
wd.get("https://www.google.com/")

image_url = "https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"


def downloadImage(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Funciona (?)")
    
    except Exception as e:
        print("Algo fallo - ", e)

downloadImage("", image_url, "test.jpg")
