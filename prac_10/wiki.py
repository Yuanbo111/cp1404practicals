import wikipedia

wikipedia.set_lang("en")

def main():
    while True:
        topic = input("Enter page title (blank to exit): ").strip()
        if topic == "":
            print("Goodbye!")
            break
        try:
            page = wikipedia.page(title=topic, auto_suggest=False)
            summary = wikipedia.summary(page.title, sentences=2)
        except wikipedia.DisambiguationError as e:
            print(f"Ambiguous topic. Options: {e.options[:5]}")
            continue
        except wikipedia.PageError:
            print("Page not found. Try another id.")
            continue


        print("-" * 80)
        print(f"Title: {page.title}")
        print(f"URL: {page.url}")
        print(f"Summary:\n{summary}\n")

main()
