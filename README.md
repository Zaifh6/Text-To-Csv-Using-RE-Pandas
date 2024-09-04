# Text-To-Csv-Using-RE-Pandas

![Complaint form for faculty using](https://github.com/user-attachments/assets/5c5ed706-7f35-4d59-9d64-ba88200afcad)
![image](https://github.com/user-attachments/assets/78ebdbab-54d7-4ee1-997c-39dd30e8377e)
![image](https://github.com/user-attachments/assets/2ab5a8a4-984f-472e-8285-8cae08c3e7da)


## Overview

The `Text-To-Csv-Using-RE-Pandas` script extracts data from a structured text file and converts it into a CSV file using regular expressions and the pandas library. This script is useful for parsing emails or similar structured text data and converting it into a tabular format for further analysis.

## Script Details

The script performs the following tasks:

1. **Read the Text File**: Opens and reads the contents of `data.txt`.
2. **Extract Data Using Regular Expressions**: Utilizes regular expressions to find patterns in the text for:
   - Dates
   - Times
   - Sender Email Addresses
   - Receiver Email Addresses
   - Subject Lines
   - Email Bodies
3. **Clean and Structure Data**: Processes the extracted data and removes unnecessary newline characters from the email body.
4. **Create a DataFrame**: Uses the pandas library to create a DataFrame from the structured data.
5. **Save to CSV**: Writes the DataFrame to a CSV file named `book_store.csv`.

## Dependencies

- **Python 3.x**
- **pandas**: Library for data manipulation and analysis.
- **re**: Python's built-in regular expression library.

## Installation

Ensure you have Python 3.x installed. You can install the required pandas library using pip:

```bash
pip install pandas
pip install re
