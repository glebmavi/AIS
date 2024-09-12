/*
    Создайте базу знаний. База знаний должна включать в себя не менее
    - 20 фактов с одним аргументом,
    - 10-15 фактов с двумя аргументам, которые дополняют и показывают связь с другими фактами
    - 5-7 правил.
    Факты могут описывать объекты, их свойства и отношения между ними. Факты 2 и более аргументами могут описывать различные атрибуты объектов, а правила - логические законы и выводы, которые можно сделать на основе фактов и предикатов.
*/

/*
    Данная БЗ описывает некоторых чемпионов из игры League of Legends.
    Является базой для рекомендатольной системы по выбору чемпиона в зависимости от игрового стиля игрока.
*/

/*
    === Факты ===
    Каждый чемпион описан одним или двумя аргументами: его имя, роль в игре и его характеристики.
*/

champion(garen).
champion(lee_sin).
champion(lucian).
champion(lulu).
champion(tristana).
champion(zed).
champion(yasuo).
champion(malphite).
champion(caitlyn).
champion(ahri).
champion(irelia).
champion(yorick).
champion(nasus).
champion(darius).
champion(jinx).
champion(soraka).
champion(zyra).
champion(singed).
champion(kassadin).
champion(karma).

% Факты с двумя аргументами (атрибуты чемпионов)
% Каждый чемпион имеет роль и позицию в игре. Также описывается его рейтинг (utility, damage, toughness, control, mobility) от 1 до 3.

% Чемпионы могут иметь несколько ролей.
role(garen, juggernaut).
role(lee_sin, diver).
role(lucian, marksman).
role(lulu, enchanter).
role(tristana, marksman).
role(yasuo, skirmisher).
role(malphite, vanguard).
role(caitlyn, marksman).
role(ahri, burst).
role(irelia, diver).
role(yorick, juggernaut).
role(nasus, juggernaut).
role(darius, juggernaut).
role(jinx, marksman).
role(soraka, enchanter).
role(zyra, catcher).
role(singed, specialist).
role(kassadin, assassin).
role(karma, enchanter).
role(karma, burst).
role(zed, assassin).

% Чемпионы могут занимать сразу несколько позиций.
position(garen, top).
position(lee_sin, jungle).
position(lucian, bot).
position(lucian, mid).
position(lulu, support).
position(tristana, bot).
position(tristana, mid).
position(yasuo, mid).
position(yasuo, top).
position(yasuo, bot).
position(malphite, top).
position(malphite, support).
position(caitlyn, bot).
position(ahri, mid).
position(irelia, top).
position(irelia, mid).
position(yorick, top).
position(nasus, top).
position(darius, top).
position(jinx, bot).
position(soraka, support).
position(zyra, support).
position(zyra, mid).
position(singed, top).
position(kassadin, mid).
position(karma, support).
position(karma, mid).
position(zed, mid).


% У каждого чемпиона есть рейтинг по 5 атрибутам (от 1 до 3)
rating(garen, utility, 1).
rating(garen, damage, 2).
rating(garen, toughness, 3).
rating(garen, control, 1).
rating(garen, mobility, 1).

rating(lee_sin, utility, 1).
rating(lee_sin, damage, 3).
rating(lee_sin, toughness, 2).
rating(lee_sin, control, 2).
rating(lee_sin, mobility, 3).

rating(lucian, utility, 1).
rating(lucian, damage, 3).
rating(lucian, toughness, 1).
rating(lucian, control, 1).
rating(lucian, mobility, 3).

rating(lulu, utility, 3).
rating(lulu, damage, 2).
rating(lulu, toughness, 1).
rating(lulu, control, 2).
rating(lulu, mobility, 1).

rating(tristana, utility, 1).
rating(tristana, damage, 3).
rating(tristana, toughness, 1).
rating(tristana, control, 2).
rating(tristana, mobility, 2).

rating(yasuo, utility, 2).
rating(yasuo, damage, 3).
rating(yasuo, toughness, 1).
rating(yasuo, control, 2).
rating(yasuo, mobility, 3).

rating(malphite, utility, 1).
rating(malphite, damage, 1).
rating(malphite, toughness, 3).
rating(malphite, control, 3).
rating(malphite, mobility, 1).

rating(caitlyn, utility, 1).
rating(caitlyn, damage, 3).
rating(caitlyn, toughness, 1).
rating(caitlyn, control, 2).
rating(caitlyn, mobility, 2).

rating(ahri, utility, 1).
rating(ahri, damage, 3).
rating(ahri, toughness, 1).
rating(ahri, control, 2).
rating(ahri, mobility, 3).

rating(irelia, utility, 2).
rating(irelia, damage, 2).
rating(irelia, toughness, 2).
rating(irelia, control, 2).
rating(irelia, mobility, 3).

rating(yorick, utility, 2).
rating(yorick, damage, 2).
rating(yorick, toughness, 2).
rating(yorick, control, 2).
rating(yorick, mobility, 1).

rating(nasus, utility, 1).
rating(nasus, damage, 2).
rating(nasus, toughness, 3).
rating(nasus, control, 2).
rating(nasus, mobility, 1).

rating(darius, utility, 1).
rating(darius, damage, 3).
rating(darius, toughness, 2).
rating(darius, control, 2).
rating(darius, mobility, 1).

rating(jinx, utility, 1).
rating(jinx, damage, 3).
rating(jinx, toughness, 1).
rating(jinx, control, 2).
rating(jinx, mobility, 1).

rating(soraka, utility, 3).
rating(soraka, damage, 1).
rating(soraka, toughness, 1).
rating(soraka, control, 2).
rating(soraka, mobility, 1).

rating(zyra, utility, 1).
rating(zyra, damage, 3).
rating(zyra, toughness, 1).
rating(zyra, control, 3).
rating(zyra, mobility, 1).

rating(singed, utility, 1).
rating(singed, damage, 2).
rating(singed, toughness, 3).
rating(singed, control, 2).
rating(singed, mobility, 2).

rating(kassadin, utility, 1).
rating(kassadin, damage, 3).
rating(kassadin, toughness, 2).
rating(kassadin, control, 1).
rating(kassadin, mobility, 3).

rating(karma, utility, 2).
rating(karma, damage, 2).
rating(karma, toughness, 1).
rating(karma, control, 2).
rating(karma, mobility, 1).

rating(zed, utility, 1).
rating(zed, damage, 3).
rating(zed, toughness, 1).
rating(zed, control, 1).
rating(zed, mobility, 3).

/*
    === Правила ===
    Правила определяют некоторые логические зависимости между атрибутами чемпионов.
*/

% Чемпион с высокой мобильностью может эффективно избегать навыков контроля
can_avoid_cc(Champion) :-
    (rating(Champion, mobility, 3)).

% Чемпионы, которые накапливают силу в течение игры, становятся сильными на поздних стадиях
strong_late_game(Champion) :-
    (role(Champion, burst); role(Champion, battlemage); rating(Champion, control, Rating), Rating > 2).

% Если чемпион является танком, то он способен принимать на себя значительный урон и инициировать бои
can_initiate(Champion) :-
    (role(Champion, juggernaut); role(Champion, diver); role(Champion, vanguard)).

% Чемпионы которые эффективны в командных сражениях
effective_in_teamfights(Champion) :-
    (role(Champion, burst); role(Champion, juggernaut); role(Champion, catcher); role(Champion, enchanter)).

% Чемпионы с высоким контролем способны ограничивать движение противников
can_control(Champion) :-
    (role(Champion, catcher); role(Champion, enchanter); rating(Champion, control, Rating), Rating > 2).

% Чемпионы с высоким уроном способны быстро уничтожать противников
can_one_shot(Champion) :-
    champion(Champion),
    \+ (role(Champion, vanguard); role(Champion, warden)).

% Чемпионы с высоким уровнем контроля и полезности являются хорошими саппортами
good_support(Champion) :-
    rating(Champion, control, ControlRating),
    rating(Champion, utility, UtilityRating),
    ControlRating >= 2,
    UtilityRating > 2.

/*
    === Запросы ===
*/

% Простые запросы

/*
Проверка на сущесвтование чемпиона
сhampion(garen).
champion(taric).

Получение роли чемпиона
position(lulu, Position).
*/

% Запросы с использованием логических операторов

/*
Получение чемпионов которые могут быть танками
(role(Champion, juggernaut); rating(Champion, toughness, 3)).

Получение чемпионов по правилу can_control
findall(Champion, can_control(Champion), Result).

Чемпионы с высоким контролем и являющиеся стрелками
role(Champion, marksman), rating(Champion, control, 3).

Получение чемпионов по правилу good_support
findall(Champion, good_support(Champion), Result).


Количество чемпионов с ролью diver
aggregate_all(count, role(_, diver), Count).


Найти чемпионов, у которых сумма всех рейтингов больше 10, и вывести их имена и сумму рейтингов
findall((Champion, Sum), 
    (champion(Champion), 
     findall(Rating, rating(Champion, _, Rating), Ratings), 
     sum_list(Ratings, Sum), 
     Sum > 10),
    Result).

Подсчитать количество чемпионов, у которых сумма всех рейтингов больше 10
aggregate_all(count, 
    (champion(Champion), 
     findall(Rating, rating(Champion, _, Rating), Ratings), 
     sum_list(Ratings, Sum), 
     Sum > 10), 
    Count).

*/

