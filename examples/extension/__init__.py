from . import ${PROJECT_NAME} as ext
from extensions import EXTENSION_REGISTRY_MD, EXTENSION_REGISTRY_TD
EXTENSION_REGISTRY_MD.register_extension('kfextdemo', ext.MD)
EXTENSION_REGISTRY_TD.register_extension('kfextdemo', ext.TD)

import extensions
import kungfu.extension as kfext

@kfext.command(help='test ext')
def test(args, logger):
    print('hello kungfu')
