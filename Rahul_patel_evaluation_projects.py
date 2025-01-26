import os
import time
import random
import requests
from datetime import datetime
import pygetwindow as gw
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json



# >>>>>>>>>>>>>>>>>>For geting new IP Start>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def get_current_ip():

    
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        response.raise_for_status()
        return response.json()["ip"]
    except Exception as e:
        print(f"Error fetching IP address: {e}")
        return None


def proton_random_Rahul_Patel_Evaluation(action, connect_list=None):
   
    openvpn_gui_path = r"C:\Program Files\OpenVPN\bin\openvpn-gui.exe"
    
    if connect_list is not None:
        location = random.choice(connect_list)
        print(f'"{openvpn_gui_path}" --command {action} "{location}"')
        os.popen(f'"{openvpn_gui_path}" --command {action} "{location}"').read()

        
        log_path = os.path.join(os.getcwd(), "proton-log.txt")
        log_entry = f"{datetime.now():%Y-%m-%d %H:%M:%S} {location}\n"
        windows = gw.getAllTitles() 
        for window in windows: 
            if "OpenVPN" in window:
                try:
                    win = gw.getWindowsWithTitle(window)[0]
                    win.close()
                except Exception as e:
                     print(f"Error closing window: {window}, {e}")    
         

        with open(log_path, "a") as log_file:
            log_file.write(log_entry)

        return location
    else:
        
        os.popen("taskkill /F /IM openvpn.exe")
        windows = gw.getAllTitles()
        for window in windows: 
            if "OpenVPN" in window:
                try:
                    win = gw.getWindowsWithTitle(window)[0]
                    win.close()
                except Exception as e:
                     print(f"Error closing window: {window}, {e}")    
         
         
    


def Get_NEW_ASSIGN_IP_Rahul_Patel_Evaluation_Peoject():
    
    config_dir = r"C:\Users\Rahul Patel\OpenVPN\config"
    
    ovpn_files = [
        os.path.join("us-free-1.protonvpn.udp.ovpn"),
        os.path.join("us-free-2.protonvpn.udp.ovpn"),
        os.path.join("us-free-51.protonvpn.udp.ovpn"),
        os.path.join("jp-free-2.protonvpn.udp.ovpn"),
    ]

    original_ip = get_current_ip()
    print(f"-------------------->Original IP: {original_ip}<---------------------")

    
    print("Connecting to VPN...")
    connected_file = proton_random_Rahul_Patel_Evaluation("connect", ovpn_files)

   
    print(f"Connected to VPN using: {connected_file}")
    print("Waiting for the connection to establish...")
    time.sleep(15)

    new_ip = get_current_ip()
    print(f"-------------------->New IP after VPN connection: {new_ip} <---------------------")
# >>>>>>>>>>>>>>>>>>>For geting New IP Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def human_typing(element, text, delay_range=(0.1, 0.3)):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(*delay_range))



def search_keywords_with_human_behavior_Rahul_Patel_Evaluation(keywords):
    print("####################################Code Start Running ##############################################")
    
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  
    chrome_options.add_argument("--start-maximized") 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    
    output_dir = "ScrapedData"
    os.makedirs(output_dir, exist_ok=True)

    results = []  
    driver.get("https://dnsleaktest.com/")
    time.sleep(5)

    try:
        for keyword in keywords:
            print(f"___________________________>>>>Searching for: {keyword}<<<<<<_______________________")
            Get_NEW_ASSIGN_IP_Rahul_Patel_Evaluation_Peoject()
            
            
            driver.get("https://dnsleaktest.com/")
            time.sleep(5)
            driver.get("https://duckduckgo.com/")
            time.sleep(random.uniform(1, 3))  

            
            search_box = driver.find_element(By.NAME, "q")

            
            print(f"Typing keyword: {keyword}")
            human_typing(search_box, keyword)
            search_box.send_keys(Keys.RETURN)
            time.sleep(random.uniform(3, 5))  

            try:
                links = driver.find_elements(By.TAG_NAME, "a")
                all_links = []

                for link in links:
                    href = link.get_attribute("href")
                    if href: 
                         all_links.append(href)

                refined_links = [link for link in all_links if link.startswith("https://www.")]         
                final_Links = refined_links[0]
                driver.get(final_Links)
                time.sleep(5)

                html_content = driver.page_source
                soup = BeautifulSoup(html_content, 'html.parser')
                page_title = soup.title.string.strip() if soup.title else "No title"                
        
                results.append({
                    "keyword": keyword,
                    "title": page_title,
                    "url": driver.current_url,
                    "html": soup.prettify()
                })
                print(f"Saved data for: {keyword}")

            except Exception as e:
                print(f"Failed to process keyword '{keyword}': {e}")

            time.sleep(random.uniform(2, 4))  

            print("--------------------->Disconnecting VPN...<---------------------")
            proton_random_Rahul_Patel_Evaluation("disconnect")
            

       
        output_file = os.path.join(output_dir, "results.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
        print(f"######################## All data saved to {output_file} ####################################")

    finally:
        driver.quit()



def main():
    keywords = ["AI for Businesses", "Python programming tutorial", "Machine Learning applications"]
    search_keywords_with_human_behavior_Rahul_Patel_Evaluation(keywords)


if __name__ == "__main__":
    main()
