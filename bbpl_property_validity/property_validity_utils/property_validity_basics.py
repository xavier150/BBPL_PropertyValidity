# SPDX-FileCopyrightText: Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  https://github.com/xavier150/BBPL
# ----------------------------------------------

from typing import Optional

import bpy

from ..property_validity_class import PropertyCheckData


def check_string_not_empty(
    property_check: PropertyCheckData, 
    value: str
) -> bool:
    """Checks if a string is not empty. Returns True if the string is not empty, False otherwise."""
    
    if value == "":
        property_check.add_error("String is empty!")
        return False
    return True

def check_bone_exist(
    property_check: PropertyCheckData, 
    armature: bpy.types.Object, 
    bone_name: str
) -> bool:
    """Checks if a bone exists in an armature. Returns True if the bone exists, False otherwise."""
    
    if not isinstance(armature.data, bpy.types.Armature):
        property_check.add_error(f"Object {armature.name} is not an armature.")
        return False
    if bone_name not in armature.data.bones:
        property_check.add_error(f"Bone {bone_name} not found in {armature.name}.")
        return False
    return True

def check_armature_and_bone_exist(
    property_check: PropertyCheckData, 
    armature: Optional[bpy.types.Object], 
    bone_name: str
) -> bool:
    """Checks if an armature exists and contains a specific bone. Returns True if the armature exists and contains the bone, False otherwise."""
    
    if armature is None:
        property_check.add_error("Armature is None.")
        return False
    if not isinstance(armature.data, bpy.types.Armature):
        property_check.add_error(f"Object {armature.name} is not an armature.")
        return False
    if bone_name not in armature.data.bones:
        property_check.add_error(f"Bone {bone_name} not found in {armature.name}.")
        return False
    return True