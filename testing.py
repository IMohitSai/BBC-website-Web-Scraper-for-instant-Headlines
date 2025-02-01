from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# Automatically download and setup ChromeDriver
service = Service(ChromeDriverManager().install())

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_and_print_content(url):
    driver.get(url)
    # Wait for the page to load
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body")))
    
    # Find and print all content on the page
    content_elements = driver.find_elements(By.CSS_SELECTOR, 'article')
    for i, content_element in enumerate(content_elements):
        content = content_element.text.strip()
        print(f"Content {i+1} from {url}:")
        try:
            print(content)
        except UnicodeEncodeError:
            print("Unable to display content due to encoding issues.")
        print()


# URL of the BBC home page
url = "https://www.bbc.com/"

# Scraping content from the main BBC home page
print("Content from the main BBC home page:")
scrape_and_print_content(url)

# Find links on the home page and visit them to scrape content
links = driver.find_elements(By.CSS_SELECTOR, 'a')
num_links_visited = 0
for link in links:
    try:
        link_url = link.get_attribute('href')
        if link_url and "bbc.com" in link_url and num_links_visited < 2:
            print(f"\nVisiting link: {link_url}")
            print("-------------------------------------")
            scrape_and_print_content(link_url)
            num_links_visited += 1
    except StaleElementReferenceException:
        continue

    if num_links_visited >= 2:
        break

# Close the driver
driver.quit()
