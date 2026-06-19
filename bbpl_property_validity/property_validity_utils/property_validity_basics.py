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

def check_string_in_list(
    property_check: PropertyCheckData, 
    value: str, 
    valid_values: list[str],
    include_list_in_report: bool = True
) -> bool:
    """Checks if a string is in a list of valid values. Returns True if the string is in the list, False otherwise."""
    
    if value not in valid_values:
        if include_list_in_report:
            property_check.add_error(f'String "{value}" is not in list: {valid_values}')
        else:
            property_check.add_error(f'String "{value}" is not in list.')
        return False
    return True

def check_string_list_in_list(
    property_check: PropertyCheckData, 
    values: list[str], 
    valid_values: list[str],
    include_list_in_report: bool = True
) -> bool:
    """Checks if all strings in a list are in a list of valid values. Returns True if all strings are in the list, False otherwise."""
    
    has_error = False
    for value in values:
        if value not in valid_values:
            has_error = True
            if include_list_in_report:
                property_check.add_error(f'String "{value}" ({values.index(value)}) is not in list: {valid_values}')
            else:
                property_check.add_error(f'String "{value}" ({values.index(value)}) is not in list.')
    return not has_error

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

def check_armature_and_bone_list_exist(
    property_check: PropertyCheckData, 
    armature: Optional[bpy.types.Object], 
    bone_names: list[str]
) -> bool:
    """Checks if an armature exists and contains a list of specific bones. Returns True if the armature exists and contains all the bones, False otherwise."""
    
    if armature is None:
        property_check.add_error("Armature is None.")
        return False
    if not isinstance(armature.data, bpy.types.Armature):
        property_check.add_error(f"Object {armature.name} is not an armature.")
        return False
    has_error = False
    for bone_name in bone_names:
        if bone_name not in armature.data.bones:
            property_check.add_error(f'Bone "{bone_name}" not found in {armature.name}.')
            has_error = True
    if has_error:
        return False
    return True