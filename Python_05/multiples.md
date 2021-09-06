![Основы Python](https://cs.sberbank-school.ru/inline?access_token=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzEwMzIyNDIsImlhdCI6MTYzMDk0NTg0MiwiZmlsZV91dWlkIjoiMjgxODdhNmUtNDdmMy0xMWVhLWJkMzMtMDA1MDU2MDExYjY4In0.TcvOHhmk1Umf2sfxv_PQRk8Kso-2Gnv38IOiSjSCvsM "Основы Python")

### Описание

Как говорилось ранее, множества содержат неповторяющиеся данные в произвольном порядке. Создадим множество несколькими способами:

``` {.language-python}
>>> a = set()
>>> print(a)
set()
>>> a = set('hello')
>>> print(a)
{'h', 'o', 'l', 'e'}
>>> a = {'a', 'b', 'c', 'd'}
>>> print(a)
{'b', 'c', 'a', 'd'}
>>> a = {i ** 2 for i in range(10)}
>>> print(a)
{0, 1, 4, 81, 64, 9, 16, 49, 25, 36}
```

Множества удобно использовать для удаления повторяющихся элементов:

``` {.language-python}
>>> words = ['hello', 'daddy', 'hello', 'mum']
>>> set(words)
{'hello', 'daddy', 'mum'}
```

### Методы для работы со множествами

Методы множеств, в основном, вызываются по схеме: set.method(). Ниже будут перечислены полезные методы для работы с множествами:

-   **len(s)** - число элементов в множестве (размер множества)

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> len(a)
4
```

-   **x in s** - принадлежит ли **x** множеству **s**

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> 'a' in a
True
```

-   **isdisjoint(other)** - истина, если **set** и **other** не имеют общих элементов

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.isdisjoint('a')
False
>>> a.isdisjoint('f')
True
```

-   **issubset(other)** или **set \<= other** - истина, если все элементы **set** принадлежат **other**

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.issubset({'a', 'b', 'c', 'd','f','e'})
True
```

-   **issuperset(other)** или **set \>= other** - аналогично
-   **union(other, ...)**или **set | other |** ... - возвращает объединение нескольких множеств

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.union({'f','d'})
{'b', 'a', 'c', 'f', 'd'}
```

-   **intersection(other, ...)** или **set & other &** ... - возвращает пересечение множеств

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.intersection({'f','a'})
{'a'}
```

-   **difference(other, ...)** или **set - other** - ... -возвращает множество из всех элементов **set**, не принадлежащие ни одному из **other**

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.difference({'a','f','d'})
{'b', 'c'}
```

-   **symmetric\_difference(other); set \^ other** - возвращает множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.symmetric_difference({'a','d'})
{'b', 'c'}
```

-   **copy()** - копия множества

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> d = a.copy()
>>> print(d)
{'d', 'b', 'a', 'c'}
```

-   **update(other, ...); set |= other |** ... - объединение множеств. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.update({'w','z'})
>>> print(a)
{'z', 'b', 'a', 'c', 'w', 'd'}
```

-   **intersection\_update(other, ...); set &= other &** ... - пересечение множеств. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.intersection_update({'a','d'})
>>> print(a)
{'a', 'd'}
```

-   **difference\_update(other, ...); set -= other |** ... - вычитание множеств. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.difference_update({'a','d'})
>>> print(a)
{'b', 'c'}
```

-   **symmetric\_difference\_update(other); set \^= other** - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.symmetric_difference_update({'a','b'})
>>> print(a)
{'c', 'd'}
```

-   **add(elem)** - добавляет элемент в множество. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.add('r')
>>> print(a)
{'r', 'c', 'a', 'd', 'b'}
```

-   **remove(elem)** - удаляет элемент из множества. **KeyError**, если такого элемента не существует. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.remove('b')
>>> print(a)
{'c', 'a', 'd'}
```

-   **discard(elem)** - удаляет элемент, если он находится в множестве. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.discard('c')
>>> print(a)
{'a', 'b', 'd'}
```

-   **pop()** - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.pop()
'c'
>>> print(a)
{'a', 'b', 'd'}
```

-   **clear()** - очистка множества. Метод, вносящий изменения в множество

``` {.language-python}
>>> a = {'a', 'b', 'c', 'd'}
>>> a.clear()
>>> print(a)
set()
```

 

**frozenset**: единственное отличие от **set** заключается в том, что **frozenset**не меняется, соответственно, к **frozenset** можно применить только те методы, которые не меняют множество.

** **
