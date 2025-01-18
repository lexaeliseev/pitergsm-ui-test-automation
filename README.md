 <h1 align="center">Автоматизация интернет-магазина <a href="https://pitergsm.ru/">PiterGsm</a></h1>

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
### Установка зависимостей
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
---
### Локальный запуск автотестов в браузере Firefox

```
pytest . --browser=firefox
```
---
### Локальный запуск автотестов в браузере Google Chrome

```
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

<img src="source/build_with_parameters.jpg" width="600">

---
### Реализована интеграция с Allure
#### Allure отчетность
**Результаты тестирования доступны в Allure-отчете.**
<img src="source/allure_report.jpg" width="600">
**При выполнении автотестов к результатам тестов прикрепляются артефакты, например логи, скриншоты и т.д.**
<img src="source/allure_report_behaviors.jpg" width="600">

#### Allure TestOps
<img src="source/testops_report.jpg" width="600">

##### При выполнении автотестов к результатам тестов прикрепляются логи, скриншоты, HTML-страница и видеозапись прохождения кейса.

##### Пример видео
https://github.com/user-attachments/assets/f6e853d1-3e50-47b6-a308-6dc586ce366d
### Реализована интеграция с Jira
<img src="source/jira_report.jpg" width="600">

---
### Внедрена функция отправки уведомлений в Telegram о результатах выполнения тестов
<img src="source/telegram_report.jpg" width="600">
