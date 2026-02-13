# Book Data Fetcher 📝 
A Python script that fetches book data from the OpenLibrary API, filters books published after the year 2000, sorts them by publication year, and exports the results to a CSV file.


## Features  
- Fetches random book data from OpenLibrary API
- Sorts books by publication year (ascending order) 
- Exports data to CSV format with proper encoding
- Handles network errors gracefull

## Run Locally  

Clone the project  

~~~bash  
git clone https://github.com/afshario/library-api-python.git
~~~

Install dependencies  

~~~bash  
pip install -r requirements.txt
~~~

Run the project 
~~~bash  
python main.py
~~~

## Output 
Creates `result.csv` with columns:
- `title`: Book title
- `first_publish_year`: Publication year
- `author_name`: Author(s)
- `language`: Language(s)


## License  
[MIT](https://choosealicense.com/licenses/mit/)  
