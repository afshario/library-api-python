import requests
import csv

url = 'https://openlibrary.org/search.json'

# API parameters: search for books with random sorting and limited fields
params = {
      'q': 'book',
      'sort': 'random',
      'fields': 'title,first_publish_year,language,author_name',
      'limit': 50,
}

def main():
      try:
            # Fetch data from OpenLibrary API
            print('fetching data from Openlibrary...')
            response = requests.get(url=url, params=params)
            if response.status_code != 200:
                  raise Exception(f'HTTP error occurred: {response.status_code}')
        
            # Filter books published after 2000
            books = list()
            for book in response.json().get('docs', ''):
                  if int(book.get('first_publish_year', 0)) > 2000:
                        books.append(book)
        
            # Sort filtered books by publication year (ascending)
            sorted_books = sorted(
                  books, 
                  key=lambda x: x.get('first_publish_year', 0)
            )
        
            # Write results to CSV file with selected fields
            with open('result.csv', 'w', newline='', encoding='utf-8') as file:
                  fieldnames = ['title', 'first_publish_year', 'author_name', 'language']
                  writer = csv.DictWriter(file, fieldnames=fieldnames)
                  writer.writeheader()

                  for book in sorted_books:
                        # Prepare row data, converting lists to comma-separated strings
                        row = {
                              'title': book.get('title', ''),
                              'first_publish_year': book.get('first_publish_year', ''),
                              'author_name': ', '.join(book.get('author_name', [])),
                              'language': ', '.join(book.get('language', []))
                        }
                        writer.writerow(row)
            
            print('results have been written successfully')

      except requests.exceptions.ConnectionError as e:
            print('Network connection error')
      except Exception as e:
            print(e)

# Running program
if __name__ == '__main__':
    main()