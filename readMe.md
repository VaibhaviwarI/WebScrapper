# Book Catalog Scraper – VuduCom Tech Intern Assignment

## 1. Project Overview


The objective is to scrape book information from the publicly available website [Books to Scrape](https://books.toscrape.com/), specifically from its **Travel category**, and store the extracted information in a CSV file.

## 2. Task Requirements

The scraper extracts the following information for every book:

- **Title:** Name of the book.
- **Price:** Listed price of the book.
- **Star Rating:** Rating given to the book.
- **Availability:** Stock availability status.
- **Description:** Full description extracted from the individual book detail page.

Additional requirements:
- Handle pagination.
- Implement basic error handling.
- Export the scraped data into `books.csv`.

## 3. Project Structure

| File | Description |
|---|---|
| `scrapper.py` | Main scraper containing the complete implementation. |
| `scrapperWholesite.py` | Supporting script created to extract website HTML for inspection and testing purposes. |
| `source.html` | Contains the extracted HTML of the Travel category section. |
| `souce2.html` | Contains the extracted HTML of the complete books website, used for testing purposes. |
| `books.csv` | CSV file containing the extracted book information. |
| `requirements.txt` | Lists the external Python dependencies required by the project. |

**Note:** `scrapper.py` is the main executable file. The supporting scraper and HTML files were created for understanding and testing the website structure.

## 4. Technologies Used

- Python
- Requests
- BeautifulSoup4
- CSV Module

## 5. Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install requests beautifulsoup4
```

## 6. How to Run

Execute the main scraper:

```bash
python scrapper.py
```

After successful execution, the scraped data will be saved in:

```text
books.csv
```

## 7. Output

The generated CSV contains five columns:

- title
- price
- availability
- rating
- description

The scraper successfully extracts all 11 books listed in the Travel category.

## 8. Error Handling

The implementation includes:
- Request timeout handling.
- HTTP status validation using `raise_for_status()`.
- Exception handling for failed requests.
- Fallback values when book descriptions are unavailable.

## 9. Author

**Vaibhav Tiwari**

VuduCom – Tech Intern Assignment