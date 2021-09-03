### Целые числа (int)

Целые числа **(int)** поддерживают обычный набор математических операций.

<table>
<col width="50%" />
<col width="50%" />
<thead>
<tr class="header">
<th align="left"><p></p>
<p>Обозначение</p></th>
<th align="left"><p></p>
<p>Действие</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p>a + b<br /></p></td>
<td align="left"><p></p>
<p>Сложение<br /></p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>a - b<br /></p></td>
<td align="left"><p></p>
<p>Вычитание<br /></p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>a * b<br /></p></td>
<td align="left"><p></p>
Умножение<br /></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>a / b<br /></p></td>
<td align="left"><p></p>
<p>Деление<br /></p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>a // b<br /></p></td>
<td align="left"><p></p>
<p>Получение целой части от деления<br /></p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>a % b<br /></p></td>
<td align="left"><p></p>
Остаток от деления<br /></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>-a</p></td>
<td align="left"><p></p>
<p>Смена знака числа<br /></p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>abs(a)</p></td>
<td align="left"><p></p>
<p>Модуль числа<br /></p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>divmod(a,b)</p></td>
<td align="left"><p></p>
<p>Получение пары чисел (a // b, a % b)<br /></p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>a ** b</p></td>
<td align="left"><p>Возведение в степень</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>pow(a, b[, c])<br /></p></td>
<td align="left"><p></p>
<p>a в степени b. Если указано число c, тогда вычисляется остаток от деления на число c<br /></p></td>
</tr>
</tbody>
</table>

``` {.language-python}
>>> 255 + 34
289
>>> 5 * 2
10
>>> 20 / 3
6.666666666666667
>>> 20 // 3
6
>>> 20 % 3
2
>>> 3 ** 4
81
>>> pow(3, 4)
81
>>> pow(3, 4, 27)
0
>>> 3 ** 150
369988485035126972924700782451696644186473100389722973815184405301748249
```

Над целыми числами также можно производить битовые операции (&, | , \^, \<\<, \>\>, \~).

Также целые числа можно переводить в другие системы счисления используя методы:

-   **bin(a)** - перевод числа в двоичную систему счисления
-   **hex(a)** - перевод числа в 16-тиричную систему счисления
-   **oct(a)** - перевод числа в 8-миричную системы счисления

``` {.language-python}
>>> bin(3)
'0b11'
>>> hex(123)
'0x7b'
>>> oct(15)
'0o17'
```

После того как мы перевели число в другую систему счисления, перед самим числом обычно записывается символьное обозначение системы, в которой записано число. Так двоичная система обозначается символами **"0b"**, 16-тиричная - **"0x"**, 8-ричная - **"0o"**.
