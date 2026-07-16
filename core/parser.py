from core.request import HTTPRequest
from urllib.parse import parse_qs

# urllib.parse is a built-in Python module used for breaking Uniform Resource Locator (URL) strings down into components or combining them back together
# parse_qs (found in the urllib.parse module) parses a URL query string into a dictionary. It maps each parameter name to a list of values.

def parse_request(raw_request):
    print("Inside parser")
    lines = raw_request.split("\r\n") # In the world of networking and computing, \r\n represents a newline 

# PARSING REQUEST_LINE: 
    request_line = lines[0] # the first line is the request line 

    method, full_path, version = request_line.split() 

    """
    request_line : GET /echo?message=hello HTTP/1.1
    method => GET
    full_path => /echo?message=hello
    version => HTTP/1.1 

    """

    if '?' in full_path:
        path, query_string = full_path.split("?", 1) # ["/echo", "message=hello"] , '1' means python stops spliting after the first '?'

        query_params = {
            key: value[0]
            for key, value in parse_qs(query_string).items()
        }

        """
        query_string : message=hello&name=sarvika
        eg) ?tag=python&tag=http => "tag" : ["python" , "http"]

        {
            "message": ["hello"],
            "name": ["sarvika"]
        }
        
        """


    else:
        path = full_path
        query_params = {}

    #print(f"Method  : {method}")
    #print(f"Path    : {full_path}")
    #print(f"Version : {version}")
    #print("Query Params:", query_params)


# PARSING HEADERS: 
    # header = lines[1] # we cannot do this, as we might have more than 1 headers, so we can create an empty dictionary in python 


    """
    # if request is:
    GET /echo?message=hello HTTP/1.1 (line 0)
    Host: 127.0.0.1:8080 (line 1)
    User-Agent: curl/8.7.1 (line 2)
    Accept: */* (line 2)

    # headers become: 
    {
    "Host": "127.0.0.1:8080",
    "User-Agent": "curl/8.7.1",
    "Accept": "*/*"
    }
    """
    
    headers = {}

    i = 1

    while i < len(lines) and lines[i] != "":  # while i is less than than length of lines and and there is no blank line, as after the blank line the body starts 

        key, value = lines[i].split(":", 1)

        headers[key.strip()] = value.strip() # headers[key] = value ; key : value pairs in the dictionary 

        i += 1

    #print(headers)

# PARSING BODY: 
    body = "\r\n".join(lines[i + 1:])
    #print(f"Body: {body}")


    request = HTTPRequest(
    method=method,
    path=path,
    version=version,
    headers=headers,
    body=body,
    query_params=query_params,
)


    return request


