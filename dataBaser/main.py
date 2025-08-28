from databaser import DataBase
import time

while True:
    DataBase.create("db.json", [])

    data = DataBase.get("db.json")

    # print(data)

    for _ in range(1, 10+1):
        data.append(
            {
                "id": len(data)+1
            } 
        )

    # print(data)

    DataBase.load("db.json", data, indent=8)
    time.sleep(1)
