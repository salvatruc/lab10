import pytest
from autoservice import Client, Car, Work, ServiceOrder


# 1. Проверка создания клиента
def test_client():
    client = Client("Иван", "89991234567")
    assert client.name == "Иван"


# 2. Проверка телефона клиента
def test_client_phone():
    client = Client("Иван", "89991234567")
    assert client.phone == "89991234567"


# 3. Проверка создания автомобиля
def test_car():
    car = Car("Toyota", "Camry", "А123ВС")
    assert car.brand == "Toyota"


# 4. Проверка модели автомобиля
def test_car_model():
    car = Car("Toyota", "Camry", "А123ВС")
    assert car.model == "Camry"


# 5. Проверка создания работы
def test_work():
    work = Work("Замена масла", 2500)
    assert work.name == "Замена масла"


# 6. Проверка стоимости работы
def test_work_price():
    work = Work("Диагностика", 1500)
    assert work.price == 1500


# 7. Проверка отрицательной цены
def test_negative_price():
    with pytest.raises(ValueError):
        Work("Ремонт", -100)


# 8. Проверка добавления работы
def test_add_work():
    client = Client("Иван", "89991234567")
    car = Car("Toyota", "Camry", "А123ВС")
    order = ServiceOrder(client, car)

    order.add_work(Work("Замена масла", 2500))

    assert len(order.works) == 1


# 9. Проверка расчёта одной работы
def test_calculate_one_work():
    client = Client("Иван", "89991234567")
    car = Car("Toyota", "Camry", "А123ВС")
    order = ServiceOrder(client, car)

    order.add_work(Work("Диагностика", 1500))

    assert order.calculate_total() == 1500


# 10. Проверка общей стоимости нескольких работ
def test_calculate_total():
    client = Client("Иван", "89991234567")
    car = Car("Toyota", "Camry", "А123ВС")
    order = ServiceOrder(client, car)

    order.add_work(Work("Замена масла", 2500))
    order.add_work(Work("Замена фильтра", 800))
    order.add_work(Work("Диагностика", 1500))

    assert order.calculate_total() == 4800


# 11. Проверка пустого заказа
def test_empty_order():
    client = Client("Иван", "89991234567")
    car = Car("Toyota", "Camry", "А123ВС")
    order = ServiceOrder(client, car)

    assert order.calculate_total() == 0