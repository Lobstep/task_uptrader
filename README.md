# task_uptrader
тестовое задание
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

Меню реализовано через template tag
Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
Хранится в БД.
Редактируется в стандартной админке Django
Активный пункт меню определяется исходя из URL текущей страницы
Меню на одной странице может быть несколько. Они определяются по названию.
При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
На отрисовку каждого меню требуется ровно 1 запрос к БД
Нужен Django-app, который позволяет вносить в БД Меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

{% draw_menu "main_menu" %}

При выполнении задания из библеотек следует использовать только Django и стандартную библеотеку Python.