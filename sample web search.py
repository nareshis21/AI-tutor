import requests

def get_web_data(url):
  """Gets data from a web URL."""
  response = requests.get(url)
  if response.status_code == 200:
    return response.text
  else:
    return None

def search_web(query):
  """Searches the web for the given query."""
  url = "https://www.google.com/search?q=" + query
  data = get_web_data(url)
  if data is not None:
    return data
  else:
    return "No results found."

def main():
  query = input("What would you like to search for? ")
  data = search_web(query)
  print(data)

if __name__ == "__main__":
  main()
