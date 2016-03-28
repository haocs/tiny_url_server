class UrlConverter():
    base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    @classmethod
    def id_to_base62_url(cls, id):
        url = ''
        for i in range(6):
            url = cls.base[id % 62] + url
            id /= 62
        return url

    @classmethod
    def base62_url_to_id(cls, url):
        def char_to_base(c):
            if c < 'A':
                return ord(c) - 48
            elif 'A' <= c and c <= 'Z':
                return ord(c) - 65 + 10
            else:
                return ord(c) - 97 + 36

        id = 0
        for c in url:
            id = id * 62 + char_to_base(c)
        return id