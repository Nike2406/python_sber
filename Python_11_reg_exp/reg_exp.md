![Основы Python](https://cs.sberbank-school.ru/inline?access_token=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzEwMzYzMTUsImlhdCI6MTYzMDk0OTkxNSwiZmlsZV91dWlkIjoiM2E4ODMxZGUtNDgwZC0xMWVhLTkwMTYtMDA1MDU2MDExYjY4In0.OWOwpa5PD9TCJCZY5N9rZl291Koq8sbe2GTIAMEFWuk "Основы Python")

### Регулярные выражения

В качестве дополнительного материала мы расскажем про регулярные выражения, с которыми рано или поздно вы можете столкнуться.

Регулярные выражения - выражения для поиска и замены части текста в строке или файле. Для работы с ними необходимо подключить модуль "re" из стандартной библиотеки Python.

Наиболее часто регулярные выражения используются для поиска в строке, разбиении строк, замены части строк. Вот некоторые методы для работы с регулярными выражениями:

-   **re.match(шаблон, строка)** - ищет заданный шаблон с самого начала строки.

``` {.language-python}
>>> import re
>>> print(re.match(r'Hey', 'Hey Hey'))
<re.Match object; span=(0, 3), match='Hey'>    # Данные нашлись
>>> print(re.match(r'Hey', 'hey Hey'))
None     # Данные не нашлись, т.к. строка отличается от шаблона с первого символа 
# Обратите внимание на синтаксис, перед шаблоном ставится латинская буква r
```

-   **re.search(шаблон, строка)** - ищет заданный шаблон по всей строке, возвращает результат при первом совпадении.

``` {.language-python}
>>> import re
>>> print(re.search(r'Hey', 'hey Hey').group(0))     # Добавляем метод group(), чтобы вывести содержимое поиска
Hey
```

-   **re.findall(шаблон, строка)** - ищет заданный шаблон и возвращает все совпадения в виде списка.

``` {.language-python}
>>> import re
>>> print(re.findall(r'Hey', 'hey Hey Hey Hey'))
['Hey', 'Hey', 'Hey']
```

-   **re.split(шаблон, строка)** - разделяет строку по заданному шаблону

``` {.language-python}
>>> import re
>>> print(re.split(r'y', 'hey Hey Hey Hey'))
['he', ' He', ' He', ' He', '']
```

-   **re.sub(шаблон, замена, строка)** - находит шаблон в строке и производит замену

``` {.language-python}
>>> import re
>>> print(re.sub(r'Hey', '?', 'hey Hey Hey Hey'))
hey ? ? ?
```

-   **re.compile(шаблон)** - позволяет собирать регулярное выражение в отдельный объект для последующего использования

``` {.language-python}
>>> ex_str = re.compile('Hey')
>>> result = ex_str.findall('hey Hey Hey')
>>> print (result)
['Hey', 'Hey']
>>> result2 = ex_str.findall('Hey')
>>> print (result2)
['Hey']
```

Перейдем к самой интересной части - представьте, что вам необходимо произвести чтение "грязного" файла и убрать из него все лишнее, но при этом вы не можете сказать точно, что необходимо убрать. Эту задачу можно решить используя специальные символы:

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<tbody>
<tr class="odd">
<td align="left">Оператор</td>
<td align="left">Значение</td>
<td align="left">Пример</td>
</tr>
<tr class="even">
<td align="left">.</td>
<td align="left">Один любой символ, кроме символа переноса строки \n</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'h..', 'hey Hey Hey Hey'))</p>
<p>hey</p></td>
</tr>
<tr class="odd">
<td align="left">?</td>
<td align="left">0 или 1 вхождение шаблона слева</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'h?', 'hey Hey Hey Hey'))</p>
<p>['h', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']</p></td>
</tr>
<tr class="even">
<td align="left">+</td>
<td align="left">1 и более вхождений шаблона слева</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'H.+', 'hey Hey Hey Hey'))</p>
<p>['Hey Hey Hey']</p>
<p>&gt;&gt;&gt; print(re.findall(r'H+', 'hey Hey Hey Hey'))</p>
<p>['H', 'H', 'H']</p></td>
</tr>
<tr class="odd">
<td align="left">*</td>
<td align="left">0 или более вхождений слева</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'H*', 'hey Hey Hey Hey'))</p>
<p>['', '', '', '', 'H', '', '', '', 'H', '', '', '', 'H', '', '', '']</p></td>
</tr>
<tr class="even">
<td align="left">\w</td>
<td align="left">Любая цифра или буква (\W — все, кроме буквы или цифры)</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'\w', 'hey Hey Hey Hey'))</p>
<p>['h', 'e', 'y', 'H', 'e', 'y', 'H', 'e', 'y', 'H', 'e', 'y']</p></td>
</tr>
<tr class="odd">
<td align="left">\d</td>
<td align="left">Любая цифра [0-9] (\D — все, кроме цифры)</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'\d', 'hey Hey1 Hey2 Hey3'))</p>
<p>['1', '2', '3']</p></td>
</tr>
<tr class="even">
<td align="left">\s</td>
<td align="left">Любой пробельный символ (\S — любой непробельный символ)</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'\s', 'hey Hey1 Hey2 Hey3'))</p>
<p>[' ', ' ', ' ']</p></td>
</tr>
<tr class="odd">
<td align="left">\b</td>
<td align="left">Граница слова</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'\b\w', 'hey, Hey1, Hey2, Hey3'))</p>
<p>['h', 'H', 'H', 'H']</p></td>
</tr>
<tr class="even">
<td align="left">[..]</td>
<td align="left">Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'[Hy]', 'hey, Hey1, Hey2, Hey3'))</p>
<p>['y', 'H', 'y', 'H', 'y', 'H', 'y']</p></td>
</tr>
<tr class="odd">
<td align="left">\</td>
<td align="left">Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'\.', 'hey. Hey1. Hey2. Hey3'))</p>
<p>['.', '.', '.']</p></td>
</tr>
<tr class="even">
<td align="left">^ и $</td>
<td align="left">Начало и конец строки соответственно</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'..$', 'hey. Hey1. Hey2. Hey3'))</p>
<p>['y3']</p></td>
</tr>
<tr class="odd">
<td align="left">{n,m}</td>
<td align="left">От n до m вхождений ({,m} — от 0 до m)</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'\w{2}', 'hey. Hey1. Hey2. Hey3'))</p>
<p>['he', 'He', 'y1', 'He', 'y2', 'He', 'y3']</p></td>
</tr>
<tr class="even">
<td align="left">a|b</td>
<td align="left">Соответствует a или b</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'h|3', 'hey. Hey1. Hey2. Hey3'))</p>
<p>['h', '3']</p></td>
</tr>
<tr class="odd">
<td align="left">()</td>
<td align="left">Группирует выражение и возвращает найденный текст</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'(\w\w\w)', 'hey. Hey1. Hey2. Hey3\n'))</p>
<p>['hey', 'Hey', 'Hey', 'Hey']</p></td>
</tr>
<tr class="even">
<td align="left">\t,\n,\r</td>
<td align="left">Символ табуляции, новой строки и возврата каретки соответственно</td>
<td align="left"><p>&gt;&gt;&gt; print(re.findall(r'\n', 'hey. Hey1. Hey2. Hey3\n'))</p>
<p>['\n']</p></td>
</tr>
</tbody>
</table>

Рассмотрим пример. Ниже представлен фрагмент лога - файла, записывающего события при работе программы:

#### Фрагмент лог-файла:

Oct 16 20:10:10 legacy sshd[59955]: Did not receive identification string from 211.156.128.23 
Oct 16 20:19:43 legacy sshd[59961]: Illegal user patrick from 211.156.128.23 
Oct 16 20:19:53 legacy sshd[59966]: Illegal user patrick from 211.156.128.23 
Oct 16 20:20:22 legacy sshd[59981]: Illegal user rolo from 211.156.128.23 
Oct 16 20:20:28 legacy sshd[59983]: Illegal user iceuser from 211.156.128.23 
Oct 16 20:20:34 legacy sshd[59985]: Illegal user horde from 211.156.128.23 
Oct 16 20:20:38 legacy sshd[59987]: Illegal user cyrus from 211.156.128.23 
Oct 16 20:20:48 legacy sshd[59991]: Illegal user wwwrun from 211.156.128.23 
Oct 16 20:20:58 legacy sshd[59993]: Illegal user matt from 211.156.128.23 
Oct 17 01:29:25 legacy sshd[60366]: Illegal user test from 218.237.4.57 
Oct 17 01:29:28 legacy sshd[60368]: Illegal user guest from 218.237.4.57 
Oct 17 01:29:32 legacy sshd[60370]: Illegal user admin from 218.237.4.57 
Oct 17 01:29:35 legacy sshd[60374]: Illegal user admin from 218.237.4.57 
Oct 17 01:29:38 legacy sshd[60376]: Illegal user user from 218.237.4.57 
Oct 17 01:29:51 legacy sshd[60387]: Illegal user test from 218.237.4.57 
Oct 17 23:29:11 legacy sshd[64098]: Did not receive identification string from 147.46.76.225 
Oct 17 23:37:18 legacy sshd[64139]: Illegal user patrick from 147.46.76.225 
Oct 17 23:37:22 legacy sshd[64141]: Illegal user patrick from 147.46.76.225 
Oct 17 23:39:35 legacy sshd[64151]: fatal: Timeout before authentication for 147.46.76.225 
Oct 18 00:09:42 legacy sshd[64320]: Illegal user test from 211.174.181.158 
Oct 18 00:09:45 legacy sshd[64322]: Illegal user guest from 211.174.181.158 
Oct 18 00:10:18 legacy sshd[64330]: Illegal user test from 211.34.197.3 
Oct 18 00:10:22 legacy sshd[64332]: Illegal user guest from 211.34.197.3 
Oct 18 00:10:25 legacy sshd[64334]: Illegal user admin from 211.34.197.3 
Oct 18 00:10:29 legacy sshd[64336]: Illegal user admin from 211.34.197.3 
Oct 18 00:10:32 legacy sshd[64338]: Illegal user user from 211.34.197.3 
Oct 18 00:10:44 legacy sshd[64347]: Illegal user test from 211.34.197.3 
Oct 18 22:47:31 legacy sshd[72101]: Did not receive identification string from 83.64.18.219 
Oct 18 23:02:01 legacy sshd[72124]: Illegal user patrick from 83.64.18.219 
Oct 18 23:02:02 legacy sshd[72126]: Illegal user patrick from 83.64.18.219 
Oct 18 23:02:15 legacy sshd[72138]: Illegal user rolo from 83.64.18.219 
Oct 18 23:02:17 legacy sshd[72140]: Illegal user iceuser from 83.64.18.219 
Oct 18 23:02:18 legacy sshd[72142]: Illegal user horde from 83.64.18.219 
Oct 18 23:02:20 legacy sshd[72144]: Illegal user cyrus from 83.64.18.219 
Oct 18 23:02:22 legacy sshd[72148]: Illegal user wwwrun from 83.64.18.219 
Oct 18 23:02:24 legacy sshd[72150]: Illegal user matt from 83.64.18.219 
Oct 18 23:02:25 legacy sshd[72152]: Illegal user test from 83.64.18.219 
Oct 18 23:02:31 legacy sshd[72154]: Illegal user test from 83.64.18.219 
Oct 18 23:02:33 legacy sshd[72156]: Illegal user test from 83.64.18.219 
Oct 18 23:02:34 legacy sshd[72158]: Illegal user test from 83.64.18.219 
Oct 18 23:02:35 legacy sshd[72160]: Illegal user www-data from 83.64.18.219 
Oct 18 23:02:37 legacy sshd[72162]: Illegal user mysql from 83.64.18.219 
Oct 18 23:02:40 legacy sshd[72166]: Illegal user adm from 83.64.18.219 
Oct 18 23:02:41 legacy sshd[72168]: Illegal user apache from 83.64.18.219 
Oct 18 23:02:43 legacy sshd[72170]: Illegal user irc from 83.64.18.219 
Oct 18 23:02:44 legacy sshd[72172]: Illegal user irc from 83.64.18.219 
Oct 18 23:02:46 legacy sshd[72174]: Illegal user adm from 83.64.18.219 
Oct 18 23:02:51 legacy sshd[72182]: Illegal user jane from 83.64.18.219 
Oct 18 23:02:53 legacy sshd[72184]: Illegal user pamela from 83.64.18.219 
Oct 18 23:03:00 legacy sshd[72196]: Illegal user cosmin from 83.64.18.219 
Oct 18 23:03:56 legacy sshd[72270]: Illegal user cip52 from 83.64.18.219 
Oct 18 23:03:57 legacy sshd[72272]: Illegal user cip51 from 83.64.18.219 
Oct 18 23:04:05 legacy sshd[72276]: Illegal user noc from 83.64.18.219 
Oct 18 23:04:12 legacy sshd[72287]: Illegal user webmaster from 83.64.18.219 
Oct 18 23:04:18 legacy sshd[72297]: Illegal user data from 83.64.18.219 
Oct 18 23:04:20 legacy sshd[72299]: Illegal user user from 83.64.18.219 
Oct 18 23:04:26 legacy sshd[72301]: Illegal user user from 83.64.18.219 
Oct 18 23:04:27 legacy sshd[72303]: Illegal user user from 83.64.18.219 
Oct 18 23:04:29 legacy sshd[72305]: Illegal user web from 83.64.18.219 
Oct 18 23:04:30 legacy sshd[72307]: Illegal user web from 83.64.18.219 
Oct 18 23:04:32 legacy sshd[72309]: Illegal user oracle from 83.64.18.219 
Oct 18 23:04:33 legacy sshd[72311]: Illegal user sybase from 83.64.18.219 
Oct 18 23:04:34 legacy sshd[72313]: Illegal user master from 83.64.18.219 
Oct 18 23:04:36 legacy sshd[72315]: Illegal user account from 83.64.18.219 
Oct 18 23:04:38 legacy sshd[72317]: Illegal user backup from 83.64.18.219 
Oct 18 23:04:39 legacy sshd[72319]: Illegal user server from 83.64.18.219 
Oct 18 23:04:41 legacy sshd[72321]: Illegal user adam from 83.64.18.219 
Oct 18 23:04:42 legacy sshd[72323]: Illegal user alan from 83.64.18.219 
Oct 18 23:04:44 legacy sshd[72325]: Illegal user frank from 83.64.18.219 
Oct 18 23:04:46 legacy sshd[72327]: Illegal user george from 83.64.18.219 
Oct 18 23:04:47 legacy sshd[72329]: Illegal user henry from 83.64.18.219 
Oct 18 23:04:49 legacy sshd[72331]: Illegal user john from 83.64.18.219 
Oct 18 23:04:58 legacy sshd[72343]: Illegal user test from 83.64.18.219 
Oct 18 23:47:19 legacy sshd[72387]: Did not receive identification string from 67.19.240.114 
Oct 19 00:04:37 legacy sshd[72447]: Illegal user patrick from 67.19.240.114 
Oct 19 00:04:38 legacy sshd[72449]: Illegal user patrick from 67.19.240.114

В нем есть характерная строка, сообщающая, что программа не получила идентификатор пользователя при подключении:

``` {.language-python}
Did not receive identification string from ip_address
```

Давайте напишем программу, которая найдет все ip адреса таких неавторизованных юзеров:

``` {.language-python}
import re
logfile = open('logfile.txt', 'r')
for string in logfile:
if re.findall(r'Did', string):
print(re.findall(r'\d+\.\d+\.\d+\.\d+', string))
```

Мы построчно читаем файл и ищем строки, в которых есть сочетание 'Did'. В каждой такой строке мы находим ip адрес. Он состоит из 4 наборов цифр, разделенных точками между собой.

Сыграем?

![](https://www.google.com/s2/favicons?domain=regexcrossword.com) [regexcrossword.com](/programs/14669/item/579109/launch)

[Перейти](/programs/14669/item/579109/launch)

Здесь приведена ссылка на портал, где можно сыграть в кроссворд из регулярных выражений. Шаблоны записываются по горизонтали и вертикали и вам необходимо вписать тот символ, который удовлетворяет одному или нескольким шаблонам. Задания выстроены по уровню сложности от простого к сложному. С помощью этой игры вы сможете открыть для себя интересные полезные комбинации для формирования собственных шаблонов.

### Итоговый проект

Для выполнения данного упражнения вам необходимо использовать некоторые программы из предыдущих упражнений.

Вам нужно написать программу, которая будет читать файл из предыдущего упражнения, заниматься его чисткой, формировать почтовые адреса для сотрудников, генерировать пароли безопасности для входа в почту, заносить информацию в этот файл и перезаписывать его.

1) Вы можете использовать предыдущие наработки

2) Ваша программа должна очистить файл от всех невалидных данных (строки с пустыми данными, некорректными именами, некорректными телефонами и городами)

3) При очистке исходного файла, все невалидные данные должны удаляться из него и сохраняться в отдельный текстовый файл

4) Поиск информации в файле должен осуществляться с помощью регулярных выражений

5) Разрешается использовать готовую функцию формирования почтового адреса или написать свою

6) Сгенерированные пароли должны заноситься в исходный файл в отдельный столбец "PASSWORD"
