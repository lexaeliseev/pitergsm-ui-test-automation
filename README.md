 <h1 align="center">Автоматизация интернет-магазина <a href="https://pitergsm.ru/">PiterGsm</a></h1>

## Описание

---

### Используемый стек технологий и инструментов
| Python | Pycharm | GitHub | Pytest | Selenide | Selene | Allure Report | Allure TestOps | Jenkins | Jira | Telegram |
|--------|---------|--------|--------|----------|--------|---------------|----------------|---------|------|----------|
| <img src="https://www.python.org/static/img/python-logo.png" width="100" height="27"> | <img src="https://bobronium.gallerycdn.vsassets.io/extensions/bobronium/darcula-from-pycharm/0.9.0/1658399345105/Microsoft.VisualStudio.Services.Icons.Default" width="67" height="53"> | <img src="https://www.renebergelt.de/logos/github.png" width="100" height="53"> | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/800px-Pytest_logo.svg.png" width="67" height="53"> | <img src="https://github.com/AleksShakhmatov/HW_14_PY_FirstProject/blob/master/media/logo/Selenide.png?raw=true" width="67" height="53"> | <img src="https://github.com/AleksShakhmatov/HW_14_PY_FirstProject/blob/master/media/logo/Selene.png?raw=true" width="67" height="53"> | <img src="https://raw.githubusercontent.com/AleksShakhmatov/HW_14_PY_FirstProject/ae64e477ecd97b46b758d3d8fc30dba0d10cccf7/media/logo/Allure_Report.svg" width="67" height="53"> | <img src="https://raw.githubusercontent.com/AleksShakhmatov/HW_14_PY_FirstProject/ae64e477ecd97b46b758d3d8fc30dba0d10cccf7/media/logo/Allure_TestOps.svg" width="67" height="53"> | <img src="https://raw.githubusercontent.com/AleksShakhmatov/HW_14_PY_FirstProject/ae64e477ecd97b46b758d3d8fc30dba0d10cccf7/media/logo/Jenkins.svg" width="67" height="53"> | <img src="https://raw.githubusercontent.com/AleksShakhmatov/HW_14_PY_FirstProject/ae64e477ecd97b46b758d3d8fc30dba0d10cccf7/media/logo/Jira.svg" width="67" height="53"> | <img src="https://raw.githubusercontent.com/AleksShakhmatov/HW_14_PY_FirstProject/ae64e477ecd97b46b758d3d8fc30dba0d10cccf7/media/logo/Telegram.svg" width="67" height="53"> |

### Реализованные автотесты
- Проверка успешной авторизации в системе
- Проверка отображения пунктов меню и конкретного перехода к нужному разделу при клике на них
- Проверка успешного поиска товара
- Проверка отображения ошибки при не успешном поиске товара
---
### Локальный запуск автотестов в браузере Firefox

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser=firefox
```
---
### Локальный запуск автотестов в браузере Google Chrome

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser=chrome
```
---
### Запуск автотестов на удаленном сервере
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --run_mode=remote --browser=[chrome|firefox] --browser_version=125.0
# Укажите браузер: chrome (по умолчанию) или firefox, и версию браузера (по умолчанию 125.0)
```
---
### Сборка в <a href="https://jenkins.autotests.cloud/job/C16-lexaeliseev-hw14/">Jenkins</a>
Для запуска сборки выполните следующие шаги:
1. Перейдите в раздел **"Build with Parameters"**.
2. Укажите необходимые параметры:
   - **Адрес удаленного сервера**: Введите URL-адрес удаленного сервера.
   - **Выбор набора тестов**: Укажите, какие тесты должны быть запущены.
   - **Версия браузера**: Выберите версию браузера для тестирования.
   - **Браузер**: Укажите, какой браузер использовать (Chrome или Firefox).
   - **Комментарий для оповещения в Telegram**: Добавьте комментарий, который будет отправлен в Telegram для оповещения о статусе тестов.
3. После заполнения всех параметров нажмите кнопку **"Build"**.

![Параметризация](https://downloader.disk.yandex.ru/preview/4643599df4e9bc232a39f5624df15eea01abdbcbfeaad415c7b24efe4242ae07/675f3fc2/sj-sFvaekmSvWVCt7oFnc-pTYDwbCMsLM3D-pra5ZYO2wTsJsNk3TODGf7B8WZhYcqQHUjYrTsH3SSqzJVdp3A%3D%3D?uid=0&filename=параметризация.jpeg.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=768x768)

---
### Реализована интеграция с Allure
#### Allure отчетность
![Allure Image 1](https://downloader.disk.yandex.ru/preview/f0c32b788ea11ba82f58acf51a0f5fa8782c8c201ab4b2047c45bb70155f893b/675f44bf/SeZw6LKQV5jSyMotMAhzIOVeEBPQsEGUVwXuEjKbY8NYF24gtbJyOBEeju2VA5a6qr9OL_UnnTgQNb4gJ1RnTw%3D%3D?uid=0&filename=allure.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=768x768)
![Allure Image 2](https://downloader.disk.yandex.ru/preview/857119d3a21c4160be29a7533f969466de41e7a973d17d0f0b4894950487d9da/675f44ff/acKVlcKTGYGsTEm2uFweUMnJAGrRo2nR49uPdmkq9SGUVxdG7TaUvm4j-ZgbAVDg7yH0Lv0j7x0XjhmcsQMkfg%3D%3D?uid=0&filename=allure1.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=768x768)
#### Allure TestOps
![TestOps](https://downloader.disk.yandex.ru/preview/28da4080ccb3b73b03d651d0ebc3c2ba6a40199d8ce2981573763f590f11f12c/675f3b95/TzZwBuc3ZEepEH1Wa2Q9Wnf7KSO1oRxDG3Vj7NJYyg0yapNWfAvDoFx01U1hDhYY-afSI4Cvqpqxp8v6VOZ0vA%3D%3D?uid=0&filename=testops.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=768x768)
##### При выполнении автотестов к результатам тестов прикрепляются логи, скриншоты, HTML-страница и видеозапись прохождения кейса.
![TestOps1](https://downloader.disk.yandex.ru/preview/432dba5d5a5975381e191335e06c89f00379e2ec648598f928bce03a28d8c36b/675f3bc7/u3kNpH13M6KlKvErGhDlu3PogqDzGCdN8I3F1MzLghTMpnbNk9MDRTWr5bRfwxfXmgGr3RnjAyt4SiGwOIZM6A%3D%3D?uid=0&filename=testops1.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=768x768)
##### Пример видео
<video width="500" height="500" controls>
  <source src="https://disk.yandex.ru/client/disk/QA%20GURU?idApp=client&dialog=slider&idDialog=%2Fdisk%2FQA%20GURU%2F3452c805-a2b3-4143-92ca-dfb4f7c0c756.mp4?dl=1" type="video/mp4">
</video>


---
### Реализована интеграция с Jira
![Jira](https://downloader.disk.yandex.ru/preview/b45588512bf91d56792d6dd8c078132e968c8280b31a6f748548dd36b8c8ee68/675f3e34/_yCxC1HuWAkLDNrwRd3Xsa1_UNysgJnv-CNLfeNfZI9f5ZtNWa5y9OZ-eATOIcd2f8ih-1tTbFGHtIOQ2KtEWg%3D%3D?uid=0&filename=jira.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=768x768)
---
### Внедрена функция отправки уведомлений в Telegram о результатах выполнения тестов
![Telegram](https://downloader.disk.yandex.ru/preview/29e13194cfbfdd8208cfd5b6acb8fb565caa597cdf8062d4e237d37a790ed906/675f3f35/0dDTxPIZayj6BID4yqwhnmfeNjfxU9svG_i8f4dWSFkYlolTXYmQlQn_a_Qyip_zSl-NtK0_66HCjuSjnLyG6A%3D%3D?uid=0&filename=telegram.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=768x768)



