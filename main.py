import re
import pandas as pd

def text_to_csv():
    with open('data.txt', 'r') as file:
        content = file.read()
        date_pattern = r'\d{4}-\d{2}-\d{2}'
        time_pattern = r'\d{2}:\d{2} \w{2}'
        sender_email_pattern = r'From:\s+([\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,})'
        receiver_email_pattern = r'To:\s+([\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,})'
        subject_pattern = r'Subject:\s+(.*)'
        body_pattern = r'Body:\s+([\s\S]*?)(?=\nDate:|\n$)'
        date_result = re.findall(date_pattern, content)
        time_result = re.findall(time_pattern, content)
        sender_email_result = re.findall(sender_email_pattern, content)
        reciever_email_result = re.findall(receiver_email_pattern, content)
        subject_result = re.findall(subject_pattern, content)
        body_result = re.findall(body_pattern, content)
        for text in body_result:
            text = text.strip('\n')
        dict = {'Subject': subject_result, 'Sender Email': sender_email_result, 'Reciever Email': reciever_email_result, 'Date': date_result, 'Time': time_result, 'Body': body_result}
        df = pd.DataFrame(dict)
        df.to_csv('book_store.csv')
        print(df)
text_to_csv()
