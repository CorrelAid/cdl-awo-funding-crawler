﻿# config/settings.py

BASE_URL = 'https://www.foerderdatenbank.de/SiteGlobals/FDB/Forms/Suche/Foederprogrammsuche_Formular.html?cl2Processes_Foerdergebiet=_bundesweit&filterCategories=FundingProgram'
CACHE_NAME = 'data/cache/foerderdatenbank_cache'
CACHE_BACKEND = 'sqlite'
CACHE_EXPIRE = None
MAX_PAGES = 5
SLEEP_INTERVAL = 30  # Sekunden
OUTPUT_FILE = 'data/output.json'
LOG_FILE = 'logs/crawler.log'
