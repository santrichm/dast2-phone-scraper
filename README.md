# Dast2 Phone Scraper

## Features
- Multi-threaded scraping for improved performance
- Real-time saving of unique phone numbers
- Automatic pagination handling
- Graceful shutdown on keyboard interrupt

## Installation

### Requirements
- Python 3.6+
- requests library

### Steps
1. Clone this repository:
   ```
   git clone https://github.com/santrichm/dast2-phone-scraper.git
   cd dast2-phone-scraper
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script with Python:
```
python dast2_scraper.py
```

The script will start scraping phone numbers and save them to `phones.txt` in the same directory. Press Ctrl+C to stop the scraper gracefully.

## Customization
You can adjust the number of threads by modifying the `num_threads` parameter when initializing the `PhoneScraper` class.

## Note
Please ensure you have the right to scrape data from Dast2.com and that you comply with their terms of service and robots.txt file. Use this script responsibly and ethically.

## License
This project is open-source and available under the MIT License.

## Disclaimer
This tool is for educational purposes only. The user assumes all responsibility for the use of this script and must ensure they have permission to scrape the target website.
