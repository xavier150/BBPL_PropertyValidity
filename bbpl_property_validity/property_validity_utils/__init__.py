# SPDX-FileCopyrightText: Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  https://github.com/xavier150/BBPL
# ----------------------------------------------

import importlib

from .property_validity_basics import *
from .property_validity_json import *

if "property_validity_basics" in locals():
    importlib.reload(property_validity_basics)
if "property_validity_json" in locals():
    importlib.reload(property_validity_json)



