import importlib
from illogic.common import utils

utils.unload_packages(silent=True, package="illogic.nuke_scanner")
importlib.import_module("illogic.nuke_scanner")
from nuke_scanner.NukeScanner import NukeScanner
NukeScanner().run()