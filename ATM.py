from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def enter_amount(self):
        pass


class SBI(ATM):
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('Withdrawal successfully completed.')
        else:
            print('Insufficient Balance.')

    def deposit(self, amount):
        self.balance += amount
        print('Deposit successfully completed.')

    def check_balance(self):
        print(f'Your current balance is: {self.balance}')
        return self.balance

    def enter_pin(self):
        pin = int(input("Enter your PIN: "))
        if self.pin == pin:
            return True
        else:
            print("Invalid PIN")
            return False

    def enter_amount(self):
        return int(input('Enter amount: '))

    def portal(self):
        while True:
            print('''
                1. Withdraw
                2. Deposit
                3. Check Balance 
                4. Exit            
            ''')
            ch = input('Enter Your Choice: ')

            if ch == '1':
                if self.enter_pin():
                    amount = self.enter_amount()
                    self.withdraw(amount)

            elif ch == '2':
                if self.enter_pin():
                    amount = self.enter_amount()
                    self.deposit(amount)

            elif ch == '3':
                self.check_balance()

            elif ch == '4':
                print("Thank you for using SBI ATM.")
                break

            else:
                print("Invalid choice, please try again.")

s = SBI(5000, 1234)
s.portal()
