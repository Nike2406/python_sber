Арифметические операторы
========================

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left"><p></p>
<p>Символ</p></th>
<th align="left"><p></p>
<p>Описание</p></th>
<th align="left"><p></p>
<p>Пример</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p>+</p></td>
<td align="left"><p></p>
<p>Оператор суммы</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(5 + 8)</p>
<p>13</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>-</p></td>
<td align="left"><p></p>
<p>Оператор разности</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(31 - 2)</p>
<p>29</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>*</p></td>
<td align="left"><p></p>
<p>Оператор произведения</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(12 * 9)</p>
<p>108</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>/</p></td>
<td align="left"><p></p>
<p>Оператор деления</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(6 / 4)</p>
<p>1.5</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>%</p></td>
<td align="left"><p></p>
<p>Оператор получения остатка от деления</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(6 % 4)</p>
<p>2</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>**</p></td>
<td align="left"><p></p>
<p>Оператор возведения в степень</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(9 ** 2)</p>
<p>81</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>//</p></td>
<td align="left"><p></p>
<p>Оператор целочисленного деления</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(6 // 4)</p>
<p>1</p></td>
</tr>
</tbody>
</table>

### Операторы сравнения (реляционные)

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left"><p></p>
<p>Символ<br /></p></th>
<th align="left"><p></p>
<p>Описание<br /></p></th>
<th align="left"><p></p>
<p>Пример<br /></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p>==</p></td>
<td align="left"><p></p>
<p>Проверяет, равны ли операнды между собой. Если они равны, то выражение становится истинным.</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(5 == 5)</p>
<p>True<br />&gt;&gt;&gt; print(6 == 44)</p>
<p>False</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>!=</p></td>
<td align="left"><p></p>
<p>Проверяет, равны ли операнды между собой. Если они не равны, то выражение становится истинным.</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(12 != 12)</p>
<p>False<br />&gt;&gt;&gt; print(1231 != 0.4)</p>
<p>True</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>&gt;</p></td>
<td align="left"><p></p>
<p>Проверяет, больше ли левый операнд чем правый, если больше, то выражение становится истинным.</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(53 &gt; 23)</p>
<p>True<br />&gt;&gt;&gt; print(432 &gt;500)</p>
<p>False</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>&lt;</p></td>
<td align="left"><p></p>
<p>Проверяет, меньше ли левый операнд чем правый, если меньше, то выражение становится истинным.</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(5 &lt; 51)</p>
<p>True<br />&gt;&gt;&gt; print(6 &lt; 4)</p>
<p>False</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>&gt;=</p></td>
<td align="left"><p></p>
<p>Проверяет, больше левый операнд, чем правый, или равен ему. Если больше или равен, то выражение становится истинным.<br /></p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(5 &gt;= 5)</p>
<p>True<br />&gt;&gt;&gt; print(6 &gt;=44)</p>
<p>False</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>&lt;=</p></td>
<td align="left"><p></p>
<p>Проверяет, меньше левый операнд, чем правый, или равен ему. Если меньше или равен, то выражение становится истинным.<br /></p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print(32 &lt;= 232)</p>
<p>True<br />&gt;&gt;&gt; print(65 &lt;= 9)</p>
<p>False</p></td>
</tr>
</tbody>
</table>

### Операторы присваивания

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left"><p></p>
<p>Символ<br /></p></th>
<th align="left"><p></p>
<p>Описание<br /></p></th>
<th align="left"><p></p>
<p>Пример<br /></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p>=</p></td>
<td align="left"><p></p>
<p>Присваивает значение правого операнда левому</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; var = 5</p>
<p>&gt;&gt;&gt; print(var)</p>
<p>5</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>+=</p></td>
<td align="left"><p></p>
<p>Прибавляет значение правого операнда к левому и присваивает левому. a += b эквивалентно записи<br />a=a+b</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; var = 5</p>
<p>&gt;&gt;&gt; var += 4</p>
<p>&gt;&gt;&gt; print(var)</p>
<p>9</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>-=</p></td>
<td align="left"><p></p>
<p>Отнимает значение у левого операнда правое и присваивает левому. a -= b эквивалентно записи a = a -b</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; var = 5</p>
<p>&gt;&gt;&gt; var -= 2</p>
<p>&gt;&gt;&gt; print(var)</p>
<p>3</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>*=</p></td>
<td align="left"><p></p>
<p>Умножает значение левого операнда на правое и присваивает левому. a *= b эквивалентно записи a=a*b</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; var = 5</p>
<p>&gt;&gt;&gt; var *= 10</p>
<p>&gt;&gt;&gt; print(var)</p>
<p>50</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>/=</p></td>
<td align="left"><p></p>
<p>Делит значение левого операнда на правое и присваивает левому. a /= b эквивалентно записи a=a/b</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; var = 5</p>
<p>&gt;&gt;&gt; var /= 4</p>
<p>&gt;&gt;&gt; print(var)</p>
<p>1.25</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>%=</p></td>
<td align="left"><p></p>
<p>Делит значение левого операнда по остатку на правое и присваивает левому. a %= b эквивалентно записи a = a % b</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; var = 5</p>
<p>&gt;&gt;&gt; var %= 10</p>
&gt;&gt;&gt;print(var)
5</td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>**=</p></td>
<td align="left"><p></p>
<p>Возводит значение левого операнда в степень правого и присваивает левому. a **= b эквивалентно записи a = a ** b</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; var = 5</p>
<p>&gt;&gt;&gt; var **= 8</p>
<p>&gt;&gt;&gt;print(var)</p>
<p>390625</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>//=</p></td>
<td align="left"><p></p>
<p>Целочисленно делит значение левого операнда на правое и присваивает левому. a //= b эквивалентно записи a = a // b</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; var = 5</p>
<p>&gt;&gt;&gt; var //= 30</p>
<p>&gt;&gt;&gt;print(var)</p>
<p>0</p></td>
</tr>
</tbody>
</table>

### Побитовые операторы

Данные операторы работают с данными в двоичной системе счисления. Например число 13 в двоичной системе будет равно 1101

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left"><p></p>
<p>Символ<br /></p></th>
<th align="left"><p></p>
<p>Описание<br /></p></th>
<th align="left"><p></p>
<p>Пример (в двоичной системе)<br /></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p>&amp;</p></td>
<td align="left"><p></p>
<p>Бинарный &quot;И&quot; оператор, копирует бит в результат только если бит присутствует в обоих операндах</p></td>
<td align="left"><p></p>
<p>0&amp;0=0</p>
<p>1&amp;0=0</p>
<p>0&amp;1=0</p>
<p>1&amp;1=1</p>
<p>101 &amp; 110 = 100<br /></p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>|</p></td>
<td align="left"><p></p>
<p>Бинарный &quot;ИЛИ&quot; оператор копирует бит, если тот присутствует в хотя бы в одном операнде</p></td>
<td align="left"><p></p>
<p>0|0=0</p>
<p>1|0=1</p>
<p>0|1=1</p>
<p>1|1=1</p>
<p>101 | 110 = 111<br /></p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>^</p></td>
<td align="left"><p></p>
<p>Бинарный &quot;Исключительное ИЛИ&quot; оператор копирует бит только если бит присутствует в одном из операндов, но не в обоих сразу</p></td>
<td align="left"><p></p>
<p>0^0=0</p>
<p>1^0=1</p>
<p>0^1=1</p>
<p>1^1=0<br />101 ^ 110 = 011<br /></p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>~</p></td>
<td align="left"><p></p>
<p>Побитовая операция &quot;НЕ&quot;. Для числа a соответствует -(a+1).
 ~ инверсия значение любого бита числа изменяется на противоположное</p></td>
<td align="left"><p></p>
<p>~1 = -10<br />~0 = -1</p>
<p>~101 = -110</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>&gt;&gt;</p></td>
<td align="left"><p></p>
<p>Побитовый сдвиг вправо. Значение левого операнда &quot;сдвигается&quot; вправо на количество бит указанных в правом операнде</p></td>
<td align="left"><p></p>
<p>100 &gt;&gt; 2 = 001</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>&lt;&lt;</p></td>
<td align="left"><p></p>
<p>Побитовый сдвиг влево. Значение левого операнда &quot;сдвигается&quot; влево на количество бит указанных в правом операнде</p></td>
<td align="left"><p></p>
<p>100 &lt;&lt; 2 = 10000</p></td>
</tr>
</tbody>
</table>

### Логические операторы

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left"><p></p>
<p>Символ<br /></p></th>
<th align="left"><p></p>
<p>Описание<br /></p></th>
<th align="left"><p></p>
<p>Пример<br /></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p>and</p></td>
<td align="left"><p></p>
<p>Логический оператор &quot;И&quot;. Условие будет истинным если оба операнда истина</p></td>
<td align="left"><p></p>
<p>True and True = True.</p>
<p>True and False = False.</p>
<p>False and True = False.</p>
<p>False and False = False.</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>or</p></td>
<td align="left"><p></p>
<p>Логический оператор &quot;ИЛИ&quot;. Если хотя бы один из операндов истинный, то и все выражение будет истинным</p></td>
<td align="left"><p></p>
<p>True or True = True.</p>
<p>True or False = True.</p>
<p>False or True = True.</p>
<p>False or False = False.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<p>not</p></td>
<td align="left"><p></p>
<p>Логический оператор &quot;НЕ&quot;. Изменяет логическое значение операнда на противоположное</p></td>
<td align="left"><p></p>
<p>not True = False.</p>
<p>not False = True.</p></td>
</tr>
</tbody>
</table>

### Операторы членства

Данные операторы участвуют в поиске данных в некоторой последовательности.

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left"><p></p>
<p>Символ<br /></p></th>
<th align="left"><p></p>
<p>Описание<br /></p></th>
<th align="left"><p></p>
<p>Пример<br /></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p>in</p></td>
<td align="left"><p></p>
<p>Возвращает истину, если элемент присутствует в последовательности, иначе возвращает ложь</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; print('he' in 'hello')</p>
<p>True</p>
<p>&gt;&gt;&gt; print(5 in [1, 2, 3, 4, 5])</p>
<p>True</p>
<p>&gt;&gt;&gt; print(12 in [1, 2, 4, 56])</p>
<p>False</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>not in</p></td>
<td align="left"><p></p>
<p>Возвращает истину если элемента нет в последовательности</p></td>
<td align="left"><p></p>
<p>результаты противоположны примерам выше</p></td>
</tr>
</tbody>
</table>

### Операторы тождественности

Данные операторы помогают сравнить размещение двух объектов в памяти компьютера

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left"><p></p>
<p>Символ<br /></p></th>
<th align="left"><p></p>
<p>Описание<br /></p></th>
<th align="left"><p></p>
<p>Пример<br /></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<p>is</p></td>
<td align="left"><p></p>
<p>Возвращает истину, если оба операнда указывают на один объект</p></td>
<td align="left"><p></p>
<p>&gt;&gt;&gt; a = 12</p>
<p>&gt;&gt;&gt;b = 12</p>
<p>&gt;&gt;&gt; a is b</p>
<p>True</p>
<p>&gt;&gt;&gt; c = 22</p>
<p>&gt;&gt;&gt; a is c</p>
<p>False</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<p>is not</p></td>
<td align="left"><p></p>
<p>Возвращает ложь, если оба операнда указывают на один объект</p></td>
<td align="left"><p></p>
<p>результаты противоположны примерам выше<br /></p></td>
</tr>
</tbody>
</table>

