#use cases in Devops
#dICTIONARIES can save configurations settings for application or settings
config={
    "hostname":"algun servidor",
    "port":8080,
    "username":"user",
    "pwd":"password"
}
#print(config["hostname"])
#Dictionaries can save environment variables for setting up deployment pipelines
environment={
    "database_url":"alguna BD",
    "API_KEY":"abc2secreto",
    "Debug":True
}
#Dictionaries Handle API responses like form DevOps tools
API_Response= {
    "status":"success",
    "data":{
        "server":"alguno",
        "uptime":3600
    }
}
print(API_Response["data"]["server"])

#Dictionaries can also manage infra like AWS EC2 instances or IP addresses
servers ={
    "webserver":{"ip":"192.1.6.8",
                 "role":"frontend"
                 },
    "db":       {"ip":"192.1.6.9",
                 "role":"database"
                 }      
        }
