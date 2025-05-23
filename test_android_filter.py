from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver
driver_path = "C:/path/to/chromedriver.exe"  # <- Update this path

# Start browser
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://uem.mgt.entgra.net/app-publisher/apps")
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)

    # Step 1: Click on the “Search Apps” bar
    search_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ant-collapse-header-text")))
    search_bar.click()

    # Step 2: Click on “+” (plus) button
    plus_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-filter-button")))  # Adjust selector
    plus_button.click()

    # Step 3: Select “Platform” from the drop-down
    platform_option = wait.until(EC.element_tose_be_clickable((By.XPATH, "//li[contains(text(), 'Platform')]")))
    platform_option.click()

    # Step 4: Click on the “Select Filter” dropdown
    filter_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".filter-dropdown")))  # Adjust selector
    filter_dropdown.click()

    # Step 5: Select “android” as the filter
    android_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'android')]")))
    android_option.click()

    # Step 6: Click on the “Search” icon
    search_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-icon")))
    search_icon.click()

    # Step 7: Verify only Android apps are visible (if class names are available)
    apps = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "app-card")))  # Adjust class
    for app in apps:
        label = app.find_element(By.CLASS_NAME, "platform-label").text.lower()

    # Step 7: Verify only Android apps are visible (if class names are available)
    apps = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "app-card")))  # Adjust class
    for app in apps:
        label = app.find_element(By.CLASS_NAME, "platform-label").text.lower()

             
    # Step 7: Verify only Android apps are visible (if class names are available)
    apps = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "app-card")))  # Adjust class
    for app in apps:
        label = app.find_element(By.CLASS_NAME, "platform-label").text.lower()

             
    # Step 7: Verify only Android apps are visible (if class names are available)
    apps = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "app-card")))  # Adjust class
    for app in apps:
        label = app.find_element(By.CLASS_NAME, "platform-label").text.lower()