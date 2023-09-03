import importlib
from illogic.common import utils

utils.unload_packages(silent=True, package="illogic.asset_loader")
importlib.import_module("illogic.asset_loader")
from illogic.asset_loader.AssetLoader import AssetLoader
try:
    app.close()
except:
    pass
app = AssetLoader()
app.show()

