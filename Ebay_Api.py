import apikey_storage
import requests
def ebay_finding_api_request(keywords, api_key):
    endpoint = 'https://svcs.ebay.com/services/search/FindingService/v1'
    operation = 'findItemsByKeywords'
    url = f"{endpoint}?OPERATION-NAME={operation}&SERVICE-VERSION=1.0.0&SECURITY-APPNAME={api_key}&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords={keywords}"

    try:
        response = requests.get(url)
        if response.status_code ==200:
            Incoming_Data = response.json()
            Items = Incoming_Data.get("findItemsByKeywordsResponse")
            with open('storage.txt', 'w',encoding='utf-8') as file:
                for i in Items:
                    file.write(str(i))
                    
                
        else:
            print(f"Status code = {response.status_code}")

    except Exception as E:
        print(f"An Error has occured: {E}")

ebay_finding_api_request("Headphones",apikey_storage.app_id)
