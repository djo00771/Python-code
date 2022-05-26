class Prakticum17():
    def __init__(self, numbers, element):
        self.num1 = numbers
        self.num2 = element

    def sorted_num(self):
        """Сортировка пузырьком"""
        for i in range(len(numbers)):
            for j in range(len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return (numbers)

    def binary_search(self, array, element, left, right):
        """Алгоритм двоичного поиска"""
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует
        middle = (right + left) // 2  # находимо середину
        if array[middle] == element:  # если элемент в середине,
            return middle  # возвращаем этот индекс
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return self.binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return self.binary_search(array, element, middle + 1, right)


try:
    numbers = [int(x) for x in input("Введите числа от -999 до 999 в любом порядке, через пробел: ").split()]
    element = int(input('Введите число от 1 до 99: '))
    array = [i for i in range(1, 100)]
    obj = Prakticum17(numbers, element)
    print(*obj.sorted_num(), '\nСписок отсортирован')
    print(obj.binary_search(array, element, 0, 99), '\nПредыдущий элемент числа')

except Exception:
    print('Ошибка, вы ввели число за пределами от 0 до 99')
