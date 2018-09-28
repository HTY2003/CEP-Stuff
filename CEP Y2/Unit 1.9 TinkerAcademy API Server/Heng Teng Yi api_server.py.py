from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import string
import random
import sqlite3
import urllib.parse

admin_password = "hengtengyi"
# non-random password for admin use

response_dict = {"Pizza Hut":{
             "founded": 2010,
             "locations": [
             "Pasir Ris",
             "Tampines",
             "Bishan",
             "Toa Payoh",
             "Orchard" # yay fake data!
             ]}}

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
    db.execute("""CREATE TABLE IF NOT EXISTS data
                (business text, founded integer,
                location text)""")
    #uploads data to table
    for key in response_dict.keys():
        for loc in response_dict[key]["locations"]:
            data = (key,response_dict[key]["founded"],loc)
            db.execute("INSERT into data VALUES(?,?,?)", data)
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
        key_valid = auth_key(key)
        print("Key Valid = " + str(key_valid))
        # Checks key validity
        if(key_valid):
            used = db.execute("""SELECT quota, used FROM keys WHERE key = ?""",(key,))
            for row in used:
                # Checks if use quota of key has been exceeded
                if row[1] < row[0]:
                    keydata = (key, row[1] + 1)
                    db.execute("""DELETE from keys WHERE key = ?""",(key,))
                    db.execute("""INSERT into keys VALUES (?, 1, 10, ?)""", keydata)
                    for row in db.execute("""SELECT * FROM keys WHERE key = ?""",(key,)):
                        print(row)
                        
                    # Checks if there is data to upload
                    if "upload_data" in data.keys():
                        upload_dict =  eval(data["upload_data"][0])
                    else:
                        upload_dict = None
                        
                    if "admin_key" in data.keys():
                        admin_key = data["admin_key"][0]
                        print("Admin API Key = " + admin_key)
                        if admin_key == admin_password:                    
                            print("Admin API Key Valid = " + str(True))
                            if upload_dict is not None:
                                    for key in upload_dict.keys():
                                        # Adds data to table and dictionary
                                        # Data already in API data will not be uploaded to prevent repeats
                                        if key in response_dict.keys():
                                            for loc in upload_dict[key]["locations"]:
                                                if loc not in response_dict[key]["locations"]:
                                                    response_dict[key]["locations"].append(loc)
                                                    data = (key, response_dict[key]["founded"], loc)
                                                    db.execute("""INSERT into data VALUES(?,?,?)""", data)
                                            # Send 200 OK with no data
                                            self.send_response(200,"Data uploaded")
                                            self.end_headers()
                                            
                                        else:
                                            response_dict[key] = {"founded": upload_dict[key]["founded"], "locations": upload_dict[key]["locations"]}
                                            for loc in upload_dict[key]["locations"]:
                                                data = (key, upload_dict[key]["founded"], loc)
                                                db.execute("""INSERT into data VALUES(?,?,?)""", data)
                                            # Send 200 OK with no data
                                            self.send_response(200,"Data uploaded")
                                            self.end_headers()
                                            
                            else:
                                # Send 200 OK and the API data
                                self.send_response(200)
                                self.send_header("Content-type","application/json")
                                self.end_headers()
                                self.wfile.write(bytes(json.dumps(response_dict), "utf8"))
                                
                        else:
                            # Send 403 Forbidden with a message
                            print("Admin Key Valid = " + str(False))
                            self.send_response(403, "Admin API Key is invalid. Unable to upload.")
                            self.end_headers()                                
                            
                    elif upload_dict is not None:
                        self.send_response(403, "No Admin API Key provided. Unable to upload.")
                        self.end_headers()
                            
                    else:
                        # Send 200 OK and the API data
                        self.send_response(200)
                        self.send_header("Content-type","application/json")
                        self.end_headers()
                        self.wfile.write(bytes(json.dumps(response_dict), "utf8"))
                           
                else:
                    # Send 403 Forbidden with a message, and deletes API key
                    db.execute("""DELETE from keys WHERE key = ?""",(key,))
                    self.send_response(403, "API Key is invalid")
                    self.end_headers()
                    
        else:
            # Send 403 Forbidden with a message
            self.send_response(403, "API Key is invalid")
            self.end_headers()
        db.commit()
        db.close()

def run(server_class = HTTPServer, handler_class = Handler):
    db = sqlite3.connect("auth.db")
    db.execute("""DELETE from data""")
    db.execute("""DELETE from keys""")
    db.commit()
    db.close()
    db_init()
    APIdata()
    print('starting server') 
    server_address = ("localhost", 8080)
    print('running server...')
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()

'''-------Documentation-------
Step 1: Run the server code to start the server.

Step 2: Run api_client_get.py to obtain an API key.
        
Step 3: Insert the server name and API into access_server() as the first two parameters.

To upload data:
To upload PH locations, enter the admin API key and upload data
into access_server() as additional 3rd and 4th parameters.

The upload data should be phrased as such: {business string:{"founded": year founded integer, "locations": [location strings]}}
                    Multiple businesses example: {business string:{"founded": year founded integer, "locations": [location strings]},
                                                business 2 string:{"founded": year founded 2 integer, "locations": [location 2 strings]}}
                                                
To read data:
To see the server data, do not enter any more parameters into the function.

Step 4: Run api_client_post.py to achieve your desired result.

-----------GUIDELINES------------

1) Data already stored in server cannot be uploaded to server.(No repeat data)

2) API keys can only be used 10 times before being invalid.

3) All data tables(keys and data) are reset to default when the server is restarted.

4) If you have the correct API Key but wrong Admin API key, you will receive a 403 Error no matter what.

5) For founding years already determined, e.g. Pizza Hut founded in 2010, the "founded" key in the data is unnesseccary and will be ignored. It can be omitted.
    But for new business added, the "founded" key is required.
'''
