class Szy:
    def __init__(self, number: str):
        self.number = number

    def zxc(self):
        number = str(self.number)
        for i in range(len(self.number)//2):
            if self.number[i] != self.number[len(number)-1-i]:
                return False
            else:
                return True

    def __str__(self):
        return f"Number: {self.number}\n"

num = Szy(number="232")
print(num)
print(num.zxc())