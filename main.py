import requests    # For sending HTTP requests
import bs4  #BeautifulSoup     # BeautifulSoup for parsing HTML

url=input("Enter Your URL : ")

response=requests.get(url)
# print(type(response))
# print(response.text)

filename="temp.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")     # Parsing the HTML Content

formatted_text=bs.prettify()  #Formatting the HTML code
# print(formatted_text)

with open(filename,"w+",encoding="utf-8") as f:
      f.write(formatted_text)

# list_imgs=bs.find_all('img')
# # print(list_imgs)
# no_of_imgs=len(list_imgs)
# list_as=bs.find_all('a')
# no_of_as=len(list_as)
# print("Number of images tag :",no_of_imgs)
# print("Number of anchor tag :",no_of_as)