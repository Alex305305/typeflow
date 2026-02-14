# lessons.py
# Уроки для ТРЕНАЖЁРА СЛЕПОЙ ПЕЧАТИ (десятипальцевый метод, раскладка ЙЦУКЕН)
# Каждое упражнение: 40-60 символов для непрерывной тренировки 1-2 минуты

LESSONS = {
    "beginner": {
        # Уровень 1: базовая позиция — указательные пальцы на А/О
        "1_base_position": [
            "а о а о а о а о а о а о а о а о а о а о а о а о а о а о а о а о а о",
            "о а о а о а о а о а о а о а о а о а о а о а о а о а о а о а о а о",
            "ааа ооо ааа ооо ааа ооо ааа ооо ааа ооо ааа ооо ааа ооо ааа ооо",
            "ооо ааа ооо ааа ооо ааа ооо ааа ооо ааа ооо ааа ооо ааа ооо ааа",
            "а о о а а о о а а о о а а о о а а о о а а о о а а о о а а о о а",
            "о а а о о а а о о а а о о а а о о а а о о а а о о а а о а а о о",
            "аоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоао",
            "оаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоаоао"
        ],

        # Уровень 2: средние пальцы — В/Л + базовые А/О
        "2_middle_fingers": [
            "а в о л а в о л а в о л а в о л а в о л а в о л а в о л а в о л а в о л",
            "л о в а л о в а л о в а л о в а л о в а л о в а л о в а л о в а л о в а",
            "ввв ллл ааа ооо ввв ллл ааа ооо ввв ллл ааа ооо ввв ллл ааа ооо",
            "о л а в о л а в о л а в о л а в о л а в о л а в о л а в о л а в о л а в",
            "ав ол ва ло ав ол ва ло ав ол ва ло ав ол ва ло ав ол ва ло ав ол",
            "лвао лвао лвао лвао лвао лвао лвао лвао лвао лвао лвао лвао лвао",
            "а в л о а в л о а в л о а в л о а в л о а в л о а в л о а в л о а в л о",
            "ол ва ол ва ол ва ол ва ол ва ол ва ол ва ол ва ол ва ол ва ол ва ол"
        ],

        # Уровень 3: безымянные пальцы — Ы/Д + предыдущие
        "3_ring_fingers": [
            "ф ы в а о л д ж ф ы в а о л д ж ф ы в а о л д ж ф ы в а о л д ж ф ы",
            "ж д л о а в ы ф ж д л о а в ы ф ж д л о а в ы ф ж д л о а в ы ф ж д л о",
            "фыфыфы ваоаоа лдлдлд жожожо фыфыфы ваоаоа лдлдлд жожожо фыфыфы",
            "а ы в ф о д л ж а ы в ф о д л ж а ы в ф о д л ж а ы в ф о д л ж а ы в ф",
            "фыва олдж фыва олдж фыва олдж фыва олдж фыва олдж фыва олдж фыва",
            "ждло авыф ждло авыф ждло авыф ждло авыф ждло авыф ждло авыф ждло",
            "ф ы ы ф в а а в о л л о д ж ж д ф ы ы ф в а а в о л л о д ж ж д ф ы",
            "олдж фыва олдж фыва олдж фыва олдж фыва олдж фыва олдж фыва олдж"
        ],

        # Уровень 4: мизинцы левой руки — Ф + предыдущие
        "4_left_pinky": [
            "ф ы в а ф ы в а ф ы в а ф ы в а ф ы в а ф ы в а ф ы в а ф ы в а ф ы в а",
            "а в ы ф а в ы ф а в ы ф а в ы ф а в ы ф а в ы ф а в ы ф а в ы ф а в ы ф",
            "ффф ыыы ввв ааа ффф ыыы ввв ааа ффф ыыы ввв ааа ффф ыыы ввв ааа ффф",
            "фыва фыва фыва фыва фыва фыва фыва фыва фыва фыва фыва фыва фыва",
            "аф вы аф вы аф вы аф вы аф вы аф вы аф вы аф вы аф вы аф вы аф вы",
            "выаф выаф выаф выаф выаф выаф выаф выаф выаф выаф выаф выаф выаф",
            "ф ы в а   ф ы в а   ф ы в а   ф ы в а   ф ы в а   ф ы в а   ф ы в а",
            "фывафыва фывафыва фывафыва фывафыва фывафыва фывафыва фывафыва"
        ],

        # Уровень 5: мизинцы правой руки — Ж/Э + полный домашний ряд левой
        "5_right_pinky": [
            "о л д ж э о л д ж э о л д ж э о л д ж э о л д ж э о л д ж э о л д ж э",
            "э ж д л о э ж д л о э ж д л о э ж д л о э ж д л о э ж д л о э ж д л о",
            "ооо ллл ддд жжж эээ ооо ллл ддд жжж эээ ооо ллл ддд жжж эээ ооо ллл",
            "олджэ олджэ олджэ олджэ олджэ олджэ олджэ олджэ олджэ олджэ олджэ",
            "эждло эждло эждло эждло эждло эждло эждло эждло эждло эждло эждло",
            "о л д ж э   о л д ж э   о л д ж э   о л д ж э   о л д ж э   о л д ж",
            "жэ ол джэ ол джэ ол джэ ол джэ ол джэ ол джэ ол джэ ол джэ ол джэ ол",
            "олджэолджэ олджэолджэ олджэолджэ олджэолджэ олджэолджэ олджэолджэ"
        ],

        # Уровень 6: полный домашний ряд левой руки — Ф Ы В А П
        "6_left_home_row": [
            "ф ы в а п ф ы в а п ф ы в а п ф ы в а п ф ы в а п ф ы в а п ф ы в а п",
            "п а в ы ф п а в ы ф п а в ы ф п а в ы ф п а в ы ф п а в ы ф п а в ы ф",
            "ффф ыыы ввв ааа ппп ффф ыыы ввв ааа ппп ффф ыыы ввв ааа ппп ффф ыыы",
            "фыва пфыва пфыва пфыва пфыва пфыва пфыва пфыва пфыва пфыва пфыва",
            "пф выа пф выа пф выа пф выа пф выа пф выа пф выа пф выа пф выа пф",
            "выафп выафп выафп выафп выафп выафп выафп выафп выафп выафп выафп",
            "ф ы в а п   ф ы в а п   ф ы в а п   ф ы в а п   ф ы в а п   ф ы в а",
            "фывапфывап фывапфывап фывапфывап фывапфывап фывапфывап фывапфыва"
        ],

        # Уровень 7: полный домашний ряд правой руки — Р О Л Д Ж Э
        "7_right_home_row": [
            "р о л д ж э р о л д ж э р о л д ж э р о л д ж э р о л д ж э р о л д ж э",
            "э ж д л о р э ж д л о р э ж д л о р э ж д л о р э ж д л о р э ж д л о р",
            "ррр ооо ллл ддд жжж эээ ррр ооо ллл ддд жжж эээ ррр ооо ллл ддд жжж",
            "ролджэ ролджэ ролджэ ролджэ ролджэ ролджэ ролджэ ролджэ ролджэ",
            "эждлор эждлор эждлор эждлор эждлор эждлор эждлор эждлор эждлор эждлор",
            "р о л д ж э   р о л д ж э   р о л д ж э   р о л д ж э   р о л д ж э",
            "ждлорэ ждлорэ ждлорэ ждлорэ ждлорэ ждлорэ ждлорэ ждлорэ ждлорэ ждло",
            "ролджэролджэ ролджэролджэ ролджэролджэ ролджэролджэ ролджэролджэ"
        ],

        # Уровень 8: верхний ряд левой руки — Й Ц У К Е
        "8_top_left": [
            "й ц у к е й ц у к е й ц у к е й ц у к е й ц у к е й ц у к е й ц у к е",
            "е к у ц й е к у ц й е к у ц й е к у ц й е к у ц й е к у ц й е к у ц й",
            "ййй ццц ууу ккк ееее ййй ццц ууу ккк ееее ййй ццц ууу ккк ееее ййй",
            "йцуке йцуке йцуке йцуке йцуке йцуке йцуке йцуке йцуке йцуке йцуке",
            "екуцй екуцй екуцй екуцй екуцй екуцй екуцй екуцй екуцй екуцй екуцй",
            "й ц у к е   й ц у к е   й ц у к е   й ц у к е   й ц у к е   й ц у к",
            "йцукейцуке йцукейцуке йцукейцуке йцукейцуке йцукейцуке йцукейцуке",
            "ф й ы ц в у а к п е ф й ы ц в у а к п е ф й ы ц в у а к п е ф й ы ц в"
        ],

        # Уровень 9: верхний ряд правой руки — Н Г Ш Щ З Х Ъ
        "9_top_right": [
            "н г ш щ з х ъ н г ш щ з х ъ н г ш щ з х ъ н г ш щ з х ъ н г ш щ з х ъ",
            "ъ х з щ ш г н ъ х з щ ш г н ъ х з щ ш г н ъ х з щ ш г н ъ х з щ ш г н",
            "ннн ггг шшш щщщ ззз ххх ъъъ ннн ггг шшш щщщ ззз ххх ъъъ ннн ггг шшш",
            "нгшщзхъ нгшщзхъ нгшщзхъ нгшщзхъ нгшщзхъ нгшщзхъ нгшщзхъ нгшщзхъ",
            "ъхзщшгн ъхзщшгн ъхзщшгн ъхзщшгн ъхзщшгн ъхзщшгн ъхзщшгн ъхзщшгн",
            "н г ш щ з   х ъ н г ш щ з   х ъ н г ш щ з   х ъ н г ш щ з   х ъ н г",
            "нгшщзхънгшщзхъ нгшщзхънгшщзхъ нгшщзхънгшщзхъ нгшщзхънгшщзхъ нгшщз",
            "р н о г л ш д щ ж з э х ъ р н о г л ш д щ ж з э х ъ р н о г л ш д щ ж"
        ],

        # Уровень 10: нижний ряд левой руки — Я Ч С М И
        "10_bottom_left": [
            "я ч с м и я ч с м и я ч с м и я ч с м и я ч с м и я ч с м и я ч с м и я ч с м и",
            "и м с ч я и м с ч я и м с ч я и м с ч я и м с ч я и м с ч я и м с ч я и м с ч я",
            "яяя ччч ссс ммм иии яяя ччч ссс ммм иии яяя ччч ссс ммм иии яяя ччч ссс",
            "ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячсми",
            "имсчя имсчя имсчя имсчя имсчя имсчя имсчя имсчя имсчя имсчя имсчя",
            "я ч с м и   я ч с м и   я ч с м и   я ч с м и   я ч с м и   я ч с м и",
            "ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячсми ячс",
            "ф я ы ч в с а м п и ф я ы ч в с а м п и ф я ы ч в с а м п и ф я ы ч в с"
        ],

        # Уровень 11: нижний ряд правой руки — Т Ь Б Ю .
        "11_bottom_right": [
            "т ь б ю . т ь б ю . т ь б ю . т ь б ю . т ь б ю . т ь б ю . т ь б ю .",
            ". ю б ь т . ю б ь т . ю б ь т . ю б ь т . ю б ь т . ю б ь т . ю б ь т",
            "ттт ььь ббб ююю ... ттт ььь ббб ююю ... ттт ььь ббб ююю ... ттт ььь ббб",
            "тьбю. тьбю. тьбю. тьбю. тьбю. тьбю. тьбю. тьбю. тьбю. тьбю. тьбю.",
            ".юбьт .юбьт .юбьт .юбьт .юбьт .юбьт .юбьт .юбьт .юбьт .юбьт .юбьт",
            "т ь б ю .   т ь б ю .   т ь б ю .   т ь б ю .   т ь б ю .   т ь б ю",
            "тьбю.тьбю. тьбю.тьбю. тьбю.тьбю. тьбю.тьбю. тьбю.тьбю. тьбю.тьбю.",
            "р т о ь л б д ю ж . э р т о ь л б д ю ж . э р т о ь л б д ю ж . э р т"
        ],

        # Уровень 12: цифровой ряд — 1 2 3 4 5 6 7 8 9 0
        "12_digits": [
            "1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5",
            "5 4 3 2 1 5 4 3 2 1 5 4 3 2 1 5 4 3 2 1 5 4 3 2 1 5 4 3 2 1 5 4 3 2 1",
            "111 222 333 444 555 111 222 333 444 555 111 222 333 444 555 111 222",
            "6 7 8 9 0 6 7 8 9 0 6 7 8 9 0 6 7 8 9 0 6 7 8 9 0 6 7 8 9 0 6 7 8 9 0",
            "0 9 8 7 6 0 9 8 7 6 0 9 8 7 6 0 9 8 7 6 0 9 8 7 6 0 9 8 7 6 0 9 8 7 6",
            "666 777 888 999 000 666 777 888 999 000 666 777 888 999 000 666 777",
            "1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5",
            "0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6"
        ],

        # Уровень 13: знаки препинания — , . ; : ? ! - _ = + ( ) [ ] { } " '
        "13_punctuation": [
            ", . , . , . , . , . , . , . , . , . , . , . , . , . , . , . , . , . , .",
            "; : ; : ; : ; : ; : ; : ; : ; : ; : ; : ; : ; : ; : ; : ; : ; : ; : ; :",
            "? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? ! ? !",
            "- _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _",
            "= + = + = + = + = + = + = + = + = + = + = + = + = + = + = + = + = + = +",
            "( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( )",
            "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]",
            "{ } { } { } { } { } { } { } { } { } { } { } { } { } { } { } { } { }"
        ],

        # Уровень 14: простые слова — 3-4 буквы
        "14_simple_words": [
            "мама папа мама папа мама папа мама папа мама папа мама папа мама папа",
            "дом дом дом дом дом дом дом дом дом дом дом дом дом дом дом дом дом дом",
            "кот кот кот кот кот кот кот кот кот кот кот кот кот кот кот кот кот кот",
            "сон сон сон сон сон сон сон сон сон сон сон сон сон сон сон сон сон сон",
            "мир мир мир мир мир мир мир мир мир мир мир мир мир мир мир мир мир мир",
            "сад сад сад сад сад сад сад сад сад сад сад сад сад сад сад сад сад сад",
            "лес лес лес лес лес лес лес лес лес лес лес лес лес лес лес лес лес лес",
            "вода вода вода вода вода вода вода вода вода вода вода вода вода вода"
        ],

        # Уровень 15: базовые предложения
        "15_basic_sentences": [
            "я иду домой я иду домой я иду домой я иду домой я иду домой я иду",
            "мы любим кота мы любим кота мы любим кота мы любим кота мы любим",
            "она читает книгу она читает книгу она читает книгу она читает книгу",
            "он пишет письмо он пишет письмо он пишет письмо он пишет письмо он",
            "дети играют в саду дети играют в саду дети играют в саду дети играют",
            "солнце светит ярко солнце светит ярко солнце светит ярко солнце све",
            "вода течёт в реку вода течёт в реку вода течёт в реку вода течёт в",
            "птицы поют в лесу птицы поют в лесу птицы поют в лесу птицы поют в"
        ],

        # Уровни 16-30: постепенное усложнение — слова, предложения, код
        "16_common_words": [
            "слепая печать слепая печать слепая печать слепая печать слепая печать",
            "мышечная память мышечная память мышечная память мышечная память мыше",
            "десять пальцев десять пальцев десять пальцев десять пальцев десять пал",
            "клавиатура текст клавиатура текст клавиатура текст клавиатура текст",
            "скорость точность скорость точность скорость точность скорость точно",
            "тренировка навык тренировка навык тренировка навык тренировка навык тр",
            "программист код программист код программист код программист код програ",
            "линукс терминал линукс терминал линукс терминал линукс терминал лину"
        ],
        "17_linux_commands": [
            "ls -la /home/user ls -la /home/user ls -la /home/user ls -la /home/use",
            "cd /var/log && pwd cd /var/log && pwd cd /var/log && pwd cd /var/log &&",
            "cat /etc/hosts cat /etc/hosts cat /etc/hosts cat /etc/hosts cat /etc/h",
            "grep error syslog grep error syslog grep error syslog grep error syslog",
            "sudo apt update sudo apt update sudo apt update sudo apt update sudo apt",
            "git status git status git status git status git status git status git sta",
            "docker ps -a docker ps -a docker ps -a docker ps -a docker ps -a docker ps",
            "kubectl get pods kubectl get pods kubectl get pods kubectl get pods kubec"
        ],
        "18_python_basics": [
            "print hello world print hello world print hello world print hello world",
            "for i in range 10 for i in range 10 for i in range 10 for i in range 1",
            "def func x return x def func x return x def func x return x def func x",
            "import os sys import os sys import os sys import os sys import os sys",
            "if x 0 return True if x 0 return True if x 0 return True if x 0 return Tr",
            "list comp x for x in list comp x for x in list comp x for x in list comp",
            "try except finally try except finally try except finally try except finall",
            "class MyClass def init class MyClass def init class MyClass def init clas"
        ],
        "19_sentences_ru": [
            "Съешь ещё этих мягких французских булок да выпей чаю Съешь ещё этих мя",
            "В чащах юга жил бы цитрус но фальшивый экземпляр В чащах юга жил бы",
            "Любя съесть булку из хлеба да выпить чаю быстро Любя съесть булку из",
            "Почему бы не взять ёжика и не отвезти его в зоопарк Почему бы не взять",
            "Широкая электрификация южных губерний даст мощный толчок Широкая элект",
            "Вьюжный февральский вечер за окном и тёплый чай в кружке Вьюжный февра",
            "Завтра пойдём в парк покормить уток и посмотреть на пруд Завтра пойдём в",
            "Каждый программист должен знать основы слепой печати Каждый программи"
        ],
        "20_sentences_en_translit": [
            "the quick brown fox jumps over the lazy dog the quick brown fox jumps ov",
            "pack my box with five dozen liquor jugs pack my box with five dozen liq",
            "how vexingly quick daft zebras jump how vexingly quick daft zebras jump",
            "sphinx of black quartz judge my vow sphinx of black quartz judge my vow",
            "cozy lummox gives smart squid who asks for job cozy lummox gives smart s",
            "grumpy wizards make toxic brew for the evil queen grumpy wizards make to",
            "linux ubuntu debian arch fedora linux ubuntu debian arch fedora linux ubu",
            "vim nano emacs sublime vscode vim nano emacs sublime vscode vim nano emac"
        ],
        "21_json_yaml_snippets": [
            "name nginx replicas 3 port 80 name nginx replicas 3 port 80 name nginx repl",
            "apiVersion v1 kind Pod metadata name nginx apiVersion v1 kind Pod metadata",
            "server listen 80 location proxy_pass http app server listen 80 location pr",
            "upstream backend server 127 0 0 1 8080 upstream backend server 127 0 0 1 80",
            "- name install deps apt pkg python3 pip - name install deps apt pkg python",
            "labels app kubernetes io name nginx labels app kubernetes io name nginx l",
            "env prod config debug false env prod config debug false env prod config de",
            "spec containers name nginx image nginx 1 25 spec containers name nginx im"
        ],
        "22_git_commands": [
            "git commit -am fix typo git commit -am fix typo git commit -am fix typo gi",
            "git rebase -i HEAD 3 git rebase -i HEAD 3 git rebase -i HEAD 3 git rebase",
            "git cherry pick abc123 git cherry pick abc123 git cherry pick abc123 git c",
            "git bisect start bad good git bisect start bad good git bisect start bad g",
            "git submodule update init git submodule update init git submodule update i",
            "git worktree add feature git worktree add feature git worktree add feature",
            "git stash pop apply git stash pop apply git stash pop apply git stash pop a",
            "git log oneline graph git log oneline graph git log oneline graph git log"
        ],
        "23_docker_k8s": [
            "docker run rm it v pwd src python bash docker run rm it v pwd src pytho",
            "docker build t app latest docker build t app latest docker build t app late",
            "kubectl get nodes o wide kubectl get nodes o wide kubectl get nodes o wide",
            "kubectl describe pod my pod kubectl describe pod my pod kubectl describe p",
            "helm repo add bitnami https charts bitnami com helm repo add bitnami http",
            "kind create cluster name dev kind create cluster name dev kind create clus",
            "istioctl install set profile demo istioctl install set profile demo istioc",
            "flux create source git repo url https github com flux create source git re"
        ],
        "24_python_syntax": [
            "def factorial n return 1 if n 0 else n factorial n 1 def factorial n retur",
            "nums x 2 for x in range 10 if x 2 0 nums x 2 for x in range 10 if x 2 0",
            "with open file txt r as f data f read with open file txt r as f data f re",
            "class Person def init self name self name name class Person def init self",
            "import numpy as np arr np array 1 2 3 import numpy as np arr np array 1 2",
            "lambda x y x y 2 lambda x y x y 2 lambda x y x y 2 lambda x y x y 2 lambda",
            "try result 10 0 except ZeroDivisionError print err try result 10 0 except",
            "from collections import defaultdict d defaultdict list from collections imp"
        ],
        "25_advanced_ru": [
            "Разработка программного обеспечения требует внимательности и практики Разр",
            "Слепая печать позволяет программисту не отвлекаться от экрана монитора Сле",
            "Десятипальцевый метод осваивается за две-три недели регулярных тренировок",
            "Каждый палец отвечает за определённые клавиши на клавиатуре компьютера К",
            "Мышечная память формируется через повторение одних и тех же движений Мыш",
            "Оптимальная скорость печати для программиста составляет 250-300 зн в минут",
            "Регулярные тренировки по 15 минут в день дают лучший результат чем редкие",
            "Использование правильной постановки рук предотвращает усталость и травмы"
        ],
        "26_advanced_en": [
            "Software development requires constant practice and attention to detail Soft",
            "Touch typing allows programmers to keep their eyes on the screen at all tim",
            "The ten finger method can be mastered in two to three weeks of daily pract",
            "Each finger is responsible for specific keys on the computer keyboard Each",
            "Muscle memory is formed through repetition of the same finger movements Mu",
            "Optimal typing speed for programmers is 250 300 characters per minute Opti",
            "Daily 15 minute practice sessions yield better results than infrequent long",
            "Proper hand positioning prevents fatigue and repetitive strain injuries Pro"
        ],
        "27_code_mix_ru_en": [
            "def привет мир print Привет Мир привет мир привет мир привет мир привет ми",
            "class User models Model email models CharField max_length 255 class User",
            "SELECT name email FROM users WHERE active True SELECT name email FROM user",
            "curl X POST https api example com v1 data curl X POST https api example com",
            "docker compose up d nginx postgres redis docker compose up d nginx postgres",
            "ansible playbook site yml i production ansible playbook site yml i product",
            "kubectl apply f deployment yaml f service yaml kubectl apply f deployment y",
            "git clone https github com user repo cd repo git clone https github com user"
        ],
        "28_long_sentences": [
            "Слепая печать это навык набора текста на клавиатуре без необходимости смотреть на клавиши Слепая печать это навык набора текста на клавиатуре без необходимости смотреть на клавиши Слепая печать это навык набора текста на клавиатуре без необходимости смотреть на клавиши",
            "Десятипальцевый метод предполагает что каждый палец отвечает за определённую группу клавиш Десятипальцевый метод предполагает что каждый палец отвечает за определённую группу клавиш Десятипальцевый метод предполагает что каждый палец отвечает за определённую группу клавиш",
            "Регулярная практика по пятнадцать минут в день поможет освоить слепую печать за две недели Регулярная практика по пятнадцать минут в день поможет освоить слепую печать за две недели Регулярная практика по пятнадцать минут в день поможет освоить слепую печать за две недели",
            "Программисты которые владеют слепой печатью работают быстрее и реже допускают ошибки Программисты которые владеют слепой печатью работают быстрее и реже допускают ошибки Программисты которые владеют слепой печатью работают быстрее и реже допускают ошибки"
        ],
        "29_full_keyboard": [
            "йцукенгшщзхъфывапролджэячсмитьбю.1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\ йцукенгшщзхъфывапролджэячсмитьбю.1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\ йцукенгшщзхъфывапролджэячсмитьбю.1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\",
            "ёйцукенгшщзхъфывапролджэячсмитьбю. ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ, ёйцукенгшщзхъфывапролджэячсмитьбю. ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ, ёйцукенгшщзхъфывапролджэячсмитьбю. ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,",
            "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890!@#$%^&*()_+-=`~ QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>? qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890!@#$%^&*()_+-=`~ QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?",
            "touch typing muscle memory ten fingers keyboard layout blind typing practice touch typing muscle memory ten fingers keyboard layout blind typing practice touch typing muscle memory ten fingers keyboard layout blind typing practice"
        ],
        "30_mastery": [
            "Слепая печать это фундаментальный навык для любого программиста который хочет работать эффективно и без усталости Слепая печать это фундаментальный навык для любого программиста который хочет работать эффективно и без усталости Слепая печать это фундаментальный навык для любого программиста который хочет работать эффективно и без усталости",
            "Мышечная память формируется через ежедневные тренировки по 15 20 минут в течение двух трёх недель после чего набор текста становится автоматическим и не требует концентрации внимания на клавиатуре Мышечная память формируется через ежедневные тренировки по 15 20 минут в течение двух трёх недель после чего набор текста становится автоматическим и не требует концентрации внимания на клавиатуре",
            "Правильная постановка рук на домашнем ряду фыва олджэ позволяет минимизировать движения пальцев и достигать максимальной скорости набора при минимальной усталости Правильная постановка рук на домашнем ряду фыва олджэ позволяет минимизировать движения пальцев и достигать максимальной скорости набора при минимальной усталости",
            "Освоив слепую печать вы сможете полностью сконцентрироваться на решении задач а не на поиске клавиш что особенно важно при программировании отладке кода и работе с терминалом Освоив слепую печать вы сможете полностью сконцентрироваться на решении задач а не на поиске клавиш что особенно важно при программировании отладке кода и работе с терминалом"
        ]
    },
    "advanced": {
        # Продвинутые уровни — реальный код, длинные тексты, смешанные языки
        "1_bash_scripts": [
            "for file in * do if grep -q TODO $file then echo Found in $file fi done for file in * do if grep -q TODO $file then echo Found in $file fi done for file in * do if grep -q TODO $file then echo Found in $file fi done",
            "while read line do echo Processing $line sleep 0.1 done < input.txt while read line do echo Processing $line sleep 0.1 done < input.txt while read line do echo Processing $line sleep 0.1 done < input.txt",
            "find /var/log -name *.log -mtime -7 -exec gzip {} \\; find /var/log -name *.log -mtime -7 -exec gzip {} \\; find /var/log -name *.log -mtime -7 -exec gzip {} \\; find /var/log -name *.log -mtime -7 -exec gzip {} \\;",
            "rsync -avz --exclude '*.tmp' --delete /src/ user@host:/dst/ rsync -avz --exclude '*.tmp' --delete /src/ user@host:/dst/ rsync -avz --exclude '*.tmp' --delete /src/ user@host:/dst/",
            "tar -czf backup-$(date +%Y%m%d).tar.gz /home/user tar -czf backup-$(date +%Y%m%d).tar.gz /home/user tar -czf backup-$(date +%Y%m%d).tar.gz /home/user tar -czf backup-$(date +%Y%m%d).tar.gz /home/user",
            "ssh -i ~/.ssh/id_rsa user@host 'sudo systemctl restart nginx' ssh -i ~/.ssh/id_rsa user@host 'sudo systemctl restart nginx' ssh -i ~/.ssh/id_rsa user@host 'sudo systemctl restart nginx'",
            "curl -s https://api.github.com/repos/user/repo/releases/latest | jq -r .tag_name curl -s https://api.github.com/repos/user/repo/releases/latest | jq -r .tag_name curl -s https://api.github.com/repos/user/repo/releases/latest | jq -r .tag_name",
            "docker run --rm -v $(pwd):/work -w /work python:3.12 python script.py docker run --rm -v $(pwd):/work -w /work python:3.12 python script.py docker run --rm -v $(pwd):/work -w /work python:3.12 python script.py"
        ],
        "2_git_workflows": [
            "git checkout -b feature/login && git add . && git commit -m feat add login page && git push -u origin feature/login git checkout -b feature/login && git add . && git commit -m feat add login page && git push -u origin feature/login",
            "git fetch origin && git rebase origin/main && git push --force-with-lease git fetch origin && git rebase origin/main && git push --force-with-lease git fetch origin && git rebase origin/main && git push --force-with-lease",
            "git log --oneline --graph --all --decorate git log --oneline --graph --all --decorate git log --oneline --graph --all --decorate git log --oneline --graph --all --decorate git log --oneline --graph --all --decorate",
            "git diff HEAD~1 --stat && git diff HEAD~1 --name-only git diff HEAD~1 --stat && git diff HEAD~1 --name-only git diff HEAD~1 --stat && git diff HEAD~1 --name-only git diff HEAD~1 --stat && git diff HEAD~1 --name-only",
            "git cherry-pick abc123 def456 && git push origin main git cherry-pick abc123 def456 && git push origin main git cherry-pick abc123 def456 && git push origin main git cherry-pick abc123 def456 && git push origin main",
            "git bisect start && git bisect bad && git bisect good v1.0.0 && git bisect run pytest tests/ git bisect start && git bisect bad && git bisect good v1.0.0 && git bisect run pytest tests/",
            "git submodule add https://github.com/user/lib.git vendor/lib && git commit -m add submodule git submodule add https://github.com/user/lib.git vendor/lib && git commit -m add submodule",
            "git worktree add ../hotfix-1.2.3 v1.2.3 && cd ../hotfix-1.2.3 && git checkout -b hotfix/fix-critical git worktree add ../hotfix-1.2.3 v1.2.3 && cd ../hotfix-1.2.3 && git checkout -b hotfix/fix-critical"
        ],
        "3_k8s_yaml": [
            "apiVersion apps/v1 kind Deployment metadata name nginx-deployment spec replicas 3 selector matchLabels app nginx template metadata labels app nginx spec containers - name nginx image nginx 1 25 ports - containerPort 80 apiVersion apps/v1 kind Deployment metadata name nginx-deployment spec replicas 3 selector matchLabels app nginx template metadata labels app nginx spec containers - name nginx image nginx 1 25 ports - containerPort 80",
            "apiVersion v1 kind Service metadata name nginx-service spec selector app nginx ports - protocol TCP port 80 targetPort 80 type LoadBalancer apiVersion v1 kind Service metadata name nginx-service spec selector app nginx ports - protocol TCP port 80 targetPort 80 type LoadBalancer",
            "apiVersion networking k8s io/v1 kind Ingress metadata name nginx-ingress spec rules - host example com http paths - path / pathType Prefix backend service name nginx-service port number 80 apiVersion networking k8s io/v1 kind Ingress metadata name nginx-ingress spec rules - host example com http paths - path / pathType Prefix backend service name nginx-service port number 80",
            "apiVersion batch/v1 kind CronJob metadata name backup-cron spec schedule 0 2 * * * jobTemplate spec template spec containers - name backup image alpine command - /bin/sh - -c - mysqldump -u root -p$MYSQL_PASSWORD db > /backup/db.sql restartPolicy OnFailure apiVersion batch/v1 kind CronJob metadata name backup-cron spec schedule 0 2 * * * jobTemplate spec template spec containers - name backup image alpine command - /bin/sh - -c - mysqldump -u root -p$MYSQL_PASSWORD db > /backup/db.sql restartPolicy OnFailure"
        ],
        "4_python_advanced": [
            "@dataclass class User id int name str email str created_at datetime @dataclass class User id int name str email str created_at datetime @dataclass class User id int name str email str created_at datetime @dataclass class User id int name str email str created_at datetime",
            "async def fetch_data url async with aiohttp ClientSession as session async with session get url as resp return await resp json async def fetch_data url async with aiohttp ClientSession as session async with session get url as resp return await resp json",
            "result = [x**2 for x in range(100) if x % 2 == 0] result = [x**2 for x in range(100) if x % 2 == 0] result = [x**2 for x in range(100) if x % 2 == 0] result = [x**2 for x in range(100) if x % 2 == 0] result = [x**2 for x in range(100) if x % 2 == 0]",
            "with ThreadPoolExecutor max_workers 4 as executor futures = executor map process_file files results = [f result for f in futures] with ThreadPoolExecutor max_workers 4 as executor futures = executor map process_file files results = [f result for f in futures]",
            "class Database metaclass=Singleton def __init__ self self connection = None class Database metaclass=Singleton def __init__ self self connection = None class Database metaclass=Singleton def __init__ self self connection = None",
            "def retry max_attempts 3 def decorator func @wraps func def wrapper *args **kwargs for attempt in range max_attempts try return func *args **kwargs except Exception as e if attempt == max_attempts 1 raise e time sleep 2 ** attempt return wrapper return decorator def retry max_attempts 3 def decorator func @wraps func def wrapper *args **kwargs for attempt in range max_attempts try return func *args **kwargs except Exception as e if attempt == max_attempts 1 raise e time sleep 2 ** attempt return wrapper return decorator"
        ],
        "5_prose_ru": [
            "Слепая печать — это метод набора текста на клавиатуре без зрительного контроля положения пальцев. Основная идея заключается в том, что каждый палец отвечает за определённую группу клавиш, а руки находятся в базовой позиции на домашнем ряду. Благодаря этому методу достигается высокая скорость набора и снижается утомляемость при длительной работе за компьютером. Слепая печать особенно важна для программистов, писателей и всех, чья работа связана с интенсивным использованием клавиатуры. Слепая печать — это метод набора текста на клавиатуре без зрительного контроля положения пальцев. Основная идея заключается в том, что каждый палец отвечает за определённую группу клавиш, а руки находятся в базовой позиции на домашнем ряду.",
            "Десятипальцевый метод набора был разработан в конце XIX века вместе с изобретением пишущей машинки. Раскладка клавиш была специально спроектирована так, чтобы наиболее часто используемые буквы располагались под сильными пальцами, а редкие — под слабыми. Это позволяло избежать заедания рычагов в механических машинках. Современные клавиатуры сохранили эту раскладку по инерции, хотя технической необходимости в ней больше нет. Тем не менее, десятипальцевый метод остаётся самым эффективным способом набора текста и сегодня. Десятипальцевый метод набора был разработан в конце XIX века вместе с изобретением пишущей машинки. Раскладка клавиш была специально спроектирована так, чтобы наиболее часто используемые буквы располагались под сильными пальцами, а редкие — под слабыми.",
            "Для освоения слепой печати требуется регулярная практика в течение двух-трёх недель. Ежедневные занятия по 15–20 минут дают лучший результат, чем редкие длительные сессии. Важно не пытаться сразу набирать быстро — сначала нужно выработать правильную постановку рук и точность, скорость придёт автоматически через мышечную память. Не смотрите на клавиатуру даже если ошиблись — исправляйте ошибки на ощупь. Это ключевой принцип формирования навыка слепого набора. Для освоения слепой печати требуется регулярная практика в течение двух-трёх недель. Ежедневные занятия по 15–20 минут дают лучший результат, чем редкие длительные сессии.",
            "Преимущества слепой печати очевидны: увеличение скорости набора до 300–400 знаков в минуту, снижение усталости глаз и рук, возможность полностью концентрироваться на содержании текста, а не на поиске клавиш. Для программистов это особенно ценно — они могут не отвлекаться от экрана кода, что повышает продуктивность и снижает количество ошибок. Даже если вы не планируете становиться профессиональным печатником, базовые навыки слепой печати значительно упростят повседневную работу за компьютером. Преимущества слепой печати очевидны: увеличение скорости набора до 300–400 знаков в минуту, снижение усталости глаз и рук, возможность полностью концентрироваться на содержании текста, а не на поиске клавиш."
        ],
        "6_prose_en": [
            "Touch typing is a technique where the typist uses all ten fingers without looking at the keyboard. The fingers rest on the home row keys, and each finger is responsible for a specific set of keys. This method allows for significantly higher typing speeds and reduces fatigue during prolonged typing sessions. Touch typing is especially valuable for programmers, writers, and anyone who spends significant time working with text on a computer. With practice, touch typing becomes automatic, allowing the brain to focus on content creation rather than mechanical key pressing. Touch typing is a technique where the typist uses all ten fingers without looking at the keyboard. The fingers rest on the home row keys, and each finger is responsible for a specific set of keys.",
            "The ten-finger typing method was developed in the late 19th century alongside the invention of the typewriter. The QWERTY layout was specifically designed to prevent mechanical jams in early typewriters by separating commonly used letter pairs. Although modern keyboards no longer suffer from this mechanical limitation, the layout has persisted due to convention. Despite its historical quirks, the ten-finger method remains the most efficient way to type on a standard keyboard layout today. Learning proper finger placement and technique is more important than the specific keyboard layout used. The ten-finger typing method was developed in the late 19th century alongside the invention of the typewriter.",
            "Mastering touch typing typically requires two to three weeks of consistent daily practice. Short daily sessions of 15–20 minutes are more effective than infrequent longer sessions. It is crucial not to focus on speed initially — accuracy and proper hand positioning must come first. Speed will naturally develop through muscle memory as the neural pathways strengthen with repetition. Never look at the keyboard even when making mistakes — correct errors by feel. This discipline is essential for developing true touch typing proficiency. Mastering touch typing typically requires two to three weeks of consistent daily practice. Short daily sessions of 15–20 minutes are more effective than infrequent longer sessions.",
            "The benefits of touch typing are substantial: typing speeds of 60–80 words per minute become achievable, eye strain and hand fatigue decrease significantly, and mental focus shifts entirely to content creation rather than mechanical key location. For programmers, this means maintaining concentration on code logic without breaking flow to hunt for keys. Even casual computer users will find their productivity enhanced and frustration reduced after acquiring basic touch typing skills. The initial investment of two to three weeks of practice pays dividends throughout one's entire computing career. The benefits of touch typing are substantial: typing speeds of 60–80 words per minute become achievable, eye strain and hand fatigue decrease significantly."
        ],
        "7_mixed_code_text": [
            "class ArticleViewSet ViewSet queryset Article objects all serializer_class ArticleSerializer def list self request queryset self filter_queryset self get_queryset serializer self get_serializer queryset many True return Response serializer data class ArticleViewSet ViewSet queryset Article objects all serializer_class ArticleSerializer def list self request queryset self filter_queryset self get_queryset serializer self get_serializer queryset many True return Response serializer data",
            "SELECT u id u name COUNT o id AS orders FROM users u LEFT JOIN orders o ON u id o user_id WHERE u created_at 2023 01 01 GROUP BY u id u name HAVING COUNT o id 5 ORDER BY orders DESC SELECT u id u name COUNT o id AS orders FROM users u LEFT JOIN orders o ON u id o user_id WHERE u created_at 2023 01 01 GROUP BY u id u name HAVING COUNT o id 5 ORDER BY orders DESC",
            "const handleSubmit = async e => { e preventDefault ; try { const res = await fetch '/api/login' { method 'POST' headers { 'Content-Type' 'application/json' } body JSON stringify { email password } } ; if res ok navigate '/dashboard' ; else setError 'Invalid credentials' ; } catch err { setError 'Network error' ; console error err ; } } ; const handleSubmit = async e => { e preventDefault ; try { const res = await fetch '/api/login' { method 'POST' headers { 'Content-Type' 'application/json' } body JSON stringify { email password } } ; if res ok navigate '/dashboard' ; else setError 'Invalid credentials' ; } catch err { setError 'Network error' ; console error err ; } } ;",
            "docker-compose.yml version '3.8' services web build context . dockerfile Dockerfile ports - '8000 8000' volumes - . /app env_file - .env db image postgres 15 environment POSTGRES_DB mydb POSTGRES_USER user POSTGRES_PASSWORD secret redis image redis 7 alpine ports - '6379 6379' docker-compose.yml version '3.8' services web build context . dockerfile Dockerfile ports - '8000 8000' volumes - . /app env_file - .env db image postgres 15 environment POSTGRES_DB mydb POSTGRES_USER user POSTGRES_PASSWORD secret redis image redis 7 alpine ports - '6379 6379'"
        ],
        "8_speed_mastery": [
            "йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.йцукенгшщзхъфывапролджэячсмитьбю.",
            "qwertyuiop[]asdfghjkl;'zxcvbnm,./qwertyuiop[]asdfghjkl;'zxcvbnm,./qwertyuiop[]asdfghjkl;'zxcvbnm,./qwertyuiop[]asdfghjkl;'zxcvbnm,./qwertyuiop[]asdfghjkl;'zxcvbnm,./qwertyuiop[]asdfghjkl;'zxcvbnm,./qwertyuiop[]asdfghjkl;'zxcvbnm,./qwertyuiop[]asdfghjkl;'zxcvbnm,./qwertyuiop[]asdfghjkl;'zxcvbnm,./",
            "1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\1234567890!@#$%^&*()_+-=[]{};:',.<>?/\\",
            "the quick brown fox jumps over the lazy dog THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG 1234567890 the quick brown fox jumps over the lazy dog THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG 1234567890 the quick brown fox jumps over the lazy dog THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG 1234567890"
        ],
        "9_linux_admin": [
            "journalctl -u nginx --since yesterday | grep -i error | awk '{print $1, $2, $5}' | sort | uniq -c | sort -rn journalctl -u nginx --since yesterday | grep -i error | awk '{print $1, $2, $5}' | sort | uniq -c | sort -rn journalctl -u nginx --since yesterday | grep -i error | awk '{print $1, $2, $5}' | sort | uniq -c | sort -rn",
            "iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP",
            "for user in $(cut -d: -f1 /etc/passwd); do echo -n $user: ; groups $user | cut -d: -f2 ; done | column -t for user in $(cut -d: -f1 /etc/passwd); do echo -n $user: ; groups $user | cut -d: -f2 ; done | column -t for user in $(cut -d: -f1 /etc/passwd); do echo -n $user: ; groups $user | cut -d: -f2 ; done | column -t",
            "find /home -type f -name '*.log' -mtime +30 -exec rm -f {} \\; && echo Cleanup complete at $(date) >> /var/log/cleanup.log find /home -type f -name '*.log' -mtime +30 -exec rm -f {} \\; && echo Cleanup complete at $(date) >> /var/log/cleanup.log"
        ],
        "10_python_ds": [
            "def dijkstra graph start distances {node float('inf') for node in graph} distances start 0 pq [(0 start)] while pq curr_dist curr_node heapq heappop pq if curr_dist distances curr_node continue for neighbor weight in graph curr_node items new_dist curr_dist + weight if new_dist < distances neighbor distances neighbor new_dist heapq heappush pq (new_dist neighbor) return distances def dijkstra graph start distances {node float('inf') for node in graph} distances start 0 pq [(0 start)] while pq curr_dist curr_node heapq heappop pq if curr_dist distances curr_node continue for neighbor weight in graph curr_node items new_dist curr_dist + weight if new_dist < distances neighbor distances neighbor new_dist heapq heappush pq (new_dist neighbor) return distances",
            "class TrieNode __init__ self self children {} self is_end False class Trie __init__ self self root TrieNode def insert self word node self root for char in word if char not in node children node children char TrieNode node node children char node is_end True def search self word node self root for char in word if char not in node children return False node node children char return node is_end class TrieNode __init__ self self children {} self is_end False class Trie __init__ self self root TrieNode def insert self word node self root for char in word if char not in node children node children char TrieNode node node children char node is_end True def search self word node self root for char in word if char not in node children return False node node children char return node is_end",
            "def quicksort arr if len arr <= 1 return arr pivot arr len arr // 2 left [x for x in arr if x < pivot] middle [x for x in arr if x == pivot] right [x for x in arr if x > pivot] return quicksort left + middle + quicksort right def quicksort arr if len arr <= 1 return arr pivot arr len arr // 2 left [x for x in arr if x < pivot] middle [x for x in arr if x == pivot] right [x for x in arr if x > pivot] return quicksort left + middle + quicksort right",
            "@lru_cache maxsize None def fib n if n < 2 return n return fib n 1 + fib n 2 dp [0] * (n+1) dp 1 1 for i in range 2 n+1 dp i dp i 1 + dp i 2 return dp n @lru_cache maxsize None def fib n if n < 2 return n return fib n 1 + fib n 2 dp [0] * (n+1) dp 1 1 for i in range 2 n+1 dp i dp i 1 + dp i 2 return dp n"
        ],
        "11_web_dev": [
            "const app = express ; app use cors ; app use express json ; app use '/api' apiRoutes ; app use errorHandler ; app listen process env PORT || 3000 () => console log Server running on port ${process env PORT || 3000} ) ; const app = express ; app use cors ; app use express json ; app use '/api' apiRoutes ; app use errorHandler ; app listen process env PORT || 3000 () => console log Server running on port ${process env PORT || 3000} ) ;",
            "<div className='container' onClick={() => setShow(!show)}><header className='header'><nav className='nav'><ul className='nav-list'>{links.map((link) => (<li key={link.id} className={`nav-item ${active === link.id ? 'active' : ''}`}><a href={link.href} className='nav-link'>{link.text}</a></li>))}</ul></nav></header></div> <div className='container' onClick={() => setShow(!show)}><header className='header'><nav className='nav'><ul className='nav-list'>{links.map((link) => (<li key={link.id} className={`nav-item ${active === link.id ? 'active' : ''}`}><a href={link.href} className='nav-link'>{link.text}</a></li>))}</ul></nav></header></div>",
            ".container { display grid; grid-template-columns repeat(auto-fit minmax(300px 1fr)); gap 2rem; padding 2rem; } .card { background #fff; border-radius 8px; box-shadow 0 4px 6px rgba(0 0 0 0.1); transition transform 0.3s ease; } .card:hover { transform translateY(-5px); box-shadow 0 10px 15px rgba(0 0 0 0.2); } @media (max-width 768px) { .container { grid-template-columns 1fr; } } .container { display grid; grid-template-columns repeat(auto-fit minmax(300px 1fr)); gap 2rem; padding 2rem; } .card { background #fff; border-radius 8px; box-shadow 0 4px 6px rgba(0 0 0 0.1); transition transform 0.3s ease; } .card:hover { transform translateY(-5px); box-shadow 0 10px 15px rgba(0 0 0 0.2); } @media (max-width 768px) { .container { grid-template-columns 1fr; } }",
            "async function fetchData() { try { const response = await fetch('https://api.example.com/data'); if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`); const data = await response.json(); setData(data); setLoading(false); } catch (error) { setError(error.message); setLoading(false); } finally { setLoading(false); } } useEffect(() => { fetchData(); }, []); async function fetchData() { try { const response = await fetch('https://api.example.com/data'); if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`); const data = await response.json(); setData(data); setLoading(false); } catch (error) { setError(error.message); setLoading(false); } finally { setLoading(false); } } useEffect(() => { fetchData(); }, []);"
        ],
        "12_sql_queries": [
            "WITH RECURSIVE category_tree AS ( SELECT id name parent_id 0 AS depth FROM categories WHERE parent_id IS NULL UNION ALL SELECT c id c name c parent_id ct depth + 1 FROM categories c INNER JOIN category_tree ct ON c parent_id = ct id ) SELECT * FROM category_tree ORDER BY depth name WITH RECURSIVE category_tree AS ( SELECT id name parent_id 0 AS depth FROM categories WHERE parent_id IS NULL UNION ALL SELECT c id c name c parent_id ct depth + 1 FROM categories c INNER JOIN category_tree ct ON c parent_id = ct id ) SELECT * FROM category_tree ORDER BY depth name",
            "SELECT DATE_TRUNC('day' created_at) AS day COUNT DISTINCT user_id AS dau AVG session_duration AS avg_session FROM user_sessions WHERE created_at >= CURRENT_DATE - INTERVAL '30 days' GROUP BY DATE_TRUNC('day' created_at) ORDER BY day DESC LIMIT 30 SELECT DATE_TRUNC('day' created_at) AS day COUNT DISTINCT user_id AS dau AVG session_duration AS avg_session FROM user_sessions WHERE created_at >= CURRENT_DATE - INTERVAL '30 days' GROUP BY DATE_TRUNC('day' created_at) ORDER BY day DESC LIMIT 30",
            "UPDATE products p SET price = price * 0.9 WHERE EXISTS ( SELECT 1 FROM categories c JOIN category_discounts cd ON c id = cd category_id WHERE c id = p category_id AND cd discount_percent >= 10 AND cd active = true AND cd valid_until > CURRENT_DATE ) RETURNING p id p name p price UPDATE products p SET price = price * 0.9 WHERE EXISTS ( SELECT 1 FROM categories c JOIN category_discounts cd ON c id = cd category_id WHERE c id = p category_id AND cd discount_percent >= 10 AND cd active = true AND cd valid_until > CURRENT_DATE ) RETURNING p id p name p price",
            "SELECT u email u created_at COUNT o id FILTER (WHERE o status = 'completed') AS completed_orders COUNT o id FILTER (WHERE o status = 'cancelled') AS cancelled_orders SUM o amount FILTER (WHERE o status = 'completed') AS total_spent FROM users u LEFT JOIN orders o ON u id = o user_id WHERE u created_at >= '2023-01-01' GROUP BY u id u email u created_at HAVING COUNT o id FILTER (WHERE o status = 'completed') > 5 ORDER BY total_spent DESC LIMIT 100 SELECT u email u created_at COUNT o id FILTER (WHERE o status = 'completed') AS completed_orders COUNT o id FILTER (WHERE o status = 'cancelled') AS cancelled_orders SUM o amount FILTER (WHERE o status = 'completed') AS total_spent FROM users u LEFT JOIN orders o ON u id = o user_id WHERE u created_at >= '2023-01-01' GROUP BY u id u email u created_at HAVING COUNT o id FILTER (WHERE o status = 'completed') > 5 ORDER BY total_spent DESC LIMIT 100"
        ],
        "13_terminal_mastery": [
            "tmux new-session -s dev \\; split-window -h \\; split-window -v \\; select-pane -t 0 \\; send-keys 'vim main.py' C-m \\; select-pane -t 1 \\; send-keys 'python -m pytest -xvs' C-m \\; select-pane -t 2 \\; send-keys 'git status' C-m tmux new-session -s dev \\; split-window -h \\; split-window -v \\; select-pane -t 0 \\; send-keys 'vim main.py' C-m \\; select-pane -t 1 \\; send-keys 'python -m pytest -xvs' C-m \\; select-pane -t 2 \\; send-keys 'git status' C-m",
            "fzf --preview 'bat --color=always {}' --bind 'enter:execute(vim {})' --height 40% --layout=reverse --border fzf --preview 'bat --color=always {}' --bind 'enter:execute(vim {})' --height 40% --layout=reverse --border fzf --preview 'bat --color=always {}' --bind 'enter:execute(vim {})' --height 40% --layout=reverse --border",
            "rg --type py --hidden --glob '!.git' 'def.*request' --pretty | fzf --multi --preview 'bat --color=always --line-range {1}: {2} {3}' rg --type py --hidden --glob '!.git' 'def.*request' --pretty | fzf --multi --preview 'bat --color=always --line-range {1}: {2} {3}' rg --type py --hidden --glob '!.git' 'def.*request' --pretty | fzf --multi --preview 'bat --color=always --line-range {1}: {2} {3}'",
            "watch -n 0.5 'ps aux | grep python | grep -v grep | awk \"{print $2, $3, $4, $11}\" | column -t' watch -n 0.5 'ps aux | grep python | grep -v grep | awk \"{print $2, $3, $4, $11}\" | column -t' watch -n 0.5 'ps aux | grep python | grep -v grep | awk \"{print $2, $3, $4, $11}\" | column -t'"
        ],
        "14_algo_interview": [
            "def longest_substring_without_repeating_chars s char_index_map {} left = 0 max_length = 0 for right char in enumerate s if char in char_index_map and char_index_map char >= left left = char_index_map char + 1 char_index_map char = right max_length = max max_length right - left + 1 return max_length def longest_substring_without_repeating_chars s char_index_map {} left = 0 max_length = 0 for right char in enumerate s if char in char_index_map and char_index_map char >= left left = char_index_map char + 1 char_index_map char = right max_length = max max_length right - left + 1 return max_length",
            "def merge_k_sorted_lists lists if not lists return None if len lists == 1 return lists 0 mid = len lists // 2 left = merge_k_sorted_lists lists :mid right = merge_k_sorted_lists lists mid: return merge_two_lists left right def merge_two_lists l1 l2 dummy = ListNode 0 curr = dummy while l1 and l2 if l1 val < l2 val curr next = l1 l1 = l1 next else curr next = l2 l2 = l2 next curr = curr next curr next = l1 or l2 return dummy next def merge_k_sorted_lists lists if not lists return None if len lists == 1 return lists 0 mid = len lists // 2 left = merge_k_sorted_lists lists :mid right = merge_k_sorted_lists lists mid: return merge_two_lists left right",
            "def max_profit prices if not prices return 0 min_price = float('inf') max_profit = 0 for price in prices min_price = min min_price price max_profit = max max_profit price - min_price return max_profit def max_profit prices if not prices return 0 min_price = float('inf') max_profit = 0 for price in prices min_price = min min_price price max_profit = max max_profit price - min_price return max_profit",
            "def word_break s wordDict word_set = set wordDict dp = [False] * (len s + 1) dp 0 = True for i in range 1 len s + 1 for j in range i if dp j and s j i in word_set dp i = True break return dp len s def word_break s wordDict word_set = set wordDict dp = [False] * (len s + 1) dp 0 = True for i in range 1 len s + 1 for j in range i if dp j and s j i in word_set dp i = True break return dp len s"
        ],
        "15_final_mastery": [
            "Слепая печать — это не просто навык, а фундаментальная компетенция современного специалиста, работающего с информацией. Освоив десятипальцевый метод, вы освободите когнитивные ресурсы для решения сложных задач, а не для механического поиска клавиш. Мышечная память, сформированная через регулярные тренировки, позволит вам печатать со скоростью 300-400 знаков в минуту без усталости даже после восьмичасового рабочего дня. Помните: ключ к успеху — не скорость на старте, а дисциплина и правильная техника. Не смотрите на клавиатуру, даже когда ошибаетесь. Исправляйте ошибки на ощупь. Через две-три недели ежедневных занятий по 15 минут вы обнаружите, что набираете текст автоматически, не задумываясь о положении пальцев. Это и есть мастерство слепой печати. Слепая печать — это не просто навык, а фундаментальная компетенция современного специалиста, работающего с информацией. Освоив десятипальцевый метод, вы освободите когнитивные ресурсы для решения сложных задач, а не для механического поиска клавиш.",
            "Touch typing is not merely a skill but a foundational competency for any information worker in the digital age. By mastering the ten-finger method, you free cognitive resources for complex problem-solving rather than mechanical key hunting. Muscle memory, developed through consistent daily practice, enables typing speeds of 60-80 words per minute without fatigue even after an eight-hour workday. Remember: the key to success is not initial speed but discipline and proper technique. Never look at the keyboard, even when making mistakes. Correct errors by feel. Within two to three weeks of daily 15-minute sessions, you will discover that text flows automatically under your fingers without conscious thought about key positions. This is the essence of touch typing mastery. Touch typing is not merely a skill but a foundational competency for any information worker in the digital age. By mastering the ten-finger method, you free cognitive resources for complex problem-solving rather than mechanical key hunting."
        ]
    }
}

def get_next_level(track: str, level_key: str):
    """Возвращает следующий уровень в треке или None, если конец."""
    levels = list(LESSONS[track].keys())
    try:
        idx = levels.index(level_key)
        return levels[idx + 1] if idx + 1 < len(levels) else None
    except ValueError:
        return None

def get_lesson(track: str, level_key: str, language: str = "ru") -> list:
    """
    Возвращает список упражнений для заданного трека и уровня.
    :param track: "beginner" или "advanced"
    :param level_key: например, "1_base_position"
    :param language: "ru" или "en" (в текущей версии все упражнения на русском/код)
    :return: список строк
    """
    # Все упражнения уже подготовлены на русском + код/англ где уместно
    # Для английской раскладки потребуется отдельная библиотека (не входит в задачу "слепой" для русской)
    return LESSONS.get(track, {}).get(level_key, [])