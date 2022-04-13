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
interval_value = input("Enter the interval daily 30mins 15mins:")
start_year = input("Enter the start year:")
start_month = input("Enter the start month:")
start_day = input("Enter the start day:")
start_date = date(int(start_year),int(start_month),int(start_day))
end_year = input("Enter the end year:")
end_month = input("Enter the end month:")
end_day = input("Enter the end day:")
end_date = date(int(end_year),int(end_month),int(end_day))
incoming_contact_volume = input("Enter incoming contact volume including abandoned call, plus or minus 5 to 10 contacts:")
avg_handle_time = input("Average Handle Time, will add or minus up to 20 seconds:")
# contacts_handled = input("Contacts that are handled, minus 3 to 5 contacts:")


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
  icv = random.randrange(int(incoming_contact_volume)-5,int(incoming_contact_volume)+5)
  aht = random.randrange( int(avg_handle_time)-20 , int(avg_handle_time)+20 )
  ch = icv - random.randrange(3,5)
  if interval_value == 'daily':
    row_list.insert(len(row_list), [queue_name,queue_id,channel_type,single_date.strftime("%Y-%m-%dT00:00:00Z"),interval_value,icv,aht,ch])
  elif interval_value == '15mins':
    for hours in range (23):
      for minutes in range(0,60,15):
        icv = random.randrange(int(incoming_contact_volume)-5,int(incoming_contact_volume)+5)
        aht = random.randrange( int(avg_handle_time)-20 , int(avg_handle_time)+20 )
        ch = icv - random.randrange(3,5)
        timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
        row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
  elif interval_value == '30mins':
    for hours in range (23):
      for minutes in range(0,60,30):
        icv = random.randrange(int(incoming_contact_volume)-5,int(incoming_contact_volume)+5)
        aht = random.randrange( int(avg_handle_time)-20 , int(avg_handle_time)+20 )
        ch = icv - random.randrange(3,5)
        timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
        row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
	

with open (queue_name+'-'+interval_value+'.csv','w',newline='') as file:
  writer = csv.writer(file)
  writer.writerows(row_list)