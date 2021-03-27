# Crawling-CV-Conference-Papers

## Introduction

Python code to crawl computer vision papers from top CV conferences. Currently it supports CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR, SIGGRAPH. It leverages [selenium](https://www.selenium.dev/), a website testing framework to crawl the titles and pdf urls from the conference website, and download them one by one with some simple anti-anti-crawler tricks.

Websites for older conferences are not guaranteed to be bug-free, since this project is based on newest website structure.

## Requirements
```
pip install selenium, slugify
```
Besides, downlowd [chromedriver.exe](https://chromedriver.chromium.org/downloads) from the link to any local path you favour.

## Usage

To execute the crawler, you could run *download.py* or *download.ipynb* (Basically the same). Before the execution, some paths need to be set up, including:

```
conference = 'neurips'
conference_url = "https://papers.nips.cc/paper/2019" # the conference url to download papers from
chromedriver_path = '.../chromedriver.exe' # the chromedriver.exe path
root = './NeurIPS-2019-ALL' # file path to save the downloaded papers
```

Here are some conference url examples:

```
cvpr: https://openaccess.thecvf.com/CVPR2020 (CVPR 2020)
eccv: https://openaccess.thecvf.com/ECCV2018 (ECCV 2018) (changed in 2020)
eccv: https://www.ecva.net/papers.php (ECCV 2020) 
iccv: https://openaccess.thecvf.com/ICCV2019 (ICCV 2019)
icml: http://proceedings.mlr.press/v119/ (ICML 2020)
neurips: https://papers.nips.cc/paper/2020 (NeurIPS 2020)
iclr: https://openreview.net/group?id=ICLR.cc/2021/Conference (ICLR 2021)
siggraph: https://dl.acm.org/toc/tog/2020/39/4 (SIGGRAPH 2021)
```
Replace the url and the conference names with your choice.

## Others

**Warnings**: It is heard that crawling from conference websites might cause a banning of your IP (hasn't happened to me so far). Not sure of the risk. 

**Warnings**: This project is for learning purpose only. Do not crawl the same website frequently, which will burden the server.

*Welcome to submit a **pull request** if there is any bugs or if you would like to add support to other conferences!*

## Maintainer

[Xiaoyang Huang](https://github.com/seanywang0408) 
Email: huangxiaoyang@sjtu.edu.cn

