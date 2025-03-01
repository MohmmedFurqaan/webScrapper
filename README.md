**Hacker News Scraper 📰🚀**

A Python-based web scraper that fetches the top-voted news articles from Hacker News using BeautifulSoup and Requests. The script extracts article titles, links, and vote counts, filtering articles with more than 99 votes and sorting them in descending order.

Features

✅ Scrapes news from multiple Hacker News pages

✅ Extracts article title, URL, and vote count

✅ Filters articles with more than 99 upvotes

✅ Sorts results by votes (highest first)

✅ Handles HTTP errors gracefully

Technologies Used

🐍 Python 3

🌐 Requests (for making HTTP requests)

🛠️ BeautifulSoup (for web scraping)

Installation & Usage

1️⃣ Clone the Repository

**bash**

Copy

git clone https://github.com/MohmmedFurqaan/webScrapper.git

cd webScrapper

2️⃣ Install Dependencies

bash

Copy

Edit

pip install -r requirements.txt

3️⃣ Run the Script

bash

Copy

Edit

python script.py

Example Output

lua

Copy

Edit

--- Page 1 News ---

{'title': 'OpenAI Announces GPT-4 Turbo', 'link': 'https://openai.com/news', 'votes': 230}

{'title': 'New Linux Kernel Released', 'link': 'https://kernel.org', 'votes': 180}

--- Page 2 News ---

{'title': 'Python 3.13 Features', 'link': 'https://python.org', 'votes': 150}

Contributing

Feel free to submit a Pull Request or open an Issue if you have suggestions for improvements.

License

📜 MIT License – Use it freely!


