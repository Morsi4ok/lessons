"""
В школе решили набрать три новых класса по программированию.
Так как занятия по у них проходят в одно и то же время, было решено выделить кабинет для каждого класса
и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход
три натуральных числа: количество учащихся в каждом из трех классов.
"""


def main(a, b, c):
    k = (a + 1) // 2 + (b + 1) // 2 + (c + 1) // 2  # добавляем 1 к делимому числу,чтобы избежать покупки половины парты
    return k


if __name__ == '__main__':
    a = int(input("Students in class A? "))
    b = int(input("Students in class B? "))
    c = int(input("Students in class C? "))
    print(main(a, b, c))
