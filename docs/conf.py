# docs/conf.py
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent / "cosmobewi-shared"))

from conf_shared import *     # shared theme & config


import importlib.util

# charger pdv-to-lambda/conf.py
spec2 = importlib.util.spec_from_file_location("pdv_conf", Path(__file__).parent / "pdv-to-lambda" / "conf.py")
pdv_conf = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(pdv_conf)

# hérite des variables
extensions = extensions + pdv_conf.extensions
bibtex_bibfiles = pdv_conf.bibtex_bibfiles

