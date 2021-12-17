from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor, as_completed


def add_wiki_links():
    wiki = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    res = open('results.txt', 'w+', encoding='utf8')
    for _ in tqdm(range(100)):
        html_code = urlopen(wiki).read().decode('utf8')
        soup = BeautifulSoup(html_code, 'html.parser')
        links_tags = soup.find_all('a')

        for link in links_tags:
            href = link.get('href')
            if href and href.startswith('http') and 'wiki' not in href:
                print(href, file=res)


def concurrent_check_links():
    count_workers = int(input('Set count workers: '))
    with ThreadPoolExecutor(max_workers=count_workers) as executor:
        links = open('results.txt', encoding='utf8').read().split('\n')
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 10): url for url in links}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')
            else:
                print(f'{url} page is {len(data)} bytes')
        print('\nVerification completed')


def load_url(url, timeout):
    with urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    add_wiki_links()
    concurrent_check_links()


if __name__ == '__main__':
    main()