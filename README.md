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
![Параметризация](https://downloader.disk.yandex.ru/preview/a6fd3d72afa2a4be741925a17b248f2b3ce1839641155334bb9ca9ba809b19d7/675e06f5/sj-sFvaekmSvWVCt7oFnc-pTYDwbCMsLM3D-pra5ZYO2wTsJsNk3TODGf7B8WZhYcqQHUjYrTsH3SSqzJVdp3A%3D%3D?uid=0&filename=параметризация.jpeg.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=768x768)
---

### Интеграция с Allure







