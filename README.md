# SentimentBenchmark: Advanced NLP Sentiment Analysis Tool
Overview
SentimentBenchmark is a simple sentiment analysis tool designed for comparison of Natural Language Processing (NLP) and Large Language Models (LLMs) performance. This tool is specifically tailored to process Excel files, applying a range of sentiment analysis techniques to text data. It might be helpful for researchers, data analysts, and anyone interested in gaining deeper insights into textual sentiment.

# Key Features
Input: In current version accepts Excel files focusing on the most popular data storage format in research and business.
Configurable Column Analysis: Users can specify the column name containing text for analysis, under column_name parameter.
Multiple Analysis Methods: Includes six sentiment analysis methodologies, described below. 
Output Convenience: Outputs an Excel file with  sentiment analysis for each entry, facilitating further data manipulation and visualization.

# Sentiment Analysis Methodologies
The tool employs the following diverse and robust methods for sentiment analysis:

1. NLTK with Vader Lexicon: Utilizes the Natural Language Toolkit (NLTK) configured with the Vader lexicon, often used in media sentiment analysis.
2. TextBlob: A simple yet powerful library for processing textual data, providing a straightforward approach to sentiment analysis.
3. ChatGPT 3.5-Turbo (Default Configuration): Leverages OpenAI's GPT-3.5-Turbo model in its default setting.
4. ChatGPT 3.5-Turbo (Custom Configuration): Employs GPT-3.5-Turbo with adjusted parameters (temperature=0.3, top_p=0.8, max_tokens=32) for more controlled output.
5. ChatGPT 4 (Default Configuration): Integrates the advanced capabilities of OpenAI's GPT-4 for state-of-the-art sentiment analysis.
6. ChatGPT 4-Turbo (Custom Configuration): Utilizes GPT-4-Turbo with fine-tuned settings (temperature=0.3, top_p=0.8, max_tokens=32) for more controlled output.

# Getting Started
To use SentimentBenchmark, follow these steps:

Prepare Your Data: Ensure your data is in an Excel format with the text for analysis in a one column. 
Configure the Tool: Set the excel filename, as well as column and sheet name parameter in the code to match your data structure.
Run the Analysis: Execute the tool to perform sentiment analysis. 
Review the Results: Analyze the output Excel file, which will include detailed sentiment assessments for each entry.

# Contributions and Feedback
Welcome contributions and feedback to improve SentimentBenchmark. If you have suggestions, issues, or would like to contribute to the project, please feel free to open an issue or submit a pull request.

# License
This project is licensed under MIT License, allowing for wide-ranging use and modification within the bounds of the license.
