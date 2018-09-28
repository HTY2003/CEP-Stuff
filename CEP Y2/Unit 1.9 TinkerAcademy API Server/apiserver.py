from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import string
import random
import sqlite3
import urllib.parse

admin_password = "hengtengyi"
# non-random password for admin use

response_dict = {
             "business": "Pizza Hut",
             "founded": 2010, # Bogus date
             "locations": [
             "Pasir Ris",
             "Tampines",
             "Bishan",
             "Toa Payoh",
             "Orchard" # ...and everywhere else
             ]
            }

def db_init():
    db = sqlite3.connect("auth.db")
    db.execute("""CREATE
    TABLE IF NOT EXISTS keys (key text, status integer, quota integer,
    used integer)""")
    db.commit()
    db.close()

def keygen(length=32):
       charspace = string.ascii_letters + string.digits
       key = ""
       for _ in range(length):
          key += random.choice(charspace)
       return key

def db_keygen():
     newkey = keygen()
     t = (newkey,)
     db = sqlite3.connect("auth.db")
     db.execute("INSERT INTO keys VALUES (?, 1, 10, 0)", t)
     db.commit()
     db.close()
     return newkey
    
def auth_key(key):
    t = (key,)
    db = sqlite3.connect("auth.db")
    for row in db.execute("SELECT key, quota FROM keys WHERE key = ?", t):
        db.close()
        return True
    db.close()
    return False

def APIdata():
    #creates API data table
    db = sqlite3.connect("auth.db")
    db.execute("""CREATE TABLE IF NOT EXISTS apidata
                (business text, founded integer,
                location text)""")
    #uploads data to table
    for loc in response_dict["locations"]:
        location = (loc,)
        db.execute("""INSERT into apidata VALUES("Pizza Hut",2010,?)""", location)
    db.commit()
    db.close()

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        newkey = db_keygen()
        self.wfile.write(bytes(newkey, "utf8"))

    def do_POST(self):
        db = sqlite3.connect("auth.db")
        data = self.rfile.read(int(self.headers.get("Content-length"))).decode("utf-8")
        data = urllib.parse.parse_qs(data)
        key = data["key"][0]
        print("Key = " + key)
        tukey = (key,)
        key_valid = auth_key(key)
        print("Key valid = " + str(key_valid))
        # Checks key validity
        if(key_valid):
            used = db.execute("SELECT quota, used FROM keys WHERE key = ?", tukey)
            for row in used:
                # Checks if use quota of key has been exceeded
                if row[1] < row[0]:
                    newused = (row[1] + 1,)
                    db.execute("DELETE from keys WHERE key = ?", tukey)
                    db.execute("INSERT into keys VALUES (?, 1, 10, ?)", tukey + newused)
                    for row in db.execute("SELECT * FROM keys WHERE key = ?", tukey):
                        print(row)
                    # Checks if there is data to upload
                    if "upload_data" != None:
                        # Checks if there is an admin key provided
                        if "admin_key" != None:
                            print("Admin API Key = " + admin_key)
                            admin_key = data["admin_key"][0]
                            upload_data = data["upload_data"]
                            # Checks if admin key is valid
                            if admin_key == admin_password:
                                print("Admin API Key valid = " + str(True))
                                # Send 200 OK with no data
                                self.send_response(200,"Data uploaded")
                                self.end_headers()
                                loclist = list(db.execute("SELECT location FROM apidata")
                                for loc in upload_data:
                                    # Adds data to table and dictionary(can be more than 1 string)
                                    # Data already in API data will not be uploaded to prevent repeats
                                    if loc not in loclist:
                                        response_dict["locations"].append(loc)
                                        db.execute("""INSERT into apidata VALUES("Pizza Hut",2010,?)""", (loc,))
                            else:
                                # Send 403 Forbidden with a message
                                print("admin key valid = " + str(False))
                                self.send_response(403, "Admin API Key is invalid")
                                self.end_headers()
                        else:
                            # Send 403 Forbidden with a message
                            self.send_response(403, "No Admin API Key provided")
                            self.end_headers()
                    else:
                        # Send 200 OK and the API data
                        self.send_response(200)
                        self.send_header("Content-type","application/json")
                        self.end_headers()
                        self.wfile.write(bytes(json.dumps(response_dict), "utf8"))
                else:
                    # Send 403 Forbidden with a message, and deletes API key
                    db.execute("DELETE * from keys WHERE key = ?", tukey)
                    self.send_response(403, "API Key is invalid")
                    self.end_headers()
        else:
            # Send 403 Forbidden with a message
            self.send_response(403, "API Key is invalid")
            self.end_headers()
        db.commit()
        db.close()

def run(server_class = HTTPServer, handler_class = Handler):
    db_init()
    APIdata()
    print('starting server')
    db = sqlite3.connect("auth.db")
    db.execute("DELETE from keys")
    db.execute("DELETE from apidata")
    db.commit()
    db.close()
    server_address = ("localhost", 8080)
    print('running server...')
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()

'''-------Documentation-------
Step 1: Run the server code to run the server.

Step 2: Insert the server name into access_key()
        and run api_client_get.py to obtain an API key.
        
Step 3: Insert the server name and API into access_server() as parameters.

To upload:
To upload PH locations, enter the admin API key and upload data
into access_server() as parameters.

To read data:
To see the server data, do not enter any parameters into the function.

Step 4: Run api_client_post.py to achieve your desired result.

---------GUIDELINES------------

1) Data already stored in server cannot be uploaded to server

2) API key can only be used 10 times before being invalid
'''
