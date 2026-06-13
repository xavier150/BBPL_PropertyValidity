# SPDX-FileCopyrightText: Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  https://github.com/xavier150/BBPL
# ----------------------------------------------

import bpy

from ..property_validity_class import PropertyCheckData


def check_bone_exist(property_check: PropertyCheckData, armature: bpy.types.Object, bone_name: str) -> bool:
    """Checks if a bone exists in an armature. Returns True if the bone exists, False otherwise."""
    if isinstance(armature.data, bpy.types.Armature):
        if bone_name not in armature.data.bones:
            property_check.add_error(f"Bone {bone_name} not found in {armature.name}.")
    else:
        property_check.add_error(f"Object {armature.name} is not an armature.")
    return False