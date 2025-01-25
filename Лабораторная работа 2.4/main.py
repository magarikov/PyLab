

class Device:

    def __init__(self, name, status, is_connected):
        ''' name - имя устройства, status - включен, выключен, is_connected - подключен ли к электросети'''
        if not isinstance(name, str):
            raise TypeError("Name should be string type")
        self.name = name

        if not isinstance(status, str):
            raise TypeError("Status should be string type")
        if (status == "on") or (status == "off"):
            self.status = status
        else:
            raise TypeError('Status should be "on" or "off"')

        if not isinstance(is_connected, bool):
            raise TypeError("is_connected should be bool type")
        self.is_connected = is_connected


    def __str__(self):
        return f'Устройство "{self.name}", состояние: {self.status}, подключено к сети: {self.is_connected}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, status={self.status}, is_connected={self.is_connected})"
    def turn_on(self):
        ''' Включает устройство '''
        if (self.is_connected == True):
            self.status = "on"
            print(f"Устройство {self.name} включено")

    def turn_off(self):
        ''' Выключает устройство '''
        self.status = "off"
        print(f"Устройство {self.name} выключено")

    def plug_in(self):
        ''' Подключает устройство к электросети '''
        self.is_connected = True
        print(f"Устройство {self.name} подключено к сети")

    def plug_out(self):
        ''' Отключает устройство от электросети '''
        self.is_connected = False
        print(f"Устройство {self.name} отключено сети")



class Phone(Device):

    def __init__(self, name, status, is_connected, battery):
        ''' battery - заряд батареи от 0% до 100% '''
        super().__init__(name, status, is_connected)
        if not isinstance(battery, int):
            raise TypeError("Battery should be int type")
        if (0 <= battery <= 100):
            self.battery = battery
        else:
            raise TypeError("Battery should be value from 0 to 100")

    def __str__(self):
        return f'Устройство "{self.name}", состояние: {self.status}, подключено к сети: {self.is_connected}, заряд батареи: {self.battery}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, status={self.status}, is_connected={self.is_connected}, battery={self.battery})"

    def plug_in(self):
        '''
        Подключает устройство к электросети.
        Т.к. у телефона есть батарея, необходимо так-же описать, что
        при подключении к сети она будет заряжаться
        '''
        self.is_connected = True
        print(f"Устройство {self.name} подключено к заряжается")
        self.battery = 100

    def turn_on(self):
        '''
        Необходим отдельный метод, т.к. у телефона есть батарея и он может
        работать даже если не подключен к сети
        '''
        if (self.is_connected == True) or (self.battery > 0):
            self.status = "on"
            print(f"Устройство {self.name} включено")

    def call(self, number):
        ''' Позвонить по номеру number'''
        if self.status == "on":
            print(f"Устройство {self.name} звонит на номер: " + number)
        else:
            print(f"Устройство {self.name} выключено")


class Printer(Device):
    def __init__(self, name, status, is_connected, num_papers):
        ''' num_papers - количество листов бумаги в принтере '''
        super().__init__(name, status, is_connected)
        if not isinstance(num_papers, int):
            raise TypeError("Num_papers should be int type")

        self.num_papers = num_papers

    def __str__(self):
        return f'Устройство "{self.name}", состояние: {self.status}, подключено к сети: {self.is_connected}, количество бумаги: {self.num_papers}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, status={self.status}, is_connected={self.is_connected}, num_papers={self.num_papers})"
    def print_paper(self):
        ''' Печатает лист, если есть бумага'''
        if (self.status == "on"):
            if (self.num_papers > 0):
                print(f"Принтер {self.name} напечатал лист")
                self.num_papers -= 1
            else:
                print(f"В принтере {self.name} нет бумаги, лист не распечатан")
        else:
            print(f"Лист не распечатан. Принтер {self.name} выключен")

    def add_paper(self, num):
        ''' Добавляет кол-во "num" бумаги в принтер'''
        self.num_papers += num
        print(f'В принтер "{self.name}" добавлено ' + str(num) + ' бумаги. Текущее количество бумаги: ' + str(self.num_papers))







phone = Phone("telephone1", "on", True, 80)
print(phone.__str__())
print(phone.__repr__())
phone.turn_off()

print()

printer = Printer("printer1", "off", False, 10)
print(printer.__str__())
print(printer.__repr__())
printer.print_paper()
printer.plug_in()
printer.turn_on()
printer.add_paper(10)
printer.print_paper()