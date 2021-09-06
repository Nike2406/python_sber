![Основы Python](https://cs.sberbank-school.ru/inline?access_token=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzA3NTg3NTMsImlhdCI6MTYzMDY3MjM1MywiZmlsZV91dWlkIjoiODU4YzQzNTAtNDdlZi0xMWVhLThhODMtMDA1MDU2MDExYjY4In0.R_BhtoUtgRE4UOlVVKFw6fKT9s0w8cJ64-75AgxJvIY "Основы Python")

### Описание

Строки это упорядоченные последовательности символов, для работы с текстовой информацией. Чтобы присвоить переменной строковое значение, достаточно приравнять выражение в кавычках.

``` {.language-python}
s = 'ain"t it fun?'
s = "ain't it fun?"
```

Как говорилось ранее, разницы между одинарными и двойными кавычками нет, они были введены для того, чтобы можно было не экранировать кавычки внутри предложения, как показано на примере выше. То есть, если бы мы в первом варианте с одинарными кавычками в слове **ant"t** применили также одинарную кавычку, тогда бы мы получили сообщение об ошибке, потому что наша строка состояла бы только из символов **'ain'**, остальной текст не был бы воспринят как часть строки, и в конце стояла бы одинокая открывающая кавычка. Но и этого можно избежать применив экранирование, или другими словами - отмену действия прямого назначения символа:

``` {.language-python}
s = 'ain\'t it fun?'
```

В данном случае символ **\\** отменяет действие кавычки, то есть она не закрывает строку, а воспринимается как часть выражения и заканчивается оно в самом конце, однако не всегда такой вид удобочитаем.

Существуют различные экранированные последовательности, которые позволяют вставить символы, которые трудно ввести с клавиатуры, приведем пример одной из таких последовательностей:

-   **\\n** - перевод строки

``` {.language-python}
>>> s = 'ain"t \nit \nfun?'
>>> print(s)
ain"t
it
fun?
```

### Операции со строками

Строки можно складывать:

``` {.language-python}
>>> s_1 = 'Python'
>>> s_2 = ' '
>>> s_3 = 'is awesome!'
>>> print(s_1 + s_2 + s_3)
'Python is awesome!'
```

Или дублировать:

``` {.language-python}
>>> print('spam' * 3)
spamspamspam
```

С помощью метода **len()** можно узнать количество символов в строке:

``` {.language-python}
>>> len('Python')
6
```

Можно обращаться к элементам по их индексу **(индексация ведется от нуля)**:

``` {.language-python}
>>> s = 'Python'
>>> print(s[0])
P
>>> print(s[5])
n
```

По индексу можно извлекать несколько символов, тогда это будет называться **срез**:

``` {.language-python}
>>> s = 'Python'
>>> print(s[1:2])
y
>>> print(s[0:])
Python
>>> print(s[:3])
Pyt
>>> print(s[:])
Python
```

Методов работы со строками довольно много, мы рассмотрим часть наиболее популярных:

-   **find(str, [start],[end])** - Поиск подстроки в строке. Возвращает номер первого вхождения или -1

``` {.language-python}
>>> s = 'PythonohtyP'
>>> s.find('t')
2
```

-   **rfind(str, [start],[end])**- Поиск подстроки в строке. Возвращает номер последнего вхождения или -1

``` {.language-python}
>>> s = 'PythonohtyP'
>>> s.rfind('t')
8
```

-   **index(str, [start],[end])** - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает **ValueError**

``` {.language-python}
>>> s = 'Python'
>>> s.index('t')
2
```

-   **rindex(str, [start],[end])** - Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает **ValueError**

``` {.language-python}
>>> s = 'PythonohtyP'
>>> s.rindex('t')
8
```

-   **replace(шаблон, замена)** - Замена шаблона

``` {.language-python}
>>> s = 'Python'
>>> s.replace('P', 'AAA')
'AAAython'
```

-   **split(символ)** - Разбиение строки по разделителю

``` {.language-python}
>>> s = 'Python'
>>> s.split('t')
['Py', 'hon']
```

-   **isdigit()**- Состоит ли строка из цифр

``` {.language-python}
>>> s = 'Python'
>>> s.isdigit()
False
```

-   **isalpha()** - Состоит ли строка из букв

``` {.language-python}
>>> s = 'Python'
>>> s.isalpha()
True
```

-   **isalnum()** - Состоит ли строка из цифр или букв

``` {.language-python}
>>> s = 'Python'
>>> s.isalnum()
True
```

-   **islower()** - Состоит ли строка из символов в нижнем регистре

``` {.language-python}
>>> s = 'Python'
>>> s.islower()
False
```

-   **isupper()** - Состоит ли строка из символов в верхнем регистре

``` {.language-python}
>>> s = 'Python'
>>> s.isupper()
False
```

-   **istitle()** - Начинаются ли слова в строке с заглавной буквы

``` {.language-python}
>>> s = 'Python'
>>> s.istitle()
True
```

-   **upper()** - Преобразование строки к верхнему регистру

``` {.language-python}
>>> s = 'Python'
>>> s.upper()
'PYTHON'
```

-   **lower()** - Преобразование строки к нижнему регистру

``` {.language-python}
>>> s = 'Python'
>>> s.lower()
'python'
```

-   **startswith(str)** - Начинается ли строка **S** с шаблона **str**

``` {.language-python}
>>> s = 'Python'
>>> s.startswith('P')
True
```

-   **endswith(str)** - Заканчивается ли строка **S** шаблоном**str**

``` {.language-python}
>>> s = 'Python'
>>> s.endswith('a')
False
```

-   **join(список)** - Сборка строки из списка с разделителем **S**

``` {.language-python}
>>> s = 'Python'
>>> s.join(['a','b','c'])
'aPythonbPythonc'
```

 
