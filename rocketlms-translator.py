from translate import Translator
import os

lang = input("Enter language code that you want to translate to: ")
translator = Translator(to_lang=lang)


diretorio_entrada = input("Enter source directory: ")
diretorio_saida = input("Enter destination directory (to be created): ")

for r, d, f in os.walk(diretorio_entrada):
    root = r.replace(diretorio_entrada,"")
    print('creating directory '+diretorio_saida+root)
    if not os.path.exists(diretorio_saida+root):
        os.mkdir(diretorio_saida+root)
    for file in f:
        print('translating file '+file)
        with open(r+'/'+file,'r') as f1:
            with open(diretorio_saida+root+'/'+file,'w') as f2:
                for line in f1:
                    parts = line.split('=>')
                    if len(parts) > 1:
                        phrase = parts[1].strip().replace("'","")[0:-1]
                        #traduzida = translator.translate(phrase)
                        #print(traduzida)
                        #line.replace(phrase,traduzida)
                    f2.write(line)

