import requests
import csv

url = "https://openlibrary.org/search.json"

params = {
      'q':'book',
      'sort':'random',
      'fields':'title,first_publish_year,edition_count,language,author_name',
      'limit':50,
}
      
def main():

      try:
            res = requests.get(url=url,params=params)
            if(res.status_code != 200):
                  raise Exception(f"An error accures, http code : {res.status_code}")
      except requests.exceptions.ConnectionError as e:
            print("Network connection error")
      except Exception as e:
            print(e)

if __name__ == "__main__":
      main()