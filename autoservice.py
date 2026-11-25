# Класс клиента
class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


# Класс автомобиля
class Car:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number


# Класс выполненной работы
class Work:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")

        self.name = name
        self.price = price


# Класс заказа автосервиса
class ServiceOrder:
    def __init__(self, client, car):
        self.client = client
        self.car = car
        self.works = []

    # Добавление работы в заказ
    def add_work(self, work):
        self.works.append(work)

    # Расчёт общей стоимости
    def calculate_total(self):
        return sum(work.price for work in self.works)

    # Вывод информации о заказе
    def show_info(self):
        print("Клиент:", self.client.name)
        print("Телефон:", self.client.phone)
        print("Автомобиль:", self.car.brand, self.car.model)
        print("Номер автомобиля:", self.car.number)

        print("Выполненные работы:")
        for work in self.works:
            print(work.name, "-", work.price, "руб.")

        print("Итоговая стоимость:",
              self.calculate_total(), "руб.")


# Создание клиента и автомобиля
client = Client("Иван Иванов", "89991234567")
car = Car("Toyota", "Camry", "А123ВС")

# Создание заказа
order = ServiceOrder(client, car)

# Добавление работ
order.add_work(Work("Замена масла", 2500))
order.add_work(Work("Замена фильтра", 800))
order.add_work(Work("Диагностика", 1500))

# Вывод информации
order.show_info()