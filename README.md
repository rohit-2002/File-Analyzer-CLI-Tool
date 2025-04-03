# File Analyzer CLI Tool

## 📌 Objective
This is a Python command-line tool that analyzes a text file and provides a summary report, including:
- Total number of words
- Top 5 most frequent words (excluding common stop words)
- Average word length
- Number of sentences

## 🛠️ Requirements
- Python 3.x

## 📥 Installation
No installation is required. Just ensure you have Python 3 installed on your system.

## ▶️ Usage
To run the script, use the following command in your terminal:

```sh
python file_analyzer.py sample.txt
```

## 📝 Features
- Reads a text file and processes its content.
- Removes punctuation (except for sentence end markers like `.`, `?`, `!`).
- Splits text into sentences.
- Counts total words, excluding stop words.
- Displays the top 5 most frequently used words (ignoring common stop words).
- Computes the average word length.
- Counts the total number of sentences.

## 🖥️ Sample Output
```
Summary Report:
Total number of words: 120
Top 5 most frequent words (ignoring common stop words):
  life: 8
  technology: 5
  world: 4
  knowledge: 3
  history: 3
Average word length: 4.85
Number of sentences: 6
```
Enjoy using the **File Analyzer CLI Tool**! 🚀

