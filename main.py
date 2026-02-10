import requests
import csv

url = "https://openlibrary.org/search.json"

params = {
      'q':'book',
      'sort':'random',
      'fields':'title,first_publish_year,language,author_name',
      'limit':50,
}
      
def main():

      try:
            response = requests.get(url=url,params=params)
            if(response.status_code != 200):
                  raise Exception(f"An error accures, http code : {response.status_code}")
            books = list()
            for book in response.json().get("docs",""):
                  if book.get("first_publish_year",0) > 2000 :
                        books.append(book)
            sorted_books = sorted(
                  books, 
                  key= lambda x: x.get("first_publish_year",0)
            )
            with open('result.csv', 'w', newline='', encoding='utf-8') as file:
                  fieldnames = ['title', 'first_publish_year', 'author_name',"language"]
                  writer = csv.DictWriter(file, fieldnames=fieldnames)
                  writer.writeheader()

                  for book in sorted_books:
                        row = {
                        'title': book.get('title', ''),
                        'first_publish_year': book.get('first_publish_year', ''),
                        'author_name': ', '.join(book.get('author_name', [])),
                        "language": ', '.join(book.get('language', []))
                        }
                        writer.writerow(row)

      except requests.exceptions.ConnectionError as e:
            print("Network connection error")
      except Exception as e:
            print(e)

if __name__ == "__main__":
      main()