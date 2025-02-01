from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Set up the proxy server details
proxy_ip_port = "127.0.0.1:8080"

# Configure the proxy
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

# Create a WebDriver instance with the proxy settings
chrome_options = webdriver.ChromeOptions()
chrome_options.proxy = proxy

driver = webdriver.Chrome(options=chrome_options)

# Navigate to a website
driver.get("http://www.example.com")

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()
