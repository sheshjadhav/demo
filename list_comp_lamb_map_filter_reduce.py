"""

# List Comprehensions
squares = [x**2 for x in range(10)]
print("List comprehensions:",squares)

# Lambda Functions
add = lambda x, y: x + y
print("Lamblda Functions:",add(5, 3))

# Map Function
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print("Map Function:",squared)

# Filter Function
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter Function:",even_numbers)

# Reduce Function
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Reduce Function:",product)
"""
"""
# Regular Expressions
import re
pattern = r"\d+"
result = re.findall(pattern, "There are 2 apples and 3 oranges.")
print("regular expressions:",result)
"""
"""
# Date and Time
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#Enumerate Function
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print("Enumerate Function:",index, fruit)

"""
'''
#Zip Function
names = ["John", "Alice", "Bob"]
ages = [30, 25, 22]
combined = list(zip(names, ages))
print(combined)
'''
'''
#Iterators and Generators
def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
        print("my GeneraTOR:",value)        
'''
"""
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
with MyContext() as context:
    print("Inside the context")        
"""
"""
#Static and Class Methods
class MyClass:
    @staticmethod
    def static_method():
        print("Static method called")
    @classmethod
    def class_method(cls):
        print("Class method called")
MyClass.static_method()
MyClass.class_method()
"""
"""
#  String Methods
text1 = " Hello,  World!                  "
text=text1.strip()
print(text+"i am shesh") # Remove whitespace
"""
"""        
#String Joining
words = ["Hello", "World",'i','am shesh']
sentence = " ".join(words)
print(sentence)

# String Splitting
text = "Hello, World,i am , shesh rao ,jADHAV"
words = text.split(",")
print(words)
"""
"""
#Writing CSV Files
import csv
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["John", 30])
"""
"""
# Using `BeautifulSoup` for Web Scraping
from bs4 import BeautifulSoup
import requests
response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.string)
"""
"""
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()        
"""
"""
# Using `SQLite` for Database Management
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
conn.commit()
conn.close()
"""
'''
def test_add():
    assert add(1,2)==3
'''
'''
import os
print(os.getcwd())

l={'a','b','c','d'}    
l.add('e')
print(l)    
'''