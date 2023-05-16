import sys
from crawler import LinkCrawler

def get_pages_data():
    raise NotImplementedError()


if __name__ == "__main__":
    switch = sys.argv[1]
    if switch == 'find_links':
        Crawler = LinkCrawler(cities = ['paris' , 'berlin'])
        Crawler.start_crawl()
    elif switch == 'extract_pages':
        get_pages_data()