import random
import sqlite3


class slotmachine:
    def __init__(self):
        self.coin = 3  # 제출한 금액
        self.connect = sqlite3.connect('casino.db')
        self.cursor = self.connect.cursor()
        self.items = {
            1: '자수정',
            2: '사과',
            3: '철주괴',
            4: '금주괴',
            5: '금로나',
            6: '다이아주괴',
            7: '다이아로나',
        }

    def main_function(self):
        # 현재 상금의 수를 가져오기 위해 DB 에서 조회
        self.cursor.execute("SELECT * FROM SLOTMACHINE_TABLE")
        present_money = self.cursor.fetchone()  # 누적 상금 + 내가 게임 을 시작하고 투자한 금액

        slot = []

        for _ in range(3):
            slot.append(random.randint(1, 7))

        if slot[0] == slot[1] == slot[2] and slot[0] == self.items[7]:
            self.cursor.execute("UPDATE SLOTMACHINE_TABLE SET money=? WHERE money=?", (0, present_money))
            return present_money + self.coin
        elif slot[0] == slot[1] == slot[2] and slot[0] == self.items[6]:
            self.cursor.execute("UPDATE SLOTMACHINE_TABLE SET money=? WHERE money=?",
                                (int(present_money // 2), present_money))
            return int(present_money // 2 + self.coin)
        elif slot[0] == slot[1] == slot[2] and slot[0] == self.items[5]:
            self.cursor.execute("UPDATE SLOTMACHINE_TABLE SET money=? WHERE money=?", (
                int(present_money % 3), present_money))
            return int(present_money // 3 + self.coin)
        else:
            return 0


a = slotmachine()

print(a.main_function())
