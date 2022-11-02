import csv
from datetime import timezone, date, timedelta
import datetime
import random

def daterange(start_date,end_date):
  for n in range(int((end_date - start_date).days)):
    yield start_date + timedelta(n)

queue_name = input("Enter the queue name:")
queue_id   = input("Enter the queue id:")
channel_type = input("Enter the channel type VOICE or CHAT:")
interval_value = input("Enter the interval, daily, 30mins or 15mins:")
start_year = int(input("Enter the start year:"))
start_month = int(input("Enter the start month:"))
start_day = int(input("Enter the start day:"))
start_date = date(start_year,start_month,start_day)
end_year = int(input("Enter the end year:"))
end_month = int(input("Enter the end month:"))
end_day = int(input("Enter the end day:"))
end_date = date(end_year,end_month,end_day)
incoming_contact_volume = int(input("Enter incoming contact volume including abandoned call:"))
contact_volume_range = int(input("How much higher and lower the range you wanna be?  if you enter 5, it will generate a number from Incoming Contact Volume-5 to Incoming Contact Volume+5:"))
avg_handle_time = int(input("Average Handle Time, will add or minus up to 20 seconds:"))
# contacts_handled = input("Contacts that are handled, minus 3 to 5 contacts:")
start_time = int(input("Used in 15 or 30 min only, which hour does the day start to take calls in UTC in 24hr format like 13 for 1pm:"))
stop_time = int(input("Used in 15 or 30 min only, which hour does the day stop to take calls in UTC in 24hr format like 21 for 9pm:"))


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
  icv = random.randrange(incoming_contact_volume-contact_volume_range,incoming_contact_volume+contact_volume_range)
  aht = random.randrange(avg_handle_time-20 , avg_handle_time+20 )
  ch = icv
  if interval_value == 'daily':
    row_list.insert(len(row_list), [queue_name,queue_id,channel_type,single_date.strftime("%Y-%m-%dT00:00:00Z"),interval_value,icv,aht,ch])
  elif interval_value == '15mins':
    for hours in range (0,start_time,1):
      for minutes in range(0,60,15):
        icv = 0
        aht = 0
        ch = icv
        timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
        row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
    for hours in range (start_time,stop_time,1):
      for minutes in range(0,60,15):
        icv = random.randrange(incoming_contact_volume-contact_volume_range,incoming_contact_volume+contact_volume_range)
        aht = random.randrange(avg_handle_time-20 , avg_handle_time+20 )
        ch = icv
        timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
        row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
    for hours in range (stop_time,24,1):
      for minutes in range(0,60,15):
        icv = 0
        aht = 0
        ch = icv
        timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
        row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
  elif interval_value == '30mins':
    for hours in range (0,start_time,1):
      for minutes in range(0,60,30):
        icv = 0
        aht = 0
        ch = icv
        timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
        row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
    for hours in range (start_time,stop_time,1):
      for minutes in range(0,60,30):
        icv = random.randrange(incoming_contact_volume-contact_volume_range,incoming_contact_volume+contact_volume_range)
        aht = random.randrange(avg_handle_time-20 , avg_handle_time+20 )
        ch = icv
        timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
        row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
    for hours in range (stop_time,24,1):
      for minutes in range(0,60,30):
        icv = 0
        aht = 0
        ch = icv
        timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
        row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
	

with open (queue_name+'-'+interval_value+'-'+channel_type+'.csv','w',newline='') as file:
  writer = csv.writer(file)
  writer.writerows(row_list)
