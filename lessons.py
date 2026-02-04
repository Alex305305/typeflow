# lessons.py
# Уроки для тренажёра слепой печати — совместимо с GUI (строки с пробелами)
# Поддержка: ru / en
# Структура: beginner (10 уровней) + advanced (5 уровней)

LESSONS = {
    "beginner": {
        # Уровень 1: базовые клавиши F и J
        "1_fingers": [
            "f f f f f f",
            "j j j j j j",
            "f j f j f j",
            "j f j f j f",
            "f f j j f f",
            "j j f f j j",
            "f j j f f j",
            "j f f j j f"
        ],

        # Уровень 2: домашний ряд (ASDF / JKL;)
        "2_home_row": [
            "a s d f ; l k j",
            "f d s a j k l ;",
            "a s d f f j k l",
            "; l k j a s d f",
            "a ; s l d k f j",
            "f j d k s a ; l",
            "asdf ;lkj asdf",
            "fdsa jkl; fdsa"
        ],

        # Уровень 3: верхний левый ряд (QWERT)
        "3_top_left": [
            "q w e r t y u i o p",
            "q t w r e y u i o p",
            "qw er ty ui op qw",
            "er qw ty ui op er",
            "q w e r t q w e r t",
            "t r e w q t r e w q",
            "qwerty uiop asdf",
            "qwe rty uio p asd"
        ],

        # Уровень 4: правый верхний ряд (YUIOP)
        "4_top_right": [
            "y u i o p",
            "p o i u y",
            "y u i o p y u i o p",
            "u i o p y u i o p y",
            "yui op yui op",
            "poy ui yop iu",
            "y u i o p ; l k j",
            "p o i u y f d s a"
        ],

        # Уровень 5: нижний ряд (ZXCVBNM)
        "5_bottom_row": [
            "z x c v b n m",
            "m n b v c x z",
            "z x c v b n m z x",
            "b v c x z m n",
            "zx cv bn mz",
            "cv zx nb mv",
            "zxc vbn m , . /",
            "z x c v b n m , . /"
        ],

        # Уровень 6: цифры и символы
        "6_symbols": [
            "1 2 3 4 5 6 7 8 9 0",
            "! @ # $ % ^ & * ( )",
            "1 ! 2 @ 3 # 4 $ 5 %",
            "q w e r t 1 2 3 4 5",
            "` ~ - _ = + [ ] { }",
            "| \\ : ; \" ' < > , . ? /",
            "123 456 7890 !@#$",
            "qwerty 12345 asdfg"
        ],

        # Уровень 7–10: комбинации
        "7_combos_1": [
            "f j a s d k l ;",
            "q w e r t y u i",
            "z x c v b n m , .",
            "1 2 3 4 5 6 7 8 9",
            "the and for are but",
            "linux ubuntu debian",
            "vim nano emacs git",
            "ssh scp rsync grep"
        ],
        "8_combos_2": [
            "ls -la /home",
            "cd .. && pwd",
            "cat /etc/os-release",
            "sudo apt update",
            "git init && git add .",
            "docker run -d nginx",
            "kubectl get pods",
            "helm install nginx"
        ],
        "9_combos_3": [
            "The quick brown fox",
            "Pack my box with five",
            "How vexingly quick daft zebras jump!",
            "Sphinx of black quartz, judge my vow.",
            "Cwm fjord bank glyphs vext quiz.",
            "Cozy lummox gives smart squid who asks for job",
            "Grumpy wizards make toxic brew for the evil queen",
            "Blame the blue sky for the bright light"
        ],
        "10_full_speed": [
            "f j a s d f j k l ; q w e r t y u i o p z x c v b n m",
            "1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( ) - _ = +",
            "ls -l | grep \".py\" && python main.py",
            "git commit -am \"fix: typo in config\"",
            "docker-compose up --build",
            "kubectl apply -f deployment.yaml",
            "ansible-playbook site.yml -i inventory",
            "curl -X GET https://api.example.com/v1/data"
        ]
    },
    "advanced": {
        "1_bash_basic": [
            "echo $PATH",
            "export PS1='\\u@\\h:\\w$ '",
            "history | grep ssh",
            "find /var/log -name *.log -mtime -7",
            "tar -czf backup.tar.gz /home/user",
            "rsync -avz /src/ user@host:/dst/",
            "chmod 755 script.sh",
            "chown user:group file"
        ],
        "2_git_dev": [
            "git status -s",
            "git diff --cached",
            "git reset HEAD~1",
            "git rebase -i HEAD~3",
            "git cherry-pick abc1234",
            "git bisect start && git bisect bad && git bisect good 123",
            "git submodule update --init",
            "git worktree add ../feature-branch feature"
        ],
        "3_docker_k8s": [
            "docker build -t app:latest .",
            "docker run --rm -it -v $(pwd):/src python:3.12 bash",
            "kubectl get nodes -o wide",
            "kubectl describe pod my-pod",
            "helm repo add bitnami https://charts.bitnami.com/bitnami",
            "kind create cluster --name dev",
            "istioctl install --set profile=demo",
            "flux create source git my-repo --url=https://github.com/user/repo"
        ],
        "4_yaml_json": [
            "apiVersion: v1\nkind: Pod\nmetadata:\n  name: nginx",
            "spec:\n  containers:\n  - name: nginx\n    image: nginx:1.25",
            '{"name":"nginx","replicas":3,"port":80}',
            '{"env":"prod","config":{"debug":false}}',
            "server {\n  listen 80;\n  location / { proxy_pass http://app; } }",
            "upstream backend { server 127.0.0.1:8080; }",
            "- name: install-deps\n  apt:\n    pkg: python3-pip",
            "labels:\n  app.kubernetes.io/name: nginx"
        ],
        "5_prose_en_ru": [
            "The five boxing wizards jump quickly.",
            "Pack my box with five dozen liquor jugs.",
            "Съешь ещё этих мягких французских булок, да выпей чаю.",
            "Размножение бактерий происходит путём деления клетки.",
            "DevOps — это культура и практика автоматизации ИТ-процессов.",
            "Kubernetes управляет контейнеризированными приложениями в кластерах.",
            "Git — распределённая система контроля версий.",
            "Linux — свободная операционная система с открытым исходным кодом."
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
    :param level_key: например, "2_home_row"
    :param language: "ru" или "en"
    :return: список строк (на выбранном языке)
    """
    exercises_en = LESSONS.get(track, {}).get(level_key, [])

    if language == "ru":
        trans_map = {
            # === Level 1 ===
            "f f f f f f": "а а а а а а",
            "j j j j j j": "о о о о о о",
            "f j f j f j": "а о а о а о",
            "j f j f j f": "о а о а о а",
            "f f j j f f": "а а о о а а",
            "j j f f j j": "о о а а о о",
            "f j j f f j": "а о о а а о",
            "j f f j j f": "о а а о о а",

            # === Level 2 ===
            "a s d f ; l k j": "ф ы в а ж э л д",
            "f d s a j k l ;": "а в ы ф о к л ж",
            "a s d f f j k l": "ф ы в а а о к л",
            "; l k j a s d f": "ж л к о ф ы в а",
            "a ; s l d k f j": "ф ж ы л в к а о",
            "f j d k s a ; l": "а о в к ы ф ж л",
            "asdf ;lkj asdf": "фывап жлко фывап",
            "fdsa jkl; fdsa": "авыф оклж авыф",

            # === Level 3 ===
            "q w e r t y u i o p": "й ц у к е н г ш щ з",
            "q t w r e y u i o p": "й е ц к у н г ш щ з",
            "qw er ty ui op qw": "йц ук ен гш щз йц",
            "er qw ty ui op er": "ук йц ен гш щз ук",
            "q w e r t q w e r t": "й ц у к е й ц у к е",
            "t r e w q t r e w q": "е к у ц й е к у ц й",
            "qwerty uiop asdf": "йцукен гшщз фыва",
            "qwe rty uio p asd": "йцу кен гшщ з фыв",

            # === Level 4 ===
            "y u i o p": "н г ш щ з",
            "p o i u y": "з щ ш г н",
            "y u i o p y u i o p": "н г ш щ з н г ш щ з",
            "u i o p y u i o p y": "г ш щ з н г ш щ з н",
            "yui op yui op": "нгш щз нгш щз",
            "poy ui yop iu": "зон гш ноз шг",
            "y u i o p ; l k j": "н г ш щ з ж э л д",
            "p o i u y f d s a": "з щ ш г н а в ы ф",

            # === Level 5 ===
            "z x c v b n m": "я ч с м и т ь",
            "m n b v c x z": "ь т и м с ч я",
            "z x c v b n m z x": "я ч с м и т ь я ч",
            "b v c x z m n": "и м с ч я ь т",
            "zx cv bn mz": "яч см ит мь",
            "cv zx nb mv": "см яч ти мв",
            "zxc vbn m , . /": "ячс мит ь , . ю",
            "z x c v b n m , . /": "я ч с м и т ь , . ю",

            # === Level 6 ===
            "1 2 3 4 5 6 7 8 9 0": "1 2 3 4 5 6 7 8 9 0",
            "! @ # $ % ^ & * ( )": "! @ # $ % ^ & * ( )",
            "1 ! 2 @ 3 # 4 $ 5 %": "1 ! 2 @ 3 # 4 $ 5 %",
            "q w e r t 1 2 3 4 5": "й ц у к е 1 2 3 4 5",
            "` ~ - _ = + [ ] { }": "` ~ - _ = + [ ] { }",
            "| \\ : ; \" ' < > , . ? /": "| \\ : ; \" ' < > , . ? /",
            "123 456 7890 !@#$": "123 456 7890 !@#$",
            "qwerty 12345 asdfg": "йцукен 12345 фывапр",

            # === Level 7 ===
            "f j a s d k l ;": "а о ф ы в к л ж",
            "q w e r t y u i": "й ц у к е н г ш",
            "z x c v b n m , .": "я ч с м и т ь , .",
            "1 2 3 4 5 6 7 8 9": "1 2 3 4 5 6 7 8 9",
            "the and for are but": "что и для но но",
            "linux ubuntu debian": "линукс убунту дебиан",
            "vim nano emacs git": "вим нано эмакс гит",
            "ssh scp rsync grep": "ссш скп рсинк греп",

            # === Level 8 ===
            "ls -la /home": "лс -ла /хоум",
            "cd .. && pwd": "цд .. && пвд",
            "cat /etc/os-release": "кат /етц/ос-релиз",
            "sudo apt update": "судо апт апдейт",
            "git init && git add .": "гит инит && гит адд .",
            "docker run -d nginx": "докер ран -д нгинкс",
            "kubectl get pods": "кабectl гет подс",
            "helm install nginx": "хелм инсталл нгинкс",

            # === Level 9–10 ===
            "The quick brown fox": "Быстрый коричневый лис",
            "Pack my box with five": "Упакуй мой ящик пятью",
            "How vexingly quick daft zebras jump!": "Как раздражающе быстро глупые зебры прыгают!",
            "Sphinx of black quartz, judge my vow.": "Сфинкс из чёрного кварца, оцени мою клятву.",
            "Cwm fjord bank glyphs vext quiz.": "Кум фьорд банк глифс векст квиз.",
            "Cozy lummox gives smart squid who asks for job": "Уютный неуклюжий тип даёт умному спруту, который просит работу",
            "Grumpy wizards make toxic brew for the evil queen": "Ворчливые волшебники варят ядовитое зелье для злой королевы",
            "Blame the blue sky for the bright light": "Вини голубое небо за яркий свет",

            "f j a s d f j k l ; q w e r t y u i o p z x c v b n m": "а о ф ы в а о к л ж й ц у к е н г ш щ з я ч с м и т ь",
            "1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( ) - _ = +": "1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( ) - _ = +",
            "ls -l | grep \".py\" && python main.py": "лс -л | греп \".пу\" && питон майн.пу",
            "git commit -am \"fix: typo in config\"": "гит коммит -ам \"фикс: опечатка в конфиге\"",
            "docker-compose up --build": "докер-композ ап --билд",
            "kubectl apply -f deployment.yaml": "кабectl апплай -ф деплоймент.ямл",
            "ansible-playbook site.yml -i inventory": "ансIBLE-плейбук сайт.ямл -и инвентори",
            "curl -X GET https://api.example.com/v1/data": "карл -Х ГЕТ хттпс://апи.екзампле.ком/в1/дата"
        }

        translated = []
        for ex in exercises_en:
            if ex in trans_map:
                translated.append(trans_map[ex])
            else:
                # Не переводим команды, JSON, YAML, спецсимволы
                translated.append(ex)
        return translated

    else:
        return exercises_en