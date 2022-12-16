import csv
from datetime import timezone, date, timedelta
import datetime
import random

def daterange(start_date,end_date):
  for n in range(int((end_date - start_date).days)):
    yield start_date + timedelta(n)


channel_types = input("1. Enter the channel types, VOICE, CHAT or BOTH, default is BOTH: ") or "BOTH"
if channel_types == "BOTH":
  channel_types = "VOICE_CHAT"
queue_name = input("2. Enter the queue name, default is BasicQueue: " ) or "BasicQueue"
queue_id   = input("3. Enter the queue id, default is 5cbc2701-cdd5-44c6-9100-ab0fe856bbe2: ") or "5cbc2701-cdd5-44c6-9100-ab0fe856bbe2"
channel_types_list = channel_types.split("_")
interval_value = input("4. Enter the interval, daily, 30mins or 15mins, default is 15mins: ") or "15mins"
start_year = int(input("5. Enter the start year, default is 2021: ") or "2021")
start_month = int(input("6. Enter the start month, default is 1: ") or "1")
start_day = int(input("7. Enter the start day, default is 1: ") or "1")
start_date = date(start_year,start_month,start_day)
end_year = int(input("8. Enter the end year, default is 2022: ") or "2022")
end_month = int(input("9. Enter the end month, default is 12: ") or "12")
end_day = int(input("10. Enter the end day, default is 30: ") or "30")
end_date = date(end_year,end_month,end_day)

incoming_contact_volumes_voice = input("11. Enter incoming contact volume including abandoned call per interval, default is 100 : ") or "100"
incoming_contact_volumes_chat  = input("12. Enter incoming contact volume including abandoned chat per interval, default is 50  : ") or "50"

incoming_contact_volumes_list = [incoming_contact_volumes_voice,incoming_contact_volumes_chat]

contact_volume_ranges_voice = input("13. How much higher and lower the range you want to be for voice?  if you enter 5, it will generate a number from Incoming Contact Volume-5 to Incoming Contact Volume+5. Default is 5: ") or "5"

contact_volume_ranges_chat = input("14. How much higher and lower the range you want to be for chat?  if you enter 5, it will generate a number from Incoming Contact Volume-5 to Incoming Contact Volume+5. Default is 5: ") or "5"

contact_volume_ranges_list = [contact_volume_ranges_voice,contact_volume_ranges_chat]

avg_handle_times_voice = input("15. Average Handle Time for voice, will add or minus up to 20 seconds, default is 300: " ) or "300"

avg_handle_times_chat = input("16. Average Handle Time for chat, will add or minus up to 20 seconds, default is 500: " ) or "500"

avg_handle_times_list = [avg_handle_times_voice,avg_handle_times_chat]

# contacts_handled = input("Contacts that are handled, minus 1 to 3 contacts:" )

start_times_voice = input("17. Used in 15 or 30 min only, which hour does the day start to take calls in UTC in 24hr format like 13 for 1pm. default is 13: ") or "13"

start_times_chat  = input("18. Used in 15 or 30 min only, which hour does the day start to take chat in UTC in 24hr format like 13 for 1pm. default is 13: ") or "13"

start_times_list = [start_times_voice,start_times_chat]

stop_times_voice = input("19. Used in 15 or 30 min only, which hour does the day stop to take calls in UTC in 24hr format like 23 for 11pm. Default is 23: ") or "23"

stop_times_chat = input("20. Used in 15 or 30 min only, which hour does the day stop to take chat in UTC in 24hr format like 23 for 11pm. Default is 23: ") or "23"

stop_times_list = [stop_times_voice,stop_times_chat]

row_list = [
["QueueName",
 "QueueId",
 "ChannelType",
 "TimeStamp",
 "IntervalDuration",
 "IncomingContactVolume",
 "AverageHandleTime",
 "ContactsHandled"]]

 
def generateForcastingData(channel_type, incoming_contact_volume, contact_volume_range, avg_handle_time, start_time, stop_time):
  for single_date in daterange(start_date, end_date):
    icv = random.randrange(incoming_contact_volume-contact_volume_range,incoming_contact_volume+contact_volume_range)
    aht = random.randrange(avg_handle_time-20 , avg_handle_time+20 )
    ch = icv - 1
    if interval_value == 'daily':
      row_list.insert(len(row_list), [queue_name,queue_id,channel_type,single_date.strftime("%Y-%m-%dT00:00:00Z"),interval_value,icv,aht,ch])
    elif interval_value == '15mins':
      for hours in range (0,start_time,1):
        for minutes in range(0,60,15):
          icv = 0
          aht = 0
          ch = 0
          timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
          row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
      for hours in range (start_time,stop_time,1):
        for minutes in range(0,60,15):
          icv = random.randrange(incoming_contact_volume-contact_volume_range,incoming_contact_volume+contact_volume_range)
          aht = random.randrange(avg_handle_time-20 , avg_handle_time+20 )
          ch = icv -1
          timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
          row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
      for hours in range (stop_time,24,1):
        for minutes in range(0,60,15):
          icv = 0
          aht = 0
          ch = 0
          timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
          row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
    elif interval_value == '30mins':
      for hours in range (0,start_time,1):
        for minutes in range(0,60,30):
          icv = 0
          aht = 0
          ch = 0
          timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
          row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
      for hours in range (start_time,stop_time,1):
        for minutes in range(0,60,30):
          icv = random.randrange(incoming_contact_volume-contact_volume_range,incoming_contact_volume+contact_volume_range)
          aht = random.randrange(avg_handle_time-20 , avg_handle_time+20 )
          ch = icv - 1
          timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
          row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])
      for hours in range (stop_time,24,1):
        for minutes in range(0,60,30):
          icv = 0
          aht = 0
          ch = 0
          timestamp = single_date.strftime("%Y-%m-%dT")+f"{hours:02}"+":"+f"{minutes:02}"+":"+"00Z"
          row_list.insert(len(row_list), [queue_name,queue_id,channel_type,timestamp,interval_value,icv,aht,ch])

i=0
for channel_type in channel_types_list:
  incoming_contact_volume = int(incoming_contact_volumes_list[i])
  contact_volume_range = int(contact_volume_ranges_list[i])
  avg_handle_time = int(avg_handle_times_list[i])
  start_time = int(start_times_list[i])
  stop_time = int(stop_times_list[i])
  generateForcastingData(channel_type, incoming_contact_volume, contact_volume_range, avg_handle_time, start_time, stop_time)
  i = i + 1

with open (queue_name+'-'+interval_value+'-'+channel_types + '-'+ datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') +'.csv','w',newline='') as file:
  writer = csv.writer(file)
  writer.writerows(row_list)
