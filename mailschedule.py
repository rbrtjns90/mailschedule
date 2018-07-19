from datetime import datetime
from datetime import timedelta

class MailSchedule():

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.subscribe_date = datetime.now()
        self.schedule_list = [3,2,3,5,10]
        self.date = timedelta(days=0)
        self.dates = []
    
    def subscribe_date(self):
        return self.subscribe_date
    
    def create_mail_dates(self):
        self.dates = []
        date = self.date
        for delta in self.schedule_list:
            if date == None:
                new_time = timedelta(days=delta)
                date = self.subscribe_date + new_time
            else:
                new_time = timedelta(days=delta)
                date = date + new_time
                self.dates.append(self.subscribe_date + date)
        print(self.dates)

 
    def mail_date(self):
        for date in self.dates:
            print("Mail date set for mail %s" %self.dates)
        
customer1 = MailSchedule("Robert Jones")
print("Subscriber Date %s" %customer1.subscribe_date)
e
customer1.create_mail_dates()