Rocket LMS Translator
=====================

Python3 code to translate language files from Rocket LMS using [Microsoft Translator](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator-text-api/)

### Generate Api Key

Login to your Azure account and create an api key for translation services.

### Insert Api Key and Location

Edit rocketlms-translator.py and insert api key and location of your translation engine instance.

### Execute

```console
python3 rocketlms-translator.py
```

You'll be asked if you want to just debug or not, and to input: language code, source directory of files and destination directory to be created with translated files.
