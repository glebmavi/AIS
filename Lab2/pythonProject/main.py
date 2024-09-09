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
    'assassin': ['убийца', 'ассасин', 'assassin'],
    'burst': ['бурст', 'burst'],
    'catcher': ['ловец', 'catcher', 'cc', 'кэтчер'],
    'diver': ['погружение', 'diver', 'дайвер'],
    'enchanter': ['саппорт', 'support', 'enchanter'],
    'juggernaut': ['танк', 'juggernaut', 'джаггернаут'],
    'marksman': ['стрелок', 'адк', 'marksman', 'марксман'],
    'skirmisher': ['дуэлянт', 'skirmisher', 'скримишер'],
    'specialist': ['специалист', 'specialist'],
    'vanguard': ['вангард', 'vanguard'],
}

POSITIONS = {
    'top': ['топ', 'верх'],
    'mid': ['средняя', 'мид'],
    'jungle': ['джангл', 'лес'],
    'bot': ['бот', 'нижняя', 'ботлейн'],
    'support': ['саппорт', 'поддержка']
}

ATTRIBUTES = {
    'damage': ['урон', 'damage'],
    'mobility': ['мобильность', 'mobility'],
    'utility': ['утилита', 'utility'],
    'tankiness': ['выживаемость', 'tankiness'],
    'control': ['контроль', 'control'],
    'support': ['поддержка', 'support', 'саппорт'],
    'late_game': ['поздняя', 'late', 'late game'],
    'initiation': ['инициация', 'initiation'],
    'team_fight': ['командные', 'team fight'],
    'one_shot': ['ваншот', 'one shot'],

}


def extract_preferences(user_input):
    """ Извлечение предпочтений из текста пользователя. """
    user_input = user_input.lower()

    preferences = {
        'role': None,
        'position': None,
        'attribute': None
    }

    # Ищем ключевые слова для ролей, позиций и атрибутов
    for role, keywords in ROLES.items():
        if any(keyword in user_input for keyword in keywords):
            preferences['role'] = role
    for position, keywords in POSITIONS.items():
        if any(keyword in user_input for keyword in keywords):
            preferences['position'] = position
    for attribute, keywords in ATTRIBUTES.items():
        if any(keyword in user_input for keyword in keywords):
            preferences['attribute'] = attribute

    return preferences


def query_champions(preferences):  # TODO: edit attributes according to rules
    """ Генерация запроса к базе знаний на основе предпочтений. """
    query_str = ""

    if preferences['role']:
        query_str += f"role(Champion, {preferences['role']}), "

    if preferences['position']:
        query_str += f"position(Champion, {preferences['position']}), "

    if preferences['attribute']:
        if preferences['attribute'] == 'support':
            query_str += "good_support(Champion), "
        elif preferences['attribute'] == 'late_game':
            query_str += "strong_late_game(Champion), "
        elif preferences['attribute'] == 'initiation':
            query_str += "can_initiate(Champion), "
        elif preferences['attribute'] == 'team_fight':
            query_str += "effective_in_teamfights(Champion), "
        elif preferences['attribute'] == 'one_shot':
            query_str += "can_one_shot(Champion), "

    # Удаляем последнюю запятую и пробел
    query_str = query_str.rstrip(', ')

    champions = list(prolog.query(query_str))
    return champions


def calculate_confidence(preferences, champion):
    """ Подсчет уверенности (confidence) на основе совпадений предпочтений. """
    confidence = 0
    total_criteria = len([v for v in preferences.values() if v is not None])

    if 'role' in preferences and preferences['role']:
        if list(prolog.query(f"role({champion}, {preferences['role']})")):
            confidence += 1

    if 'position' in preferences and preferences['position']:
        if list(prolog.query(f"position({champion}, {preferences['position']})")):
            confidence += 1

    if 'attribute' in preferences and preferences['attribute']:
        if preferences['attribute'] == 'damage':
            if list(prolog.query(f"good_for_damage({champion})")):
                confidence += 1
        if preferences['attribute'] == 'support':
            if list(prolog.query(f"good_for_support({champion})")):
                confidence += 1

    if total_criteria == 0:
        return 0
    return confidence / total_criteria * 100  # процентное совпадение


def main():
    user_input = input("Опишите свои предпочтения по роли, позиции и атрибутам чемпиона: ")

    # Извлекаем предпочтения
    preferences = extract_preferences(user_input)

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
