import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

URL = "http://quotes.toscrape.com/"

def scrape_first_page(url=URL):
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    quote_blocks = soup.select(".quote")  # each quote block
    quotes = []
    for q in quote_blocks:
        text = q.select_one(".text").get_text(strip=True)
        author = q.select_one(".author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in q.select(".tags a.tag")]
        quotes.append({"text": text, "author": author, "tags": tags})
    return quotes

def analyze(quotes):
    total_quotes = len(quotes)
    authors = [q["author"] for q in quotes]
    unique_authors = set(authors)
    author_counts = Counter(authors)
    top_author, top_count = author_counts.most_common(1)[0]

    # count quotes that contain word "is" (case-insensitive) as a standalone word
    is_pattern = re.compile(r"\bis\b", flags=re.IGNORECASE)
    quotes_with_is = sum(1 for q in quotes if is_pattern.search(q["text"]))

    # tags frequency
    all_tags = [tag for q in quotes for tag in q["tags"]]
    tag_counts = Counter(all_tags)

    return {
        "total_quotes": total_quotes,
        "unique_authors_count": len(unique_authors),
        "unique_authors": sorted(unique_authors),
        "top_author": (top_author, top_count),
        "quotes_with_is": quotes_with_is,
        "tag_counts": tag_counts,
        "author_counts": author_counts
    }

def pretty_print(result):
    print(f"Total quotes: {result['total_quotes']}")
    print(f"Unique authors: {result['unique_authors_count']}")
    print("Authors:", ", ".join(result["unique_authors"]))
    print(f"Top author: {result['top_author'][0]} ({result['top_author'][1]} quotes)")
    print(f"Quotes containing the word 'is' (case-insensitive): {result['quotes_with_is']}")
    print("\nTag counts:")
    for tag, cnt in result['tag_counts'].most_common():
        print(f" - {tag}: {cnt}")

if __name__ == "__main__":
    quotes = scrape_first_page()
    res = analyze(quotes)
    pretty_print(res)
