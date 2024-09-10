import re
from os import putenv

putenv("SWI_HOME_DIR", "C:\\Program Files\\swipl")

from pyswip import Prolog

# Инициализация Prolog
prolog = Prolog()

# Загрузка базы знаний Prolog
prolog.consult("part1.pl")

# Возможные ключевые слова для ролей, позиций и атрибутов
ROLES = {
    'assassin': ['убийца', 'убийц', 'ассасин', 'assassin'],
    'burst': ['бурст', 'burst'],
    'catcher': ['ловец', 'ловц', 'catcher', 'cc', 'кэтчер'],
    'diver': ['погружение', 'погруж', 'diver', 'дайвер'],
    'enchanter': ['enchanter', 'чародейка', 'чарод'],
    'juggernaut': ['танк', 'juggernaut', 'джаггернаут'],
    'marksman': ['стрелок', 'стрел', 'адк', 'marksman', 'марксман'],
    'skirmisher': ['дуэлянт', 'дуэл', 'skirmisher', 'скримишер'],
    'specialist': ['специалист', 'специал', 'specialist'],
    'vanguard': ['вангард', 'vanguard'],
}

POSITIONS = {
    'top': ['топ', 'верх'],
    'mid': ['средняя', 'средн', 'мид'],
    'jungle': ['джангл', 'лес'],
    'bot': ['бот', 'нижняя', 'нижн', 'ботлейн'],
    'support': ['саппорт', 'сапп', 'поддержка', 'поддержк']
}

ATTRIBUTES = {
    'damage': ['урон', 'damage'],
    'mobility': ['мобильность', 'мобильн', 'mobility'],
    'utility': ['утилита', 'утил', 'utility'],
    'tankiness': ['выживаемость', 'выжив', 'tankiness'],
    'control': ['контроль', 'контрол', 'control'],
    'support': ['поддержка', 'поддержк', 'support', 'саппорт', 'сапп'],
    'late_game': ['поздняя', 'поздн', 'late', 'late game'],
    'initiation': ['инициация', 'иници', 'initiation', 'инициа'],
    'team_fight': ['командные', 'команд', 'team fight'],
    'one_shot': ['ваншот', 'one shot'],
}

ATTRIBUTE_RULES = {
    'damage': 'can_one_shot',
    'mobility': 'can_avoid_cc',
    'support': 'good_support',
    'late_game': 'strong_late_game',
    'initiation': 'can_initiate',
    'team_fight': 'effective_in_teamfights'
}


def extract_preferences(user_input):
    """ Извлечение предпочтений из текста пользователя. """
    user_input = user_input.lower()

    preferences = {
        'role': None,
        'position': None,
        'attribute': None
    }

    def match_keyword(phrase, keywords):
        for keyword in keywords:
            if keyword in phrase:
                return True
        return False

    # Ищем ключевые слова для ролей, позиций и атрибутов
    for role, keywords in ROLES.items():
        if match_keyword(user_input, keywords):
            preferences['role'] = role
    for position, keywords in POSITIONS.items():
        if match_keyword(user_input, keywords):
            preferences['position'] = position
    for attribute, keywords in ATTRIBUTES.items():
        if match_keyword(user_input, keywords):
            preferences['attribute'] = attribute

    return preferences


def query_champions(preferences):
    """ Генерация запроса к базе знаний на основе предпочтений. """
    query_str = ""

    if preferences['role']:
        query_str += f"role(Champion, {preferences['role']}), "

    if preferences['position']:
        query_str += f"position(Champion, {preferences['position']}), "

    if preferences['attribute']:
        prolog_rule = ATTRIBUTE_RULES.get(preferences['attribute'])
        if prolog_rule:
            query_str += f"{prolog_rule}(Champion), "

    # Удаляем последнюю запятую и пробел
    query_str = query_str.rstrip(', ')

    champions = list(prolog.query(query_str))
    return champions


def calculate_confidence(preferences, champion):
    """ Подсчет уверенности (confidence) на основе совпадений предпочтений. """
    confidence = 0
    total_criteria = len([v for v in preferences.values() if v is not None])

    if preferences['role']:
        if list(prolog.query(f"role({champion}, {preferences['role']})")):
            confidence += 1

    if preferences['position']:
        if list(prolog.query(f"position({champion}, {preferences['position']})")):
            confidence += 1

    if preferences['attribute']:
        prolog_rule = ATTRIBUTE_RULES.get(preferences['attribute'])
        if prolog_rule and list(prolog.query(f"{prolog_rule}({champion})")):
            confidence += 1

    if total_criteria == 0:
        return 0
    return confidence / total_criteria * 100


def main():
    user_input = input("Опишите свои предпочтения по роли, позиции и атрибутам чемпиона: ")

    # Извлекаем предпочтения
    preferences = extract_preferences(user_input)

    # Вывод промежуточных предпочтений
    print("\nИзвлеченные предпочтения:")
    print(f"Роль: {preferences['role']}")
    print(f"Позиция: {preferences['position']}")
    print(f"Атрибут: {preferences['attribute']}")

    # Проверяем, все ли ключевые предпочтения были найдены
    if not preferences['role'] and not preferences['position'] and not preferences['attribute']:
        print("Не удалось распознать ваши предпочтения, попробуйте снова.")
        return

    # Получение рекомендаций
    champions = query_champions(preferences)

    if champions:
        print("\nРекомендованные чемпионы:")
        for champ in champions:
            confidence = calculate_confidence(preferences, champ['Champion'])
            print(f"Чемпион: {champ['Champion']}, Соответствие: {confidence:.2f}%")
    else:
        print("К сожалению, не найдено чемпионов, соответствующих вашим предпочтениям.")


if __name__ == "__main__":
    main()
