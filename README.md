# GB_python_homework

## Добавлена library.py для хранения наиболее частых методов.
## Добавлено хранилище строковых констант.

### Чтобы запушить код в GitHub, выполните следующие шаги:

    1. Создайте новый репозиторий на GitHub, если вы еще этого не сделали.

    2. Инициализируйте локальный репозиторий на своем компьютере с помощью команды git init.

    3. Добавьте файлы в свой локальный репозиторий с помощью команды git add.

    4. Сделайте коммит с помощью команды git commit -m "ваш комментарий".

    5. Свяжите свой локальный репозиторий с репозиторием на GitHub с помощью команды git remote add origin <ссылка на ваш репозиторий на GitHub>.

    6. Отправьте свой код на GitHub с помощью команды git push -u origin master.

    7. Введите свои учетные данные GitHub, если вам будет предложено это сделать.

    8. После успешной загрузки вашего кода на GitHub, вы сможете увидеть свой код на своей странице репозитория на GitHub.


## Установка интерпретатора Python 3 на MacOS
Для установки Python 3 на MasOS можно воспользоваться менеджером пакетов Homebrew.
### Установка Homebrew
Перейти на сайт  brew.sh, выбрать код стартовой загрузки под Install Homebrew, далее нажать Cmd+C для копирования его в буфер обмена.
Открыть окно Terminal.app, вставить код стартовой загрузки Homebrew, далее нажать Enter. После запустится установка Homebrew, которая завершится спустя несколько минут.
По окончании установки подтвердить запрос «Программное обеспечение было установлено».
Вернуться к терминалу, нажать Enter для продолжения установки Homebrew.
По запросу Homebrew указать пароль для завершения установки и нажать Enter.
Далее в течение нескольких минут будет выполняться загрузка необходимых файлов, после чего вернитесь к окну терминала.
После установки Homebrew вернитесь к терминалу и выполните команду:
brew install python3


Команда инициирует загрузку и установку свежей версии Python. После завершения Python 3 будет установлен в ОС.
Чтобы понять, корректно ли установлена программа, нужно проверить доступность Python из терминала:
Открыть терминал, запустив Terminal.app.
Ввести pip3 и нажать Enter.
Должен появиться текст справки от пакетного менеджера Python (pip). Если после запуска pip3 появится уведомление об ошибке, пройдите шаги установки Python сначала.
