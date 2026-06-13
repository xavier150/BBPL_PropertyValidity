# SPDX-FileCopyrightText: Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  https://github.com/xavier150/BBPL
# ----------------------------------------------

import importlib

import bpy

from . import property_validity_class
from . import property_validity_utils

if "property_validity_class" in locals():
    importlib.reload(property_validity_class)
if "property_validity_utils" in locals():
    importlib.reload(property_validity_utils)


# -------------------------------------------------------------------
#   Register & Unregister
# -------------------------------------------------------------------

classes = (
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)  # type: ignore

    property_validity_class.register()

def unregister():
    property_validity_class.unregister()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)  # type: ignore