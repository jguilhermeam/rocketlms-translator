import requests, uuid, json, os

def translate(src_text,lang):
    subscription_key = ""
    location = ""
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"

    params = {
        'api-version': '3.0',
        'to': lang
    }

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{ 'text': src_text }]

    request = requests.post(endpoint, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']


debug = input("Translate api has a limit for a period, so this script will run in debug mode unless you type 'y': ")

lang = input("Enter language code that you want to translate to: ")

source_dir = input("Enter source directory: ")
dest_dir = input("Enter destination directory (to be created): ")

for r, d, f in os.walk(source_dir):
    root = r.replace(source_dir,"")
    print('creating directory '+dest_dir+root)
    if not os.path.exists(dest_dir+root):
        os.mkdir(dest_dir+root)
    for file in f:
        print('translating file '+file)
        with open(r+'/'+file,'r') as f1:
            with open(dest_dir+root+'/'+file,'w') as f2:
                for line in f1:
                    parts = line.split("=>")
                    if len(parts) > 1:
                        phrase = parts[1].strip().replace("'","").replace("\"","")[0:-1]
                        if debug.lower() == 'y':
                            translated = translate(phrase,lang)
                            #print(phrase+" --> "+translated)
                            aux = line.replace(phrase,translated)
                        else:
                            aux = 'TRANSLATE WILL BE HERE'
                    else:
                        aux = line
                    f2.write(aux)
