import importlib
from illogic.common import utils

utils.unload_packages(silent=True, package="illogic.mAIrus")
importlib.import_module("illogic.mAIrus.MAIrus")
from mAIrus.MAIrus import MAIrus
try:
    mAIrus_tool.close()
except:
    pass

# ##################################################################################################################

# TODO Put your OpenAI API key here
__PATH_TO_OPENAI_KEY = 'PATH/TO/openai_key'

# ##################################################################################################################

mAIrus_tool = MAIrus(__PATH_TO_OPENAI_KEY)
mAIrus_tool.show()
