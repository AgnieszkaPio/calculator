print("hello")

class Button:




    class Calculator:
    def __init__(self):
        self.memory = None
        # Podpowiedz: użyj atrybutu do przechowywania wyniku
        # ostatniej wykonanej operacji, tak by metoda memorize przypisywała
        # wynik zapisany w tym atrybucie
        self._short_memory = None

    def add(self, arg1, arg2):
        my_sum = arg1 + arg2
        print(my_sum)
        raise NotImplementedError

    def sub(self, arg1, arg2):
        raise NotImplementedError

    def mul(self, arg1, arg2):
        raise NotImplementedError

    def div(self, arg1, arg2):
        raise NotImplementedError

    def memorize(self):
        """Zapamiętuje wynik ostatniego działania wartość."""
        raise NotImplementedError

    def clean_memory(self):
        """Usuwa zapamietaną wartość."""
        raise NotImplementedError

    def in_memory(self):
        """Wyświetla zapamietaną wartość."""
        print(f"Zapamiętana wartość: {self._memory}")