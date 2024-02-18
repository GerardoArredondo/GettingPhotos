from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

#PATH = "/home/gerotota/Udemy/Python/Projects/GettingPhotos/chromedriver.exe"

wd = webdriver.Chrome()
wd.get("https://www.google.com/")


def gettinImages(wd, delay, maxImages):
    def scroll(wd):
        wd.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?sca_esv=cd5515df3b07dc25&sxsrf=ACQVn082yViQP3i1TglnfFEU-uThXU7I6Q:1708285442500&q=dogs&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjApuaX07WEAxWcJ0QIHUo0AmYQ0pQJegQIDRAB&biw=1900&bih=897"
    wd.get(url)

    image_urls = set()
    thumbnails = wd.find_elements(By.CLASS_NAME, "rg_i")

    for img in thumbnails[:maxImages]:
        try:
            img.click()
            time.sleep(delay)
        except:
            continue
        
        images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
        for image in images:
            if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                image_urls.add(image.get_attribute('src'))
                print(f"Se encontró una imagen número {len(image_urls)}")

            if len(image_urls) >= maxImages:
                return image_urls

    return image_urls




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

urls = gettinImages(wd, 1, 5)


for i, url in enumerate(urls):
    downloadImage("Photos/", url, str(i)+".jpg")


print(urls)


