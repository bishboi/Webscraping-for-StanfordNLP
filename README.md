# Webscraping-for-StanfordNLP
This is the web scraping script for StanfordNLP 
Now, you need not download huge stanfordNLP data(around 1.9 GB) for simple tasks like POS tagging and NER

# Installation 
Just run <br/>
 ```bash install/install.sh```<br/>
This will install selenium in your python3 environment and will install geckodriver for accessing firefox through selenium

# How to use 
just add the text you want to process with the name of data.txt in Data Directory
For -CoreNLP<br/>
run code <br/>
```python3 CoreNLP.py```<br/>
Now the Code will store the data in 2d matrix and will print it,
U can use the code as a snippet which store the stanford nlp table in a 2D matrix and will print it.<br/>
For -Parsing<br/>
run code<br/>
```python3 parser.py```<br/>
it will store the parced data in a string and will print it.<br/>

# Requirements 
python 3 and firefox
