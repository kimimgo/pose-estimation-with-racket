import requests
from getfilelistpy import getfilelist

API_KEY = '###'  # Please set your API key.
FOLDER_ID = '###'  # Please set the folder ID.

resource = {
    "api_key": API_KEY,
    "id": FOLDER_ID,
    "fields": 'nextPageToken, files(id,name,webContentLink,mimeType)',
}
res = getfilelist.GetFileList(resource)
for files in res['fileList']:
    for file in files['files']:
        if 'google' not in file['mimeType']:
            filename = file['name']
            print('%s is downloading.' % filename)
            r = requests.get(file['webContentLink'], stream=True)
            if r.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(r.content)