
from datetime import datetime as dt
from datetime import timedelta


class Commands:
    comm = ["today", "t", "tomorrow", "tm", "yesterday", "y", "week", "w"]

    @staticmethod
    def is_command(ip):
        if ip in Commands.comm:
            return True
        return False


class Data:
    def __init__(self) -> None:
        date_format = "%d.%m.%Y"
        self.today_date = dt.now().strftime(date_format)
        add_one = dt.now() + timedelta(days=1)
        self.tomorrow_date = add_one.strftime(date_format)
        deduct_one = dt.now() - timedelta(days=1)
        self.yesterday_date = deduct_one.strftime(date_format)
  
    #sample dict. to delete
    root_dict = {
        "30.12.2023": {
            1: {
                "defaultname": [
                    ("Buy groceries", "done"),
                    ("Finish homework", "not done"),
                    ("Go for a run", "not done"),
                    ("Call doc", "done"),
                    ("Clean the house", "not done"),
                ]
            },
            2: {
                "imp-list": [
                    ("asdasd", "not done"),
                    ("234234", "not done"),
                ]
            },
        }
    }



class Week:
    def __init__(self) -> None:
        days_until_next_monday = (7 - dt.now().weekday()) % 7
        self.next_monday = dt.now() + timedelta(days=days_until_next_monday)
        self.next_tuesday = self.next_monday + timedelta(days=1)
        self.next_wednesday = self.next_monday + timedelta(days=2)
        self.next_thursday = self.next_monday + timedelta(days=3)
        self.next_friday = self.next_monday + timedelta(days=4)
        self.next_saturday = self.next_monday + timedelta(days=5)
        self.next_sunday = self.next_monday + timedelta(days=6)

    def get(self):
        print(f"{self.next_monday=}")
        print(f"{self.next_tuesday=}")
        print(f"{self.next_wednesday=}")
        print(f"{self.next_thursday=}")
        print(f"{self.next_friday=}")
        print(f"{self.next_saturday=}")


class Fetch:
    pass


class Process:
    def __init__(self, raw_ip):
        ip = " ".join(
            raw_ip.split()
        ) 
        self.ip = ip
        self.ip_list = self.ip.split()

    def execute(self):
        # today_obj = Today()
        data = Data()

        if any(a_command in self.ip for a_command in Commands.comm):
            print(f"atleast 1 command found. ip is: {self.ip} \n proceeding")

            for word in self.ip_list:
                print(f"processing {word}")
                if Commands.is_command(word):
                    if word in ["t", "today"]:
                        print(data.today_date)
                    elif word in ["tm", "tomorrow"]:
                        print(data.tomorrow_date)
                    elif word in ["y", "yesterday"]:
                        print(data.yesterday_date)
                    elif word in ["w", "week"]:
                        print("weekdates of next week")
                        obj = Week()
                        obj.get()


if __name__ == "__main__":
    print(
        "Welcome to ToDo Terminal. \n\
Here are the rules:\n\
Week starts at Monday.\n\
\n\
Enter 'today'       OR 't'      to see todays todos\n\
Enter 'tomorrow'    OR 'tm'     to see tomorrows todos\n\
Enter 'yesterday'   OR 'y'      to see yesterdays todos\n\
Enter 'week'        OR 'w'      to see current weeks todos\n\
Enter 'week next'   OR 'w +1'   to see the todo of each day in next week\n\
Enter 'week 1' to see the todo of each day in week 1 of this month. \n\
    ('week 2', 'week 3', 'week 4', 'week 5' are valid while, numbers greater than 5 are not valid)\n\
    ('week2' is same as 'week 2' and 'w2')\n\
"
    )
    ip=""
    while (ip!='q'): 
      ip = input("\n>> ")
      Process(ip).execute()
