class UrlConverter():
    BASE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z'
            ]

    @classmethod
    def id_to_base62_url(cls, id):
        url = ''
        for i in range(6):
            url = cls.BASE[id % 62] + url
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