from translate import Translator
import os


debug = input("Translate api has a limit for a period, so this script will run in debug mode unless you type 'y': ")

lang = input("Enter language code that you want to translate to: ")
translator = Translator(to_lang=lang)


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
                            translated = translator.translate(phrase)
                            #print(phrase+" --> "+translated)
                            aux = line.replace(phrase,translated)
                    else:
                        aux = line
                    f2.write(aux)

