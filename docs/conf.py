# docs/conf.py
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent / "cosmobewi-shared"))

from conf_shared import *     # shared theme & config
include_local_paths(__file__) # enable local overrides