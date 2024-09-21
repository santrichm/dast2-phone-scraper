import requests
from threading import Thread, Lock
from queue import Queue
import time

URL = 'https://dast2.com/api/1.0/category/1?page={}'
HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'dast2.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'X-Requested-With': 'XMLHttpRequest',
}

class PhoneScraper:
    def __init__(self, num_threads=5):
        self.queue = Queue()
        self.lock = Lock()
        self.phones = set()
        self.num_threads = num_threads
        self.is_active = True

    def fetch_phones(self):
        while self.is_active:
            try:
                page = self.queue.get(timeout=5)
            except Queue.Empty:
                continue

            try:
                response = requests.get(URL.format(page), headers=HEADERS)
                response.raise_for_status()
                data = response.json()

                if data['success']:
                    for ad in data['data']['advertises']['data']:
                        phone = ad['owner_mobile']
                        with self.lock:
                            if phone not in self.phones:
                                self.phones.add(phone)
                                print(f"Found new phone: {phone}")
                                self.save_phone(phone)
            except requests.RequestException as e:
                print(f"Error fetching page {page}: {e}")
            finally:
                self.queue.task_done()

    def save_phone(self, phone):
        with open("phones.txt", "a") as f:
            f.write(f"{phone}\n")

    def run(self):
        threads = []
        for _ in range(self.num_threads):
            thread = Thread(target=self.fetch_phones)
            thread.start()
            threads.append(thread)

        page = 1
        try:
            while self.is_active:
                self.queue.put(page)
                page += 1
                time.sleep(0.1)  # Rate limiting
        except KeyboardInterrupt:
            print("Stopping scraper...")
            self.is_active = False

        self.queue.join()
        for thread in threads:
            thread.join()

        print(f"Scraping completed. Found {len(self.phones)} unique phone numbers.")

if __name__ == "__main__":
    scraper = PhoneScraper()
    scraper.run()
