from web_search import search_teb, get_page_text

question = input("Enter your question: ")

results = search_teb(question)

for result in results[:3]:

    print("\nURL: ", result["href"])

    page_text = get_page_text(result["href"])

    print(page_text[:3000])
   