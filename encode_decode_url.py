"""
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and
it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
can be decoded to the original URL.
"""


class Codec:
    dict_h = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.dict_h = {}
        url_hash = str(hash(longUrl))
        self.dict_h[url_hash] = longUrl
        shortUrl = "http://tinyurl.com/" + str(url_hash)
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        hash_part = shortUrl[19:]
        return self.dict_h[hash_part]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))