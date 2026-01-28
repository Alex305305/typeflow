# lessons.py
# Уроки для тренажёра слепой печати — вдохновлено RapidTyping
# Поддержка: ru / en
# Структура: beginner (10 уровней) + advanced (5 уровней)

LESSONS = {
    "beginner": {
        # Уровень 1: Позиция пальцев (F и J — базовые)
        "1_fingers": [
            "f f f f f f ",
            "j j j j j j ",
            "f j f j ",
            "j f j f ",
            "f f j j ",
            "j j f f ",
            "f j j f ",
            "j f f j "
        ],
        # Уровень 2: Домашний ряд (ASDF / JKL;)
        "2_home_row": [
            "a s d f ; ",
            "f d s a ",
            "a s d f f ",
            "; l k j j k ",
            "a ; s l d k ",
            "f j d k s",
            "asdf ;lkj asdf ;lkj",
            "fdsa jkl; fdsa jkl;"
        ],
        # Уровень 3: Верхний левый ряд (QWERT)
        "3_top_left": [
            "q w e r t",
            "t r e w q",
            "q t w r e",
            "e r w t q",
            "qw qw qw qw",
            "er er er er",
            "ty ty ty ty",
            "qwerty qwerty"
        ],
        # Уровень 4: Верхний правый ряд (YUIOP)
        "4_top_right": [
            "y u i o p",
            "p o i u y",
            "y p u o i",
            "i o u p y",
            "ui ui ui ui",
            "op op op op",
            "yu yu yu yu",
            "uiop uiop uiop"
        ],
        # Уровень 5: Нижний левый ряд (ZXCVB)
        "5_bottom_left": [
            "z x c v b",
            "b v c x z",
            "z b x v c",
            "c v x b z",
            "zx zx zx zx",
            "cv cv cv cv",
            "vb vb vb vb",
            "zxcvb zxcvb"
        ],
        # Уровень 6: Нижний правый ряд (NM,./)
        "6_bottom_right": [
            "n m , . /",
            "/ . , m n",
            "n / m . ,",
            ", . m / n",
            "nm nm nm nm",
            ",. ,. ,. ,.",
            "./ ./ ./ ./",
            "nm,. / nm,. /"
        ],
        # Уровень 7: Частые биграммы (en/ru)
        "7_bigrams": [
            "th he in er an re nd at on es",
            "то но на ре ен ни то он ес"
        ],
        # Уровень 8: Короткие слова
        "8_words": [
            "cat dog and the run play type fast",
            "кот соб и что бег игр печ быс"
        ],
        # Уровень 9: Короткие фразы
        "9_short_sentences": [
            "The cat runs fast.",
            "Play and type well.",
            "Кот бежит быстро.",
            "Играй и печатай хорошо."
        ],
        # Уровень 10: Полные предложения
        "10_sentences": [
            "The quick brown fox jumps over the lazy dog.",
            "Practice makes perfect every single day.",
            "В чащах юга жил был цитрус? Да, но фальшивый экземпляр!",
            "Практика делает мастера каждый день."
        ]
    },
    "advanced": {
        # Уровень 1: Комбинированные дриллы
        "1_drills": [
            "asdf jkl; qwer uiop zxcv bnm,",
            "фывапр олдж йцук енгш ячсм ить,",
            "qaz wsx edc rfv tgb yhn ujm ik, ol. p;/",
            "йфя чсу вам икр тго шлб щдю зжэ хъь"
        ],
        # Уровень 2: Сложные слова
        "2_speed": [
            "because through should could would",
            "government beautiful experience",
            "потому через должен мог бы хотел",
            "правительство красивый опыт"
        ],
        # Уровень 3: Технические термины
        "3_technical": [
            "python javascript keyboard accuracy",
            "blind typing programming development",
            "питон яваскрипт клавиатура точность",
            "слепая печать программирование разработка"
        ],
        # Уровень 4: Цитаты
        "4_quotes": [
            "To be or not to be, that is the question.",
            "All animals are equal, but some animals are more equal than others.",
            "Быть или не быть — вот в чём вопрос.",
            "Все животные равны, но некоторые равнее других."
        ],
        # Уровень 5: Свободный набор (текст)
        "5_free_typing": [
            "The only way to do great work is to love what you do. — Steve Jobs",
            "Слепая печать — навык, который экономит тысячи часов в жизни. — Alex305305"
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
        # Словарь перевода: англ → рус (сохранение структуры пробелов!)
        trans_map = {
            # Beginner
            "f f f f f f f f": "а а а а а а а а",
            "j j j j j j j j": "о о о о о о о о",
            "f j f j f j f j": "а о а о а о а о",
            "j f j f j f j f": "о а о а о а о а",
            "f f j j f f j j": "а а о о а а о о",
            "j j f f j j f f": "о о а а о о а а",
            "f j j f f j j f": "а о о а а о о а",
            "j f f j j f f j": "о а а о о а а о",

            "a s d f ; l k j": "ф ы в а ж э л д",
            "f d s a j k l ;": "а в ы ф о к л ж",
            "a s d f f d s a": "ф ы в а а в ы ф",
            "; l k j j k l ;": "ж л к о о к л ж",
            "a ; s l d k f j": "ф ж ы л в к а о",
            "f j d k s l a ;": "а о в к ы л ф ж",
            "asdf ;lkj asdf ;lkj": "фывап жлко фывап жлко",
            "fdsa jkl; fdsa jkl;": "авыф оклж авыф оклж",

            "q w e r t": "й ц у к е",
            "t r e w q": "е к у ц й",
            "q t w r e": "й е ц к у",
            "e r w t q": "у к ц е й",
            "qw qw qw qw": "йц йц йц йц",
            "er er er er": "ук ук ук ук",
            "ty ty ty ty": "ен ен ен ен",
            "qwerty qwerty": "йцукен йцукен",

            "y u i o p": "н г ш щ з",
            "p o i u y": "з щ ш г н",
            "y p u o i": "н з г щ ш",
            "i o u p y": "ш щ г з н",
            "ui ui ui ui": "шг шг шг шг",
            "op op op op": "щз щз щз щз",
            "yu yu yu yu": "нг нг нг нг",
            "uiop uiop uiop": "гшщз гшщз гшщз",

            "z x c v b": "я ч с м и",
            "b v c x z": "и м с ч я",
            "z b x v c": "я и ч м с",
            "c v x b z": "с м ч и я",
            "zx zx zx zx": "яч яч яч яч",
            "cv cv cv cv": "см см см см",
            "vb vb vb vb": "ми ми ми ми",
            "zxcvb zxcvb": "ячсми ячсми",

            "n m , . /": "т ь , . ю",
            "/ . , m n": "ю . , ь т",
            "n / m . ,": "т ю ь . ,",
            ", . m / n": ", . ь ю т",
            "nm nm nm nm": "ть ть ть ть",
            ",. ,. ,. ,.": ",. ,. ,. ,.",
            "./ ./ ./ ./": ".ю .ю .ю .ю",
            "nm,. / nm,. /": "ть,. ю ть,. ю",

            # Bigrams
            "th he in er an re nd at on es": "то но на ре ен ни то он ес",
            # Words
            "cat dog and the run play type fast": "кот соб и что бег игр печ быс",
            # Sentences
            "The cat runs fast.": "Кот бежит быстро.",
            "Play and type well.": "Играй и печатай хорошо.",
            "The quick brown fox jumps over the lazy dog.": "В чащах юга жил был цитрус? Да, но фальшивый экземпляр!",
            "Practice makes perfect every single day.": "Практика делает мастера каждый день.",

            # Advanced
            "asdf jkl; qwer uiop zxcv bnm,": "фывапр олдж йцук енгш ячсм ить,",
            "qaz wsx edc rfv tgb yhn ujm ik, ol. p;/": "йфя чсу вам икр тго шлб щдю зжэ хъь",
            "because through should could would": "потому через должен мог бы хотел",
            "government beautiful experience": "правительство красивый опыт",
            "python javascript keyboard accuracy": "питон яваскрипт клавиатура точность",
            "blind typing programming development": "слепая печать программирование разработка",
            "To be or not to be, that is the question.": "Быть или не быть — вот в чём вопрос.",
            "All animals are equal, but some animals are more equal than others.": "Все животные равны, но некоторые равнее других.",
            "The only way to do great work is to love what you do. — Steve Jobs": "Слепая печать — навык, который экономит тысячи часов в жизни. — Alex305305"
        }

        # Применяем перевод
        translated = []
        for ex in exercises_en:
            # Ищем точное совпадение
            if ex in trans_map:
                translated.append(trans_map[ex])
            else:
                # Если нет — оставляем как есть (например, цифры, спецсимволы)
                translated.append(ex)
        return translated

    else:
        return exercises_en