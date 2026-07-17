
class HTTPResponse:
    def __init__(
        self,
        status_code=200,
        reason="OK",
        headers=None,
        body="",
    ):
        self.status_code = status_code
        self.reason = reason
        self.headers = headers if headers is not None else {}
        self.body = body

    def to_bytes(self):
        status_line = f"HTTP/1.1 {self.status_code} {self.reason}\r\n"

        self.headers["Content-Length"] = str(len(self.body.encode()))

        headers = ""

        for key, value in self.headers.items():
            headers += f"{key}: {value}\r\n"

        response = (
            status_line +
            headers +
            "\r\n" +
            self.body
        )

        return response.encode()

    