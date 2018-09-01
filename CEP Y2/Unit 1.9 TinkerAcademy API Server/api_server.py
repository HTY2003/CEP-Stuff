from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json
import string
import random
import sqlite3

# Python dict that we will convert to a JSON-formatted string
message_dict = {
    "business": "Pizza Hut",
    "founded": 2010, # Bogus date
    "locations": [
        "Pasir Ris",
        "Tampines",
        "Bishan",
        "Toa Payoh",
        "Orchard" # And everywhere else
    ]
}

# Initialise db at the start of program
def db_init():
    db = sqlite3.connect("auth.db")
    db.execute("""CREATE TABLE IF NOT EXISTS keys
                (key text, status integer,
                quota integer, used integer)""")
    db.commit()
    db.close()
    
# Generate new key
def keygen(length=32):
    charspace = string.ascii_letters + string.digits
    gen = ""
    for _ in range(length):
        gen += random.choice(charspace)
    return gen

# Generate a new key, insert into db, and return key
def db_keygen():
    newkey = keygen()
    t = (newkey,)
    db = sqlite3.connect("auth.db")
    db.execute("INSERT INTO keys VALUES (?, 1, 10, 0)", t)
    db.commit()
    db.close()
    return newkey

# Check if key is valid
def auth_key(key):
    t = (key,)
    db = sqlite3.connect("auth.db")
    for row in db.execute("SELECT * FROM keys WHERE key = ?", t):
        db.close()
        return True
    db.close()
    return False

# Create a subclass to attach HTTP method handlers
class api_handler(BaseHTTPRequestHandler):
	
    # GET method handler (generate new key)
    def do_GET(self):
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        # Generate new key, insert into db, return key
        newkey = db_keygen()

        # Return the key in the response
        self.wfile.write(bytes(newkey, "utf8"))
        
        return
    
    # POST method handler (fetch API data)
    def do_POST(self):

        # Get data from input stream
        data = self.rfile.read(int(self.headers.get("Content-length"))).decode("utf-8")
        data = urllib.parse.parse_qs(data)
        key = data["key"][0]
        print("key = " + key)

        # Check validity of key
        key_valid = auth_key(key)
        print("key valid = " + str(key_valid))

        if(key_valid):
            # Send 200 OK and the API data
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(message_dict), "utf8"))
        else:
            # Send 403 Forbidden with a message
            self.send_response(403, "API key is invalid")
            self.end_headers()
        return

def run(server_class=HTTPServer, handler_class=api_handler):
    print('starting server...')

    # Server settings
    # Run server in localhost on port 8080
    server_address = ("localhost", 8080)
    httpd = server_class(server_address, handler_class)
    
    print('running server...')
    db_init()
    httpd.serve_forever()
    
run()
