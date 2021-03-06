# Типы данных

# None type - тип, представляющий отсутствие значения.
print("None - ", type(None))
# Логический тип данных (bool) (0|1)
print("True - ", type(True))
print("False - ", type(False))
# int - целое число
print("1 - ", type(1))
# float - число с плавающей точкой
print("5.3 - ", type(5.3))
# complex - комплексное число
print("5 + 4j - ", type(5 + 4j))
# list - список (хранилище данных разного типа)
print("[1, 5.3, False, 4] - ", type([1, 5.3, False, 4]))
# tuple - кортеж (список, который после создания нельзя изменить)
print("(1, True, 3, 5+4j) - ", type((1, True, 3, 5+4j)))
# range - диапазон, неизменяемая последовательность целых чисел
print("range(5) - ", type(range(5)))
# str - строка
print("'Hello' - ", type('Hello'))
# Байт  - это минимальная единица хранения и
# обработки цифровой информации. Данный тип
# допускает возможность производить изменение
# кодировки символов в зависимости от задач.
# bytes - байты
print("b'a' - ", type(b'a'))
# Последовательность байт  - представляет собой
# некую информацию (текст, картинка и т.д.). Помимо
# изменения кодировки, имеет дополнительные возможности
# применять методы к перекодированным строкам и вносить изменения.
# bytearray - массивы байт
print("bytearray([1,2,3]) - ", type(bytearray([1,2,3])))
print("memoryview(bytearray('XYZ', 'utf-8')) - ", type(memoryview(bytearray('XYZ', 'utf-8'))))
# Множества - коллекции для неповторяющихся данных,
# хранящие эти данные в случайном порядке.
# set - множество
print("{'a', 3, True} - ", type({'a', 3, True}))
# frozenset - неизменяемое множество
print("frozenset({1, 2, 3}) - ", type(frozenset({1, 2, 3})))
# dict - словарь (являются набором пар "ключ"-"значение")
print("{'a' : 32} - ", type({'a' : 32}))