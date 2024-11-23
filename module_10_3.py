import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(0, 100):
            sum_dep = random.randint(50, 500)
            self.balance += sum_dep
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {sum_dep}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(0, 100):
            sum_take = random.randint(50, 500)
            print(f'Запрос на {sum_take}')
            if sum_take <= self.balance:
                self.balance -= sum_take
                print(f'Снятие: {sum_take}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')