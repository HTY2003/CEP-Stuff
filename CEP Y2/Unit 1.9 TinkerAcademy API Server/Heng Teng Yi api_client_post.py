import urllib.request

data = {}

def access_server(server, key, admin_key = None, upload_data = None):
    data["key"] = key
    if admin_key is not None:
        data["admin_key"] = admin_key
    if upload_data is not None:
        data["upload_data"] = upload_data
    
    data_enc = urllib.parse.urlencode(data).encode("utf8")
    headers = { "Content-type" : "application/x-www-form-urlencoded",
            "Content-length" : len(data_enc) }
    
    request = urllib.request.Request(server, data_enc, headers, method="POST")
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
#--------ALL POSSIBLE FUNCTIONS------------------
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr")       #correct key
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr" + "Wrong key")# wrong key
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtenyi")  # wrong Admin key
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtengyi") #correct Admin key and normal key
#uploading to existing keys in response_dict
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtengyi",{"Pizza Hut":{"founded": 2003, "locations": ["Orchard", "Bukit Batok", "Jurong"]}})
# no Admin key given
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", upload_data = {"Domino's Pizza":{"founded": 2003, "locations": ["Orchard", "Bukit Batok", "Jurong"]}})
# uploading to new keys in response_dict
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtengyi",{"Domino's Pizza":{"founded": 2003, "locations": ["Orchard", "Bukit Batok", "Jurong"]}})

#fodder functions
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtengyi",{"Domino's Pizza":{"founded": 2003, "locations": ["Orchard", "Bukit Batok", "Jurong"]}})
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtengyi",{"Domino's Pizza":{"founded": 2003, "locations": ["Orchard", "Bukit Batok", "Jurong"]}})
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtengyi",{"Domino's Pizza":{"founded": 2003, "locations": ["Orchard", "Bukit Batok", "Jurong"]}})
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtengyi",{"Domino's Pizza":{"founded": 2003, "locations": ["Orchard", "Bukit Batok", "Jurong"]}})

#key exceeded use limit and has been erased
#access_server("http://localhost:8080","jeJDA3Oiz6Av6JENTUMYYZ2sL91OIvHr", "hengtengyi",{"Domino's Pizza":{"founded": 2003, "locations": ["Orchard", "Bukit Batok", "Jurong"]}})

#Test the functions individually
