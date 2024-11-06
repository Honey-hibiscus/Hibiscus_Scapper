Installation and Setup
Follow these steps to set up the project locally:

Step 1: Clone the repository
git clone https://github.com/Honey-hibiscus/Hibiscus_Scraper.git
cd Hibiscus_Scraper

Step 2: Create a virtual environment
It is recommended to use a virtual environment to keep your dependencies isolated.
python -m venv venv

Step 3: Activate the virtual environment
venv\Scripts\activate

Step 4: Install dependencies
Once the virtual environment is activated, install the required dependencies from the requirements.txt file.
pip install -r requirements.txt

Usage
To run the scraper, use the following Scrapy command:
scrapy crawl testimonials 
scrapy crawl alltestimonials 

Output
You can use the following command to save the output to a .json file:
scrapy crawl testimonials -o output.json
