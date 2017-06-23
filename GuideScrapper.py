import urllib.request
from bs4 import BeautifulSoup
import pdfkit
import os
'''
It recives an url
Reads the source code of the page/s
Parses the pages
Outputs Temporal pages in temporal folder1
Gets all the pages, then fuse them into a single PDF
Success

TODO: Delete temporal folder before exit.
TODO: To make it compatible with single paged, spaghetti guides.

'''
def send_response(url,headers):
    req = urllib.request.Request(url, None, headers)
    print(url)
    #Seends request
    response = urllib.request.urlopen(req)
    #Reads page
    page = response.read()
    return page


def get_page(url,max_page):
    #An array of pages, too lazy to rename it properly in english
    arreglo_paginas = []
	#Header, just in case, yes, i copy-pasted from Stack Overflow
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
	#Requesting is donde here, request main page and add its extra pages
    arreglo_paginas.append(send_response(url,headers))
    for i in range(max_page):
        n = i + 1
        print (str(i)+"  : "+str(n))
        if n >= max_page:
            break
            
        urltemp = url+"?page="+str(n)
        arreglo_paginas.append(send_response(urltemp,headers))
    return arreglo_paginas
 
def to_pdf():
    #Here is where you turn the temporal pages into a single PDF.
    #Yes, it should be 2 different methods, but im a lil bit too lazy
    dir_array = []
    for file in os.listdir("temp"):
        if file.endswith(".html"):
            print(os.path.join("temp", file))
            dir_array.append(os.path.join("temp", file))
    pdfkit.from_file(dir_array,'guide.pdf')
    
def parse_content(page,number):
    #Yet, another method that should be 2
    #Here, we parse the page array
    #This if, is for avoiding an unsorted PDF
    if(number < 10):
        filename = 'temp/page0'+str(number)+'.html'
    else:
        filename = 'temp/page'+str(number)+'.html'
    #Creates temp dir to store the htmls, if doesnt exist, it creates a new folder
    #It strips unneeded html tags, and outputs a temporal HTML
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    soup = BeautifulSoup(page, 'html.parser')
    soup.find("div", {"class":"ftoc"}).decompose()
    print("Imprimiendo: "+str(number))
    with open(filename, 'w') as file:
      file.write(str(soup.find_all("div", {"class":"ffaq"})))
   


#Replace URL and pages
index = get_page("URL", pages)
array_of_html = []
for i in range(len(index)):
    array_of_html.append(parse_content(index[i],i))
to_pdf()
exit()
