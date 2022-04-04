import csv
from datetime import timezone, date, timedelta
import datetime

def daterange(start_date,end_date):
  for n in range(int((end_date - start_date).days)):
    yield start_date + timedelta(n)

queue_name = input("Enter the queue name:")
queue_id   = input("Enter the queue id:")
channel_type = input("Enter the channel type VOICE or CHAT:")
interval_value = input("Enter the interval daily 30mins 15mins:")
start_year = input("Enter the start year:")
start_month = input("Enter the start month:")
start_day = input("Enter the start day:")
start_date = date(int(start_year),int(start_month),int(start_day))
end_year = input("Enter the end year:")
end_month = input("Enter the end month:")
end_day = input("Enter the end day:")
end_date = date(int(end_year),int(end_month),int(end_day))


row_list = [
["QueueName",
 "QueueId",
 "ChannelType",
 "TimeStamp",
 "IntervalDuration",
 "IncomingContactVolume",
 "AverageHandleTime",
 "ContactsHandled"]]

for single_date in daterange(start_date, end_date):
  row_list.insert(len(row_list), [queue_name,queue_id,channel_type,single_date.strftime("%Y-%m-%dT00:00:00Z"),interval_value,"50","27","645"])

with open ('test.csv','w',newline='') as file:
  writer = csv.writer(file)
  writer.writerows(row_list)
