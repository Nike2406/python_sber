![Основы Python](https://cs.sberbank-school.ru/inline?access_token=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzEwMzMzNTAsImlhdCI6MTYzMDk0Njk1MCwiZmlsZV91dWlkIjoiYWNkOGVjZWEtNDcxZi0xMWVhLWFhMDgtMDA1MDU2MDExYjY4In0.N8I1umGlWv6tzJNvZYIaizbFqEO-KUVoXAY7b7vMLRk "Основы Python")

### Описание

Функции в Python это объекты, принимающие аргументы и возвращающие значение. Функции определяются с помощью инструкции **def**:

``` {.language-python}
def sum(x, y):
return x + y
```

Функции позволяют упаковывать часть кода для его последующего повторного вызова. В примере выше определена функция с именем **sum**, которая принимает два параметра **x**и **y**, и возвращает результат их суммы. Обратившись к этой функции по имени и задав параметры, мы можем получить результат:

``` {.language-python}
>>> sum(34, 12)
46
>>> sum('abc', 'def')
'abcdef'
```

Инструкция **return**позволяет вернуть значение, которое нам необходимо. Это необходимо для того, чтобы получить определенный результат и затем дальше использовать его в программе.

Функция может быть любой сложности, внутри конструкции **def -\> return**, мы можем написать любой код. Смысл в функциях заключается в том, чтобы не писать один и тот же код повторно, а просто, в нужный момент, вызывать заранее написанную функцию. Так же функция может быть без параметров или может не возвращать какое-то конкретное значение или не заканчиваться инструкцией **return** вовсе:

``` {.language-python}
def fun():
var = 'Python'
if len(var) >= 6:
print(var)
return           # В этом случае функция вернет значение None
```

Код под инструкцией **def** будет относиться к функции до тех пор, пока он вложен в эту инструкцию, то есть отступает от **def**.

Функции бывают разных типов:

-   **Глобальные функции** - такие функции доступны из любой части кода файла, в котором они написаны. Глобальные функции доступны из других модулей, но об этом мы расскажем в разделе "Подключение модулей".

``` {.language-python}
# Объявляем функцию 
def solve(s):
c = []
for i in range(len(s)):
if i%2 == 0:
c.append(s[i])
return c
# вызываем функцию solve с заданными параметрами и выводим результат ее работы
print(solve([1, 2, 3, 4, 5, 6, 7, 8]))
```

-   **Локальные функции** - функции, объявленные внутри других функций. Вызвать их можно только внутри функции, в которой они объявлены. Их удобно использовать, если необходима небольшая вспомогательная функция, которая больше нигде не используется.
-   **Лямбда-функции** - особые, анонимные функции, имеющие ряд ограничений, по сравнению с обычными функциями. Они локально решают единственную задачу. Применение такой функции выглядит, как выражение, давайте посмотрим на примере:

``` {.language-python}
# Обычная функция 
def search_len(arg_1):
return len(arg_1)
# Лямбда-функция 
result = lambda x: len(x)
```

Обычно, лямбда-функции применяют при вызове функций, которые в качестве аргументов содержат функции. Проблема использования лямбда-функций состоит в том, что иногда усложняется читаемость кода.

``` {.language-python}
>>> func = lambda x, y: x + y
>>> func(1, 2)
3
>>> func('a', 'b')
'ab'
>>> (lambda x, y: x + y)(1, 2)
3
>>> (lambda x, y: x + y)('a', 'b')
'ab'
```

Лямбда-функции не имеют имени, поэтому могут возникать проблемы с отловом ошибки. В рамках данного курса мы не будем более подробно останавливаться на данном виде функций и рекомендуем использовать стандартный, более явный тип.

-   **Методы**- функции, работающие в связке с тем типом данных, который ассоциирован с данной функцией. В прошлых разделах приводились примеры методов для каждого типа. Более подробный разбор методов является частью объектно-ориентированного программирования и не входит в рамки данного курса.

Функции могут принимать произвольное количество аргументов, для этого необходимо поставить символ \* перед именем аргумента функции:

``` {.language-python}
>>> def func(*args):
return args
>>> func(1, 2, 3, 'abc')
(1, 2, 3, 'abc')
```

Как мы видим в таком случае образуется кортеж из этих аргументов. Также можно принимать аргументы в виде словаря, для этого необходимо использовать символ \*\*:

``` {.language-python}
>>> def func(**kwargs):
return kwargs
>>> func(a=1, b=2, c=3)
{'a': 1, 'b': 2, 'c': 3}
```

Очень важно документировать описание к любой функции, чтобы каждый раз не разбирать написанное заново. Для этого используют строки, заключенные в тройные кавычки. Поскольку описание функции зачастую состоит более, чем из 1 строки, использование строк с тройными кавычками очень удобно. Обычно под документирование выделяют место между определением функции и началом основного кода:

``` {.language-python}
def solve(s):
''' Функция solve(s) принимает список
создает пустой список
находит элементы с четным индексом (включая 0)
заносит их в созданный список и возвращает его
'''
c = []
for i in range(len(s)):
if i%2 == 0:
c.append(s[i])
return c
```

Переменные, которые объявляются внутри функций являются **локальными**. Изменение этих переменных и обращение к ним происходят только внутри функций, где они были объявлены. Если же переменные объявлены вне функций, они являются **глобальными**. С глобальными переменными надо обходиться осторожно. Их удобно использовать, потому что к ним можно обращаться из любой части кода и даже из других модулей, но, если в коде происходит неконтролируемое изменение глобальной переменной, то поиск ошибки может перерасти в головную боль. Рассмотрим пример:

    var_1 = [1,2,3]  def func(a):    var_1 = []    for i in a:        var_1.append(i*2)    return var_1print(func(var_1))
    print(var_1)

Зеленым цветом обозначена **глобальная** переменная, красным - **локальная**. Глобальная переменная var\_1 в данном случае остается неизменной, т.к. она используется только в качестве параметра для функции и нигде не происходит манипуляций над ней. Внутри этой функции изменения происходят с локальной переменной var\_1. Результат выполнения такой программы будет следующий:

``` {.language-python}
[2, 4, 6]
[1, 2, 3]
```

Теперь приведем пример плохого кода, в котором происходят манипуляции с глобальной переменной:

``` {.language-python}
var_1 = [1,2,3]

def func(a):
var_2 = []
for i in a:
var_2.append(i*2)
return var_2
var_3 = var_1
var_3.append(12)
print(func(var_1))
print(var_1)
```

-   Попробуйте угадать, каким будет результат выполнения из примера выше?
-   Ответ

1) [2, 4, 6], [1, 2, 3]

2) [2, 4, 6, 24], [1, 2, 3, 12]

3) Затрудняюсь ответить

2) [2, 4, 6, 24], [1, 2, 3, 12]

За счет того, что var\_3 связывается с тем же объектом, что и var\_1, то изменения над глобальной переменной var\_3 приведет к изменению другой глобальной переменной  var\_1. В итоге эта цепочка меняет результат выполнения функции, поскольку на вход подаются уже другие данные. Вот пример неосторожного обращения с глобальными переменными. А теперь представьте, что у вас сотни строк кода и десяток функций, можете представить сколько времени понадобится на поиск подобной ошибки? 

### Дополнительно

Давайте еще раз рассмотрим один из примеров данного раздела:

``` {.language-python}
def solve(s):
''' Функция solve(s) принимает список
создает пустой список
находит элементы с четным индексом (включая 0)
заносит их в созданный список и возвращает его
'''
c = []
for i in range(len(s)):
if i%2 == 0:
c.append(s[I])
return c
```

В описании к функции написано, что она принимает список. А что, если ей на вход попадёт строка или словарь? 

В случае со строкой все будет нормально, но вот словарь вызовет ошибку. Чтобы избежать подобную ситуацию, мы можем прописать условия проверки входного параметра. Сделать это можно с помощью условия **assert**:

``` {.language-python}
def solve(s):
''' Функция solve(s) принимает список
создает пустой список
находит элементы с четным индексом (включая 0)
заносит их в созданный список и возвращает его
'''
assert type(s) == list
c = []
for i in range(len(s)):
if i%2 == 0:
c.append(s[I])
return c
```

Теперь, если на вход функции solve() попадет какой-либо тип кроме списка, **assert**проверит это и выведет ошибку определенного рода:

``` {.language-python}
Traceback (most recent call last):
File "solve.py", line 11, in <module>
print(solve(123))
File "solve.py", line 3, in solve
assert type(s) == list
AssertionError
```

Данный инструмент полезно использовать для выявления неустранимых ошибок программы. То есть, в данном случае, наша функция не предполагает получения данных отличных от типа "список". Однако, в случае, когда что-то пошло не так, с помощью **assert**, мы будем знать об этом.
