from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Импорт необходим для указания типа поиска элементов
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests # Нужна для HTTP-запросов
import os # Нужна для доступа к файловой системе

options = Options()
options.add_argument("--disable-extensions")  # Отключение расширений
options.add_argument("--disable-gpu")  # Отключение обработки GPU
options.add_argument("--no-sandbox")  # Отключение режима песочницы
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Отключение логирования

driver = webdriver.Chrome(options=options)
driver.get('https://www.хакатоны.рус/') # открываем страницу

# ФУНКЦИЯ ПАРСИНГА ТЕКСТА
def parse_text():
    timeout = 1
    elements = WebDriverWait(driver, timeout).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "js-feed-post-link"))
    )
    # находим все элементы на странице с текстом
    elements = driver.find_elements(By.CLASS_NAME, 'js-feed-post-link')
    
    # открываем текстовый файл в режиме записи
    with open('output.txt', 'w', encoding='utf-8') as file:
        for element in elements:
            if element.text.strip():
                file.write(element.text + '\n')
        
parse_text()

# ФУНКЦИЯ ПАРСИНГА ИЗОБРАЖЕНИЙй
def parse_images():
    images = driver.find_elements(By.CLASS_NAME, 't-feed__post-bgimg') # ищем HTML-элементы по названию класса
    image_urls = [] # создаем пустой список для ссылок на картинки

    # заполняем список image_urls - ссылками на картинками
    for image in images:
        image_urls.append(image.get_attribute('data-original'))

    # скачиваем картинку по текущей ссылке
    for image_url in image_urls:

        # задаем папку для сохранения
        folder = './img'
        # задаем имя файла (которое состоит из последней части ссылки)
        # ССЫЛКА - google.com/img/pics/1.png
        image_name = image_url.split('/')[-1]
        # совмещаем папку и название файла, чтобы задать путь для сохранения
        save_path = os.path.join(folder, image_name)
        
        # скачиваем изображение
        response = requests.get(image_url)
        
        # если ответ пришел успешный (код 200)
        if response.status_code == 200:
            # открыть файл для записи по пусти save_path
            with open(save_path, 'wb') as file:
                file.write(response.content)
        else:
            print('Изображение не загрузилось')

# закрываем браузер
driver.quit()