import json
import requests
import arabic_reshaper
from bidi.algorithm import get_display
import tkinter as tk

reshaper_config = arabic_reshaper.ArabicReshaper(configuration={'use_unshaped_instead_of_isolated': True})

#Constraints
API_URL = "https://api.quran.com/api/v4/quran/verses/indo-pak"
MAX_PAGES = 604
MIN_PAGES = 1



def get_page(page_no: int) -> dict:
    url = f"https://api.quran.com/api/v4/quran/verses/indo-pak?page_number={page_no}"
    response = requests.get(url)
    if response.status_code == 200:
        quran_page = response.json()
        texts = [(verse["verse_key"],verse["text_uthmani"]) for verse in quran_page["verses"]]
    else:
        print("Error requesting the page")
        return None
    return texts

def connect_pages(page_no: int):
    next_page_no = page_no + 1
    
    quran_page = get_page(page_no)
    quran_page_next = get_page(next_page_no)
    final_ayah = quran_page[-1]
    first_ayah_next = quran_page_next[0]
    print(f"last ayah of the page: {final_ayah}")
    print(f"first_ayah of the next page: {first_ayah_next}")
 
def display_page(page: dict):
    quran_page = get_page(page)
    for verse_key, text_uthmani in quran_page:
        print(f"{verse_key}: {text_uthmani}\n")

#the following function is not completed. Complete it before proceeding to run the code
def get_surah(surah_number: int):
    url = f"https://api.quran.com/api/v4/quran/verses/indo-pak?page_number={page_no}"
    response = requests.get(url)
    if response.status_code == 200:
        quran_page = response.json()
        texts = [(verse["verse_key"],verse["text_uthmani"]) for verse in quran_page["verses"]]
    else:
        print("Error requesting the page")
        return None
    return texts

def main():
    option = int(input("select the action you want to take from the following\n 1-Enter if you want to select a page \n 2-Select if you want to connect two pages\n"))
    if (option != 1 and option != 2):
        print("there is no such option")
        return
    if option == 1:
        #Take inputs
        page_no = int(input("Enter the page you want to view: "))
        if(page_no > MAX_PAGES or page_no < MIN_PAGES):
            exit()
        
        display_page(page_no)
    if option == 2:
        #Take inputs
        page_no = int(input("Enter the page you want to connect to the next page: "))
        if(page_no > MAX_PAGES or page_no < MIN_PAGES):
            exit()
        connect_pages(page_no)

if __name__ == "__main__":
    main()