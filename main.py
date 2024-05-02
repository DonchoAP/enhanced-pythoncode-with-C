import re
import subprocess




def extract_words_from_text(text):
    # Using a regular expression to extract only words from the text
    words = re.findall(r'\b\w+\b', text)
    return words

def save_words_to_txt(words, filename):
    # Saving words to a text file
    with open(filename, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

def scrape_and_save_words(url, output_filename):
    # Scrape text using a C program
    subprocess.run(["./scrape_text", url, output_filename])

# URL of the webpage you want to scrape
url = 'https://buchkodex.de/blog/verben/'
# Name of the text file where the words will be saved
output_filename = 'extracted_words_german.txt'

# Calling the function to scrape and save the words
scrape_and_save_words(url, output_filename)


#Mojo Enhancements to List, Dict, and Tuple
"""
from python import Python
from testing import assert_true
np = Python.import_module("numpy")
plt = Python.import_module("matplotlib.pyplot")

# Define Rosenbrock function
def rosenbrock(x: Float64, y: Float64) -> Float64:
    return (1 - x)**2 + 100 * (y - x**2)**2

def rosenbrock_gradient(x: Float64, y: Float64) -> Tuple[Float64, Float64]:
    dx = -2 * (1 - x) - 400 * x * (y - x**2)
    dy = 200 * (y - x**2)
    return (dx, dy)  # Return as a tuple 
    
from python import Python
from testing import assert_true
np = Python.import_module("numpy")
plt = Python.import_module("matplotlib.pyplot")

# Define Rosenbrock function
def rosenbrock(x: Float64, y: Float64) -> Float64:
    return (1 - x)**2 + 100 * (y - x**2)**2

def rosenbrock_gradient(x: Float64, y: Float64) -> Tuple[Float64, Float64]:
    dx = -2 * (1 - x) - 400 * x * (y - x**2)
    dy = 200 * (y - x**2)
    return (dx, dy)  # Return as a tuple """
