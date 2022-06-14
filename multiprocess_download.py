
from selenium import webdriver  
import time  
import urllib  
from slugify import slugify
import requests
import random
import os

"""
some variables needed to be set up by users
"""
conference = 'cvpr'
conference_url = "https://openaccess.thecvf.com/CVPR2022?day=all" # the conference url to download papers from
edgedriver_path = 'C:\\Users\\xiaoyang\\Downloads\\edgedriver_win64\msedgedriver.exe' # the chromedriver.exe path
root = r'E:\OneDrive\academics\papers\conferences\CVPR-2022-ALL'.replace('\\','/') # file path to save the downloaded papers
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
# Num of thread set to 8. Modified to the Num of core of your cpu might improve the performance.
num_threads = 8


def download_one(i, pdfname, pdfurl):
    if pdfurl != None :      
        pdfname_slugified = slugify(pdfname)
        if os.path.isfile(root+'/'+pdfname_slugified+".pdf"):
            print('existed', i, '\t', pdfname, '\t', pdfurl)
        else:
            print(i, '\t', pdfname, '\t', pdfurl)
            
            try_download = True
            while try_download:
                try:
                    data = requests.get(pdfurl, timeout=80, headers=headers).content
                    try_download = False
                except TimeoutError as e:
                    _ = time.sleep(random.uniform(1,2)) # for anti-anti-crawler purpose
                except ConnectionError as e: 
                    _ = time.sleep(random.uniform(1,2)) # for anti-anti-crawler purpose
                
            with open(root+'/'+pdfname_slugified+".pdf", 'wb')  as f:
                f.write(data)  


if __name__ == '__main__':

    os.makedirs(root, exist_ok=True)
    print(root)

    driver = webdriver.Edge(edgedriver_path)  
    driver.get(conference_url)

    def retrieve_from_cvpr2022(driver):
        pdfurllist =  []
        pdfnamelist = []

        title_element_list = driver.find_elements_by_class_name('ptitle')
        url_element_list = driver.find_elements_by_partial_link_text('pdf')
        for i, element in enumerate(url_element_list): 
            pdfnamelist.append(title_element_list[i].text)
            pdfurllist.append(url_element_list[i].get_attribute('href'))        
        return pdfurllist, pdfnamelist

    print('Retrieving pdf urls. This could take some time...')
    pdfurllist, pdfnamelist = retrieve_from_cvpr2022(driver)


    # check the retrieved urls
    print('The first 5 pdf urls:\n')
    for i in range(5):
        print(pdfurllist[i])
    print('\nThe last 5 pdf urls:\n')
    for i in range(5):
        print(pdfurllist[-(i+1)])

    # check the retrieved paper titles
    print('The first 5 pdf titles:\n')
    for i in range(5):
        
        print(pdfnamelist[i])
    print('\nThe last 5 pdf titles:\n')
    for i in range(5):
        print(pdfnamelist[-(i+1)])

    print('The number of papers is ', len(pdfnamelist))
    assert len(pdfnamelist)==len(pdfurllist), 'The number of titles and the number of urls are not matched. \
                                                You might solve the problem by checking the HTML code in the \
                                                website yourself or you could ask the author by raising an issue.'


    input_args = []
    for i, (pdfname, pdfurl) in enumerate(zip(pdfnamelist, pdfurllist)):
        input_args.append((i, pdfname, pdfurl))

    from multiprocessing import Pool
    with Pool(num_threads) as p:
        p.starmap(download_one, input_args)