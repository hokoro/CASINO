import random


class updown:
    def __init__(self):
        self.location = random.randint(1, 9)  # 시작 위치
        self.coin = 3       # 내가 거는 돈
        self.gamebool = True    # 게임의 성공 여부
        self.count = 5      # 부여된 기회
        self.nums = [i for i in range(1, 10)]   # 범위

        self.rates = {      # 배당율
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
            location_index = self.nums.index(self.location)  # 현재 위차
            ups = self.nums[location_index+1:]  # 위치 보다 up 범위의 수
            downs = self.nums[:location_index]  # 위치 보다 down 범위의 수

            choices_nums = downs + ups      # 선택 범위
            print(choices_nums)
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

            if choice == 3:             # 내가 중간에 멈추고 싶을떄
                return self.coin

            next_index = random.randint(0,7)
            next_number = choices_nums[next_index]

            if choice == 1 and self.location < next_number:     # up 성공
                self.coin = int(self.rates[self.location][1] * self.coin)
                self.location = next_number
                self.count -= 1

            elif choice == 2 and self.location > next_number:   # down 성공
                self.coin = int(self.rates[self.location][0] * self.coin)
                self.location = next_number
                self.count -= 1
            else:                   # up down 을 실패 했을떄
                self.gamebool = False
                break

        if not self.gamebool:
            return 0
        else:
            return self.coin