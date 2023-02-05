import random


class updown:
    def __init__(self):
        self.location = random.randint(1, 9)
        self.coin = 3
        self.gamebool = True
        self.count = 5
        self.nums = [i for i in range(1, 10)]

        self.rates = {
            1: [8, 1.2],
            2: [6, 1.4],
            3: [4, 1.6],
            4: [3, 1.8],
            5: [2, 2],
            6: [1.8, 3],
            7: [1.6, 4],
            8: [1.4, 6],
            9: [1.2, 8]
        }

    def main_function(self):
        while self.count != 0:
            location_index = self.nums.index(self.location)
            ups = self.nums[location_index+1:]
            downs = self.nums[:location_index]

            choices_nums = downs + ups
            print('--------------------------------------------------------------------')
            print(f'현재 코인은 : {self.coin} 이고 현재 위치는 {self.location} 입니다 ')
            print('--------------------------------------------------------------------')

            print('업 다운 번호 ')
            for num in self.nums:
                print(f'{num}', end=' ')
            print('\n')
            print(f'다운 성공시 {int(self.rates[self.location][0] * self.coin)} // 업 성공시 {int(self.rates[self.location][1] * self.coin)}  ')
            print(f'업 : 1 // 다운 : 2 // 스톱 : 3')

            choice = int(input())

            if choice == 3:
                return self.coin

            next_index = random.randint(0,7)
            next_number = choices_nums[next_index]

            if choice == 1 and self.location < next_number:
                self.coin = int(self.rates[self.location][1] * self.coin)
                self.location = next_number
                self.count -= 1

            elif choice == 2 and self.location > next_number:
                self.coin = int(self.rates[self.location][0] * self.coin)
                self.location = next_number
                self.count -= 1
            else:
                self.gamebool = False
                break

        if not self.gamebool:
            return 0
        else:
            return self.coin