import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

class AlltestimonialsSpider(scrapy.Spider):
    name = "alltestimonials"
    allowed_domains = ["hibiscus.services"]
    start_urls = ["https://hibiscus.services/"]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)  

        testimonials = self.driver.find_elements(By.CSS_SELECTOR, 'div.swiper-slide')

        for index, testimonial in enumerate(testimonials):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", testimonial)
            time.sleep(1)  

            screenshot_path = f"screenshots/testimonial_{index + 1}.png"
            testimonial.screenshot(screenshot_path)

            yield {
                'Image': testimonial.find_element(By.CSS_SELECTOR, 'img').get_attribute('src'),
                'Name': testimonial.find_element(By.CSS_SELECTOR, 'h2').text,
                'Designation': testimonial.find_element(By.CSS_SELECTOR, 'h3').text,
                'Introduction': testimonial.find_element(By.CSS_SELECTOR, 'p').text,
                'Screenshot': screenshot_path,
            }

    def closed(self, reason):
        self.driver.quit()
