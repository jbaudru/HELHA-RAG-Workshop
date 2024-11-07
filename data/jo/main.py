import csv
import os
from collections import defaultdict

# Dictionary to store rows by topic
topics = defaultdict(list)

# Function to sanitize file names
def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name)

# Open the CSV file
with open('paris-2024-faq.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    
    # Iterate over each row in the CSV file
    for row in reader:
        topic = row['topics']
        lang = row['lang']
        if lang == 'en':  # Only process rows in English
            topics[topic].append(row)

# Create a text file for each topic in English
for topic, rows in topics.items():
    sanitized_topic = sanitize_filename(topic)
    with open(f'{sanitized_topic}-en.txt', 'w', encoding='utf-8') as txtfile_en:
        for row in rows:
            txtfile_en.write('; '.join(row.values()) + '\n')