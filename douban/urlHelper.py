
class UrlCreator:

    def generate_list_url(self, base_url, times, step = 20):
        page_count = times * step
        return base_url.format(page_count)

