from os import putenv

putenv("SWI_HOME_DIR", "C:\\Program Files\\swipl")

from pyswip import Prolog

prolog = Prolog()
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
    """
    Извлечение предпочтений из текста пользователя.
    Функция проверяет на наличие ключевых слов для ролей, позиций и атрибутов.
    Если найдено совпадение, оно добавляется в соответствующий список (roles, positions, attributes).
    Возвращает словарь с предпочтениями в виде списков.
    """
    user_input = user_input.lower()

    preferences = {
        'roles': [],
        'positions': [],
        'attributes': []
    }

    def match_keyword(phrase, keywords):
        for keyword in keywords:
            if keyword in phrase:
                return True
        return False

    for role, keywords in ROLES.items():
        if match_keyword(user_input, keywords):
            preferences['roles'].append(role)

    for position, keywords in POSITIONS.items():
        if match_keyword(user_input, keywords):
            preferences['positions'].append(position)

    for attribute, keywords in ATTRIBUTES.items():
        if match_keyword(user_input, keywords):
            preferences['attributes'].append(attribute)

    return preferences


def query_champions(preferences):
    """
    Генерация нескольких запросов к базе знаний на основе предпочтений.
    Функция выполняет отдельные запросы для ролей, позиций и атрибутов.
    Объединяет результаты запросов, возвращая чемпионов, соответствующих хотя бы одному предпочтению.
    """
    champions_set = set()

    if preferences['roles']:
        for role in preferences['roles']:
            role_query = f"role(Champion, {role})"
            role_champions = list(prolog.query(role_query))
            champions_set.update([champ['Champion'] for champ in role_champions])

    if preferences['positions']:
        for position in preferences['positions']:
            position_query = f"position(Champion, {position})"
            position_champions = list(prolog.query(position_query))
            champions_set.update([champ['Champion'] for champ in position_champions])

    if preferences['attributes']:
        for attribute in preferences['attributes']:
            prolog_rule = ATTRIBUTE_RULES.get(attribute)
            if prolog_rule:
                attribute_query = f"{prolog_rule}(Champion)"
                attribute_champions = list(prolog.query(attribute_query))
                champions_set.update([champ['Champion'] for champ in attribute_champions])

    champions = [{'Champion': champ} for champ in champions_set]

    return champions


def calculate_confidence(preferences, champion):
    """
    Подсчет уверенности (confidence) на основе совпадений предпочтений.
    Функция проверяет, насколько чемпион соответствует каждому из предпочтений пользователя.
    Для каждой совпавшей роли, позиции или атрибута увеличивается счет уверенности.
    Возвращает процент уверенности в виде числа от 0 до 100.
    """
    confidence = 0
    total_criteria = len(preferences['roles']) + len(preferences['positions']) + len(preferences['attributes'])

    # Проверяем совпадение по критерию и увеличиваем уверенность за каждое совпадение
    if preferences['roles']:
        for role in preferences['roles']:
            if list(prolog.query(f"role({champion}, {role})")):
                confidence += 1

    if preferences['positions']:
        for position in preferences['positions']:
            if list(prolog.query(f"position({champion}, {position})")):
                confidence += 1

    if preferences['attributes']:
        for attribute in preferences['attributes']:
            prolog_rule = ATTRIBUTE_RULES.get(attribute)
            if prolog_rule and list(prolog.query(f"{prolog_rule}({champion})")):
                confidence += 1

    if total_criteria == 0:
        return 0
    return confidence / total_criteria * 100


def main():
    user_input = input("Опишите свои предпочтения по роли, позиции и атрибутам чемпиона: ")

    preferences = extract_preferences(user_input)

    print("\nИзвлеченные предпочтения:")
    print(f"Роли: {preferences['roles']}")
    print(f"Позиции: {preferences['positions']}")
    print(f"Атрибуты: {preferences['attributes']}")

    if not any(preferences.values()):
        print("Не удалось распознать ваши предпочтения, попробуйте снова.")
        return

    champions = query_champions(preferences)

    if champions:
        print("\nРекомендованные чемпионы:")
        for champ in champions:
            confidence = calculate_confidence(preferences, champ['Champion'])
            if confidence > 50:
                print(f"Чемпион: {champ['Champion']}, Соответствие: {confidence:.2f}%")
    else:
        print("К сожалению, не найдено чемпионов, соответствующих вашим предпочтениям.")


if __name__ == "__main__":
    main()
