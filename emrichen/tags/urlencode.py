from urllib.parse import quote_plus, urlparse, urlunparse, parse_qsl, urlencode

from .base import BaseTag


class URLEncode(BaseTag):
    """
    arguments: |
        A string to encode
        **OR**
        `url`: The URL to combine query parameters into
        `query`: An object of query string parameters to add.
    example: |
        `!URLEncode "foo+bar"`
        `!URLEncode { url: "https://example.com/", query: { foo: bar } }`
    description:
        Encodes strings for safe inclusion in a URL, or combines query string parameters into a URL.
    ---
    Three modes of operation:

    1. Just encode a plain string

        !URLEncode "foo+bar" -> "foo%2Bbar"

    2. Form a query string

        !URLEncode
            query:
                foo: bar

        -> "foo=bar"

    3. Combine a base URL and query string parameters

        !URLEncode
            url: "https://example.com/?foo=x"
            query:
                bar: xyzzy

        -> "https://example.com/?foo=x&bar=xyzzy"

    TODO Add query_mode: append|replace (currently append)
    """

    value_types = (str, dict)

    def enrich(self, context):
        if isinstance(self.data, str):
            # 1. Just encode a plain string
            return quote_plus(self.data)

        url = self.data.get('url')
        query = self.data.get('query')

        if url is not None:  # empty string ok!
            # 3. Combine a base URL and query string parameters
            url = urlparse(url)
            query = query or {}
            query = parse_qsl(url.query) + list(query.items())
            url = url._replace(query=urlencode(query))
            return urlunparse(url)

        elif query is not None:  # empty object ok!
            # 2. Form a query string
            return urlencode(query)

        else:
            raise TypeError('needs url, query or both')
