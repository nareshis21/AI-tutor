import pdfquery

def search_pdf(pdf_file, query):
  results = pdfquery.pdfquery_search(pdf_file, query)
  return results

def main():
  pdf_file = "Hands on machine learning.pdf"
  query = "logistic regression"
  results = search_pdf(pdf_file, query)
  print(results)

if __name__ == "__main__":
  main()
