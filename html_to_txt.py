import requests
from bs4 import BeautifulSoup

index_chapter = 0

while index_chapter < 232:
    with open("E:\\Z\\Links.txt", "r") as filepath:
        url_list = filepath.readlines()

    url = url_list[index_chapter].strip()  

    try:
        #
        response = requests.get(url)
        response.raise_for_status()  

        
        soup = BeautifulSoup(response.text, 'html.parser')

       
        content_div = soup.find('div', id='chr-content', class_='chr-c')

        if content_div:
            
            content_text = content_div.get_text(separator='\n', strip=True)

            
            with open(f"E:\\Z\\chapter_text_files\\chapter_{index_chapter}.txt", "w", encoding="utf-8") as file:
                file.write(content_text)

            print(f"Content saved to chapter_{index_chapter}.txt")
        else:
            print("Div with id 'chr-content' not found.")

        index_chapter += 1

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error for URL {url}: {e}")
        index_chapter += 1  

    except Exception as e:
        print(f"An error occurred: {e}")
        break  
