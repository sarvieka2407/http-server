# why do we need a config file? 
# As this project grows, multiple files (like your server, your router, your logger, or your test scripts) will need to know what host and port the server is running on. 
# Instead of hardcoding 8080 in five different files, you define it once. 
# If you want to switch to port 9090, you change it in exactly one place.

PORT = 8080
HOST = "127.0.0.1"