import os
import urllib.request

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def downloader(url):
    """
    Downloads the specified URL and saves it to disk
    """
    req = urllib.request.urlopen(url)
    filename = os.path.basename(url)
    ext = os.path.splitext(url)[1]
    if not ext:
        raise RuntimeError('URL does not contain an extension')

    with open(filename, 'wb') as file_handle:
        while True:
            chunk = req.read(1024)
            if not chunk:
                break
            file_handle.write(chunk)
    msg = 'Finished downloading {filename}'.format(filename=filename)
    return msg


def main(urls):
    """
    Create a thread pool and download specified urls
    """
    with ThreadPoolExecutor(max_workers=5) as executor:
        return executor.map(downloader, urls, timeout=60)

if __name__ == '__main__':
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    results = main(urls)
    for result in results:
        print(result)