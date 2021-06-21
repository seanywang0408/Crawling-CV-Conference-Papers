from selenium import webdriver  
import time  
import urllib  
from slugify import slugify
import requests
import random
import os


"""
some variables needed to be set up by users

conference urls examples:

cvpr: https://openaccess.thecvf.com/CVPR2020 (CVPR 2020)
eccv: https://openaccess.thecvf.com/ECCV2018 (ECCV 2018)
eccv: https://www.ecva.net/papers.php (ECCV 2020) (changed in 2020)
iccv: https://openaccess.thecvf.com/ICCV2019 (ICCV 2019)
icml: http://proceedings.mlr.press/v119/ (ICML 2020)
neurips: https://papers.nips.cc/paper/2020 (NeurIPS 2020)
iclr: https://openreview.net/group?id=ICLR.cc/2021/Conference (ICLR 2021)
siggraph: https://dl.acm.org/toc/tog/2020/39/4 (SIGGRAPH 2021)

"""
conference = 'cvpr'
conference_url = "https://openaccess.thecvf.com/CVPR2021?day=all" # the conference url to download papers from
chromedriver_path = 'C:\\Users\\xiaoyang\\Downloads\\chromedriver.exe' # the chromedriver.exe path
root = r'E:\OneDrive\academics\papers\conferences\CVPR-2021-ALL'.replace('\\','/') # file path to save the downloaded papers

os.makedirs(root, exist_ok=True)
print(root)


driver = webdriver.Chrome(chromedriver_path)  
driver.get(conference_url)

def retrieve_from_cvpr2021(driver):
    pdfurllist =  []
    pdfnamelist = []
    
    title_element_list = driver.find_elements_by_class_name('ptitle')
    url_element_list = driver.find_elements_by_partial_link_text('pdf')
    for i, element in enumerate(url_element_list): 
        pdfnamelist.append(title_element_list[i].text)
        pdfurllist.append(url_element_list[i].get_attribute('href'))
            
    return pdfurllist, pdfnamelist
    
retrieve = retrieve_from_cvpr2021
print('Retrieving pdf urls. This could take some time...')
pdfurllist, pdfnamelist = retrieve(driver)

# check the retrieved urls
print('The first 5 pdf urls:\n')
for i in range(5):
    print(pdfurllist[i])
print('\nThe last 5 pdf urls:\n')
for i in range(5):
    print(pdfurllist[-(i+1)])
print('=======================================================')

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


# download the papers one by one. The files are named after the titles (guaranteed to be valid file name after processed by slugify.)
print('Start downloading')
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
for i, url in enumerate(pdfurllist):
    if url != None :      
        pdfname = slugify(pdfnamelist[i])
        if os.path.isfile(root+'/'+pdfname+".pdf"):
            print('existed', i, '\t', pdfnamelist[i], '\t', pdfurllist[i])
        else:
            print(i, '\t', pdfnamelist[i], '\t', pdfurllist[i])
            data = requests.get(pdfurllist[i], timeout=80, headers=headers).content
            
            with open(root+'/'+pdfname+".pdf", 'wb')  as f:
                f.write(data)  
            _ = time.sleep(random.uniform(4,5)) # for anti-anti-crawler purpose