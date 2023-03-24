import requests
import re

def download_file(download_url, file_name=''):
    req = requests.get(download_url)
    try:
        if file_name:
            pass
        else:
            file_name = req.url[download_url.rfind('/')+1:]
    
        with open(file_name, 'wb') as f:
           for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return file_name
    except Exception as e:
        print(e)
        return None

with open('csv_to_download.txt') as f:
    for url in f:
        url = re.findall('^https://\S+movielens\.csv', url)
        if len(url) < 1:
            continue
        else:
            to_download = url[0]
    #print(to_download)    

download_file(to_download)
print('csv file downloaded')