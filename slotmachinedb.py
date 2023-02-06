import sqlite3

connect = sqlite3.connect("casino.db")

cursor = connect.cursor()


#cursor.execute("CREATE TABLE SLOTMACHINE_TABLE(money int)")


cursor.execute("INSERT INTO SLOTMACHINE_TABLE VALUES (0)")

connect.commit()