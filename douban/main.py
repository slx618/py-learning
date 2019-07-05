# -*- coding:utf8 -*-


from urlHelper import UrlCreator


def __init__():
    list_page_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=最新&page_limit=20&page_start={0}'
    url_creator = UrlCreator()
    url = url_creator.generate_list_url(list_page_url, 1)
    print(url)

if __name__ == '__main__':
    __init__()