"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Total phone_no in texts:-

Total_phone_no_texts=[]
for i in range(len(texts)):
    for j in range(2):
        Total_phone_no_texts.append(texts[i][j])
        
# Total phone_no in calls:-

Total_phone_no_calls=[]
for i in range(len(calls)):
    for j in range(2):
        Total_phone_no_calls.append(calls[i][j])
        
# Convert all phone_no into unique set:-

Total_phone_no=Total_phone_no_calls+Total_phone_no_texts
unique_phone_no=set(Total_phone_no)

print("There are",len(unique_phone_no),"different telephone numbers in the records")
