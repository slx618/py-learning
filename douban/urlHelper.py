
class UrlCreator(object):

    @staticmethod
    def generate_list_url(self, base_url, times, step = 20):
        page_count = times * step
        return print(base_url %page_count)

