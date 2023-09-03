"""mAIrus - A tool for generating text using OpenAI's GPT-3 API"""

import importlib
from illogic.common import utils




# ##################################################################################################################

# TODO Put your OpenAI API key here
__PATH_TO_OPENAI_KEY = 'PATH/TO/openai_key'

# ##################################################################################################################
if __name__ == "__main__":
    utils.unload_packages(silent=True, package="illogic.mAIrus")
    importlib.import_module("illogic.mAIrus.MAIrus")
    from mAIrus.MAIrus import MAIrus
    try:
        mAIrus_tool.close()
    except:
        pass
    mAIrus_tool = MAIrus(__PATH_TO_OPENAI_KEY)
    mAIrus_tool.show()
