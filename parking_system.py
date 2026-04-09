import datetime
import random
import math


class ParkingSystem:
    def __init__(self):
        self.tickets = {}
        
        self.hourly_rate = 100

    def generate_ticket_id(self):
        return str(random.randint(100000, 999999))

    def issue_ticket(self):
        car_number = input("Введите номер машины: ").strip()
        
        if not car_number or " " in car_number:
            print("\nОшибка: Неверный формат номера машины. Пожалуйста, введите номер в правильном формате.\n")
            return

        ticket_id = self.generate_ticket_id()
        entry_time = datetime.datetime.now()

        self.tickets[ticket_id] = {
            "car_number": car_number,
            "entry_time": entry_time,
            "paid": False
        }

        print(f"\nТалон выдан:")
        print(f"Номер талона: {ticket_id}")
        print(f"Номер машины: {car_number}")
        print(f"Время выдачи: {entry_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    def return_ticket(self):
        ticket_id = input("Введите номер талона: ").strip()

        if ticket_id not in self.tickets:
            print(f"\nОшибка: Талон с номером {ticket_id} не найден. Пожалуйста, проверьте номер и попробуйте снова.\n")
            return

        ticket = self.tickets[ticket_id]
        if ticket["paid"]:
            print(f"\nОшибка: Талон с номером {ticket_id} уже оплачен. Везд был ранее оплачен.\n")
            return

        exit_time = datetime.datetime.now()
        duration = exit_time - ticket["entry_time"]
        total_seconds = duration.total_seconds()

        
        billable_hours = math.ceil(total_seconds / 3600)

        
        if total_seconds < 60:
            time_str = f"{int(total_seconds)} сек. (округлено до 1 часа)"
        elif total_seconds < 3600:
            time_str = f"{int(total_seconds // 60)} мин. (округлено до 1 часа)"
        else:
            time_str = f"{billable_hours} час(а)"

        cost = billable_hours * self.hourly_rate

        print(f"\nСчет к оплате:")
        print(f"Номер талона: {ticket_id}")
        print(f"Номер машины: {ticket['car_number']}")
        print(f"Время въезда: {ticket['entry_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Время выезда: {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Продолжительность парковки: {time_str}")
        print(f"Стоимость парковки: {cost} сом\n")

        ticket["paid"] = True

    def main_menu(self):
        while True:
            print("Выберите действие:")
            print("1. Выдача талона")
            print("2. Сдача талона")
            choice = input("Ваш выбор: ")

            if choice == "1":
                self.issue_ticket()
            elif choice == "2":
                self.return_ticket()
            else:
                print("Неверный выбор, попробуйте снова.\n")


if __name__ == "__main__":
    parking = ParkingSystem()
    parking.main_menu()
