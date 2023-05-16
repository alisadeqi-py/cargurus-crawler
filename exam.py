import requests
import traceback

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
link = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=&zip=95117'

def get_page(link):
    try:
        response = requests.get(link , headers=headers) 
        print(response)
    except Exception:
        traceback.print_exc()
        return None
    return response

print(get_page(link))