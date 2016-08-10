import wikipedia


def print_wikipedia_results(word):
    """
    Searches for pages that match the specified word
    """
    results = wikipedia.search(word)

    for result in results:
        try:
            page = wikipedia.page(result)
        except wikipedia.exceptions.DisambiguationError:
            print('DisambiguationError')
            continue
        except wikipedia.exceptions.PageError:
            print('PageError for result: ' + result)
            continue

        print(page.summary)

if __name__ == '__main__':
    print_wikipedia_results('wombat')