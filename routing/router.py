# links a combination of an HTTP Method and a URL Path to a specific action (handler).
from core.response import HTTPResponse

class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, method, path, handler):
        self.routes[(method, path)] = handler

# This code implements the lookup and dispatch logic of your router. 
# It takes an incoming request, checks if the server knows how to handle that request, and if so, runs the appropriate function.

# This method takes a request object (which contains parsed data like request.method and request.path) as its input.
# route = (request.method, request.path)

    def handle(self, request):
        route = (request.method, request.path)

        print("Requested route:", route)
        print("Available routes:", self.routes)

        if route not in self.routes:
            return None

        handler = self.routes[route]

        return handler(request)


# ------------------ Handler Functions ------------------

def home_handler(request):
        return HTTPResponse(
            status_code=200,
            reason="OK",
            headers={
                "Content-Type": "text/plain"
            },
            body="Welcome to the Home Page"
        )


def echo_handler(request):
        return HTTPResponse(
            status_code=200,
            reason="OK",
            headers={
                "Content-Type": "text/plain"
            },
            body="Echo Endpoint"
        )


# ------------------ Dummy Request ------------------

class DummyRequest:
    def __init__(self, method, path):
        self.method = method
        self.path = path


# ------------------ Testing ------------------

if __name__ == "__main__":

    router = Router()

    router.add_route("GET", "/", home_handler)
    router.add_route("GET", "/echo", echo_handler)

    request = DummyRequest("GET", "/abc")

    response = router.handle(request)

    if response is None:
        print(" ⚠️ This route is not available")
    else:
        print(response.status_code)
        print(response.reason)
        print(response.headers)
        print(response.body)


# __init__: Short for "initialize". The double underscores tell Python: "Hey, this is a built-in special engine method. Don't make the programmer call this manually; run it automatically behind the scenes."
# self: This represents the specific object that is currently being created.

# my_router = Router()
#Python instantly and automatically does this behind the scenes:
#1. It creates a brand-new, empty Router object.
#2. It jumps inside __init__.
#3. It treats self as your new my_router variable.
#4. It executes my_router.routes = {}.
