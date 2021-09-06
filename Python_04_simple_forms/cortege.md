![Основы Python](https://cs.sberbank-school.ru/inline?access_token=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzA3NjA5NjgsImlhdCI6MTYzMDY3NDU2OCwiZmlsZV91dWlkIjoiYTAwOTczMDgtNDdmMi0xMWVhLTg4MDAtMDA1MDU2MDExYjY4In0.0PE-evToGKNbAQ_y7dw3JjP_1yzwAfwgAAfoZrVleqo "Основы Python")

### Описание

Как говорилось ранее, кортежи это неизменяемые списки. Их удобно использовать для защиты данных, которые не должны быть изменены. Создать кортеж можно следующим образом:

``` {.language-python}
>>> a = (1, 2, 3, 4, 5, 6)
>>> print(a)
(1, 2, 3, 4, 5, 6)
```

Чтобы создать пустой кортеж, необходимо применить метод **tuple()**:

``` {.language-python}
>>> a = tuple()
>>> print(a)
()
```

Если вам нужен кортеж из одного элемента, то он создается следующим образом:

``` {.language-python}
>>> a = (1,)
>>> print(a)
(1,)
```

Если не указать на конце запятую, тогда мы получим не кортеж, а элемент того типа, который мы указали:

``` {.language-python}
>>> a = (1)
>>> print(a)
1
```

Кстати, необязательно даже указывать скобки, кортеж можно создать и без них:

``` {.language-python}
>>> a = 1, 2, 3, 4
>>> print(a)
(1, 2, 3, 4)
```

Над кортежами работают все операции, работающие со списками, которые не вносят изменения в список.
