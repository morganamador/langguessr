documentation.md

langguessr is a tool to identify your geographic location based on the text found on signs around you.

3 endpoints:
/hello, GET method to return "Hello World!"

/id_text, POST method to send user’s text and return the user’s likely location

/, GET method to render the HTML form 






Input:
String of text from the user’s environment (typed out or obtained from a photo by way of tools such as Google Lens)

Output
The user’s ranked likely locations, in the form of a JSON list of entries with the form: [country, language, score, note], sorted by score, the score is the fraction of the intersection of the input's characters with that language's character inventory.




requires Python 3.12 and Docker. 

how to use:

clone the repo

create a virtual environment

pip install -r requirements.txt

docker compose up

python app.py

open a browser and go to http://localhost:5000 , and click guess. OR curl.exe -d "user_text=your text here" http://localhost:5000/id_text



curl example below:
```
langguessr> curl.exe -d "user_text=Straße gesperrt" http://localhost:5000/id_text
[["Germany","German",1.0,"\u00df used in standard orthography"],["Austria","German",1.0,"\u00df used in standard orthography"],["Switzerland","German",1.0,"\u00df not used; expect 'Strasse' instead"],["Liechtenstein","German",1.0,"\u00df not used; expect 'Strasse' instead"],["United Kingdom","English",0.875,""],["United States","English",0.875,""],["Canada","English",0.875,""],["Australia","English",0.875,""],["Ireland","English",0.875,""]]
```



Future work:

add more countries’ character data to the database

Divide language data into country specific data, like the ss example with German speaking countries

Implement signclues function and create database of sign clues

Create models of the data as correlated with the longitudinal points of the data

