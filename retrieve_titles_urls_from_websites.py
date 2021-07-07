
# def retrieve_from_siggraph(driver):
#     pdfurllist =  []
#     pdfnamelist = []
#     import time    
#     elementllist =  driver.find_elements_by_class_name('toc__section')[1:-2]
#     for i, section in enumerate(elementllist):
#         section.find_element_by_partial_link_text('SESSION').click()
#         time.sleep(3)
#         # print(session_name)
#         for j, paper_element in enumerate(section.find_elements_by_class_name('issue-item__content')):
#             paper_name = paper_element.find_element_by_xpath('div/h5').text
#             pdf_url = paper_element.find_element_by_class_name('red').get_attribute('href')

#             pdfnamelist.append(paper_name)
#             pdfurllist.append(pdf_url)

#     return pdfurllist, pdfnamelist


def retrieve_from_siggraph(driver):
    pdfurllist =  []
    pdfnamelist = []
    import time    
    elementllist =  driver.find_elements_by_class_name('accordion-tabbed')[1].find_elements_by_class_name('toc__section')
    for i, section in enumerate(elementllist):
        section.click()
        time.sleep(3)
        print('\n', section.text)
        for j, paper_element in enumerate(section.find_elements_by_class_name('issue-item__content')):
            paper_name = paper_element.find_element_by_xpath('div/h5').text
            pdf_url = paper_element.find_element_by_class_name('red').get_attribute('href')
            print('\t', paper_name)
            pdfnamelist.append(paper_name)
            pdfurllist.append(pdf_url)

    return pdfurllist, pdfnamelist


def retrieve_from_iclr(driver):
    pdfurllist =  []
    pdfnamelist = []
    
    # three sections: oral, spotlight, poster
    for num_section, section in enumerate(['Oral', 'Spotlight', 'Poster']):
        driver.find_element_by_partial_link_text(section).click()
        elementllist =  driver.find_elements_by_tag_name('h4')[1:]
        for i, element in enumerate(elementllist): 
            pdfnamelist.append(elementllist[i].text)
            pdfurllist.append(elementllist[i].find_elements_by_xpath('a')[1].get_attribute('href'))

    return pdfurllist, pdfnamelist



def retrieve_from_eccv(driver):
    pdfurllist =  []
    pdfnamelist = []

    elementllist =  driver.find_elements_by_class_name('ptitle')
    url_element_list =  driver.find_elements_by_link_text('pdf')
    for i, element in enumerate(url_element_list): 
        pdfnamelist.append(elementllist[i].text)
        pdfurllist.append(url_element_list[i].get_attribute('href'))
    return pdfurllist, pdfnamelist



def retrieve_from_iccv(driver):
    pdfurllist =  []
    pdfnamelist = []

    title_element_list = driver.find_elements_by_class_name('ptitle')
    url_element_list = driver.find_elements_by_partial_link_text('pdf')
    for i, element in enumerate(url_element_list): 
        pdfnamelist.append(title_element_list[i].text)
        pdfurllist.append(url_element_list[i].get_attribute('href'))
    return pdfurllist, pdfnamelist


def retrieve_from_icml(driver):
    pdfurllist =  []
    pdfnamelist = []
    elementllist =  driver.find_elements_by_class_name('title')
    url_element_list =  driver.find_elements_by_link_text('Download PDF')
    for i, element in enumerate(url_element_list): 
        pdfnamelist.append(elementllist[i].text)
        pdfurllist.append(url_element_list[i].get_attribute('href'))
    return pdfurllist, pdfnamelist



def retrieve_from_neurips(driver):
    pdfurllist =  []
    pdfnamelist = []
    elementllist =  driver.find_elements_by_tag_name('li')[2:]
    for i, element in enumerate(elementllist): 
        pdfnamelist.append(elementllist[i].find_elements_by_xpath('a')[0].text)
        pdfurllist.append(elementllist[i].find_elements_by_xpath('a')[0].get_attribute('href').replace('hash', 'file', 1). \
                                                                            replace('Abstract.html', 'Paper.pdf', 1))
    return pdfurllist, pdfnamelist

def retrieve_from_cvpr(driver):
    pdfurllist =  []
    pdfnamelist = []
    for day in range(3):
        driver.find_elements_by_xpath('//body/div[3]/dl/dd/a')[day].click()
        title_element_list = driver.find_elements_by_class_name('ptitle')
        url_element_list = driver.find_elements_by_partial_link_text('pdf')
        for i, element in enumerate(url_element_list): 

            pdfnamelist.append(title_element_list[i].text)
            pdfurllist.append(url_element_list[i].get_attribute('href'))
        driver.back()
        
    return pdfurllist, pdfnamelist
