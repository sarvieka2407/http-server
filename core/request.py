class HTTPRequest:
    def __init__(
        self,
        method,
        path,
        version,
        headers,
        body,
        query_params,
    ):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers
        self.body = body
        self.query_params = query_params

    def __repr__(self):
        return (
            f"HTTPRequest("
            f"method={self.method!r}, "
            f"path={self.path!r}, "
            f"version={self.version!r}, "
            f"headers={self.headers!r}, "
            f"query_params={self.query_params!r}, "
            f"body={self.body!r})"
        )