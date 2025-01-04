import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


stock_name = r'vodafone'


def scrape_fundamentals(stock_name):
    screener_url = "https://www.screener.in/"

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--headless')

    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(screener_url)

    wait = WebDriverWait(driver, timeout=2)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[2]/div/div/div/input')))   

    driver.find_element(By.XPATH, '/html/body/nav/div[2]/div/div/div/div[2]/div[2]/a[1]').click()
    time.sleep(1)

    email_field = driver.find_element(By.ID, 'id_username')
    email_field.send_keys(email_id)
    
    password_field = driver.find_element(By.ID, 'id_password')
    password_field.send_keys(password)

    time.sleep(1)
    login_button = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/form/button').click()
    time.sleep(3)

    search_stock = driver.find_element(By.XPATH, '//*[@id="desktop-search"]/div/input')
    search_stock.send_keys(stock_name)
    time.sleep(1)
    search_stock.send_keys(Keys.ENTER)
    
    fundamentals = {}

    current_price = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[2]/span[2]/span')
    volume = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[10]/span[2]/span')

    pe_ratio = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[4]/span[2]/span')
    cash_market_cap = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[17]/span[2]/span')
    peg_ratio = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[18]/span[2]/span')
    evebitda = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[19]/span[2]/span')
    price_to_book = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[20]/span[2]/span')
        
    roe = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[8]/span[2]/span')
    roce = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[7]/span[2]/span')
    wc_to_sales = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[21]/span[2]/span')
    asset_turnover = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[22]/span[2]/span') 
    debtor_days = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[23]/span[2]/span')
    croic = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[24]/span[2]/span')

    sales_growth = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[11]/span[2]/span')
    net_profit_growth = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[14]/span[2]/span')
    sales_growth_3years = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[12]/span[2]/span')
    quater_sales_growth_YOY = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[13]/span[2]/span')
    eps = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[15]/span[2]/span')
    eps_lastyear = driver.find_element(By. XPATH, '//*[@id="top-ratios"]/li[16]/span[2]/span')

    dividend_yield = driver.find_element(By.XPATH, '//*[@id="top-ratios"]/li[6]/span[2]/span')


    current_price = current_price.text.strip().replace(",", "")
    volume = volume.text.strip().replace(",", "")
    pe_ratio = pe_ratio.text.strip().replace(",", "")
    cash_market_cap = cash_market_cap.text.strip().replace(",", "")
    peg_ratio = peg_ratio.text.strip().replace(",", "")
    evebitda = evebitda.text.strip().replace(",", "")
    price_to_book = price_to_book.text.strip().replace(",", "")
    roe = roe.text.strip().replace(",", "")
    roce = roce.text.strip().replace(",", "")
    wc_to_sales = wc_to_sales.text.strip().replace(",", "")
    asset_turnover = asset_turnover.text.strip().replace(",", "")
    debtor_days = debtor_days.text.strip().replace(",", "")
    croic = croic.text.strip().replace(",", "")
    sales_growth = sales_growth.text.strip().replace(",", "")
    net_profit_growth = net_profit_growth.text.strip().replace(",", "")
    sales_growth_3years = sales_growth_3years.text.strip().replace(",", "")
    quater_sales_growth_YOY = quater_sales_growth_YOY.text.strip().replace(",", "")
    eps = eps.text.strip().replace(",", "")
    eps_lastyear = eps_lastyear.text.strip().replace(",", "")
    dividend_yield = dividend_yield.text.strip().replace(",", "")

    fundamentals["stock name"] = stock_name
    fundamentals['current_price'] = current_price
    fundamentals['volume'] = volume
    fundamentals['pe_ratio'] = pe_ratio
    fundamentals['cash_market_cap'] = cash_market_cap
    fundamentals['peg_ratio'] = peg_ratio
    fundamentals['evebitda'] = evebitda
    fundamentals['price_to_book'] = price_to_book
    fundamentals['roe'] = roe
    fundamentals['roce'] = roce
    fundamentals['wc_to_sales'] = wc_to_sales
    fundamentals['asset_turnover'] = asset_turnover
    fundamentals['debtor_days'] = debtor_days
    fundamentals['croic'] = croic
    fundamentals['sales_growth'] = sales_growth
    fundamentals['net_profit_growth'] = net_profit_growth
    fundamentals['sales_growth_3years'] = sales_growth_3years
    fundamentals['quater_sales_growth_YOY'] = quater_sales_growth_YOY
    fundamentals['eps'] = eps
    fundamentals['eps_lastyear'] = eps_lastyear
    fundamentals['dividend_yield'] = dividend_yield


    with open('fundamentals.json', 'w') as file:
        json.dump(fundamentals, file, indent=4)

    driver.quit()

scrape_fundamentals(stock_name)