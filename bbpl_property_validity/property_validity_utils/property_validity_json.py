# SPDX-FileCopyrightText: Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  https://github.com/xavier150/BBPL
# ----------------------------------------------

import json
from typing import List, Optional, Any, cast

import bpy

from . import property_validity_basics
from ..property_validity_class import PropertyCheckData

def _check_modifier_json(
    property_check: PropertyCheckData, 
    value: str
) -> Optional[object]:
    """Checks if a string is a valid JSON. Returns the parsed JSON object if valid, None otherwise."""

    if value == "":
        property_check.add_error("Json value is Empty!")
        return None
    try:
        jdata = json.loads(value)
        return jdata
    except ValueError:
        property_check.add_error("Json not valid: "+str(ValueError))
        return None

def check_is_a_valid_json_string(
    property_check: PropertyCheckData, 
    value: str
) -> bool:
    """Checks if a string is a valid JSON string. Returns True if the bone exists, False otherwise."""

    return _check_modifier_json(property_check, value) is not None

def _check_and_get_json_list(
    property_check: PropertyCheckData, 
    value: str
) -> Optional[List[Any]]:

    json_result = _check_modifier_json(property_check, value)

    if not json_result:
        return None
    
    if not isinstance(json_result, list):
        property_check.add_error("Json not a list: " + str(json_result))
        return None
    
    return cast(List[Any], json_result)

def _check_and_get_json_string_list(
    property_check: PropertyCheckData, 
    value: str
) -> Optional[List[str]]:
    """Checks if a string is a valid JSON list of strings. Returns the parsed list if valid, None otherwise."""

    json_list = _check_and_get_json_list(property_check, value)
    if not json_list:
        return None
    
    has_error = False
    for x, o in enumerate(json_list):
        if not isinstance(o, str):
            property_check.add_error(f"Index {str(x)} is not a String (str): {str(o)}")
            has_error = True
        elif o == "":
            property_check.add_warning(f"Index {str(x)} is empty!")
    if has_error:    
        return None

    return json_list

def check_json_string_list(
    property_check: PropertyCheckData, 
    value: str
) -> bool:
    """Checks if a string is a valid JSON list of strings. Returns True if the list is valid, False otherwise."""

    json_list = _check_and_get_json_string_list(property_check, value)

    if not json_list:
        return False
    return True

def check_json_string_list_in_list(
    property_check: PropertyCheckData, 
    value: str,
    valid_values: List[str],
    include_list_in_report: bool = True
) -> bool:
    """Checks if a string is a valid JSON list of strings and if all strings are in a list of valid values. Returns True if the list is valid, False otherwise."""

    json_list = _check_and_get_json_string_list(property_check, value)

    if not json_list:
        return False

    has_error = False
    for x, o in enumerate(json_list):
        if o not in valid_values:
            if include_list_in_report:
                property_check.add_error(f'Index {str(x)}: "{o}" is not in list: {valid_values}')
            else:
                property_check.add_error(f'Index {str(x)}: "{o}" is not in list.')
            has_error = True
    if has_error:
        return False

    return True

def check_json_object_list(
    property_check: PropertyCheckData, 
    value: str,
    type: Optional[str] = None
) -> bool:
    """Checks if a string is a valid JSON list of objects. Returns True if the list is valid, False otherwise."""

    json_list = _check_and_get_json_string_list(property_check, value)

    if not json_list:
        return False
    
    has_error = False
    for o in json_list:
        if o not in bpy.context.scene.objects:
            property_check.add_error(f'"{str(o)}" not found in scene objects.')
            has_error = True
        else:
            if type:
                obj = bpy.context.scene.objects[o]
                if obj.type != type:
                    property_check.add_error(f'"{str(o)}" is not of type {str(type)}.')
                    has_error = True

    if has_error:    
        return False

    return True


def check_armature_and_json_bone_list_exist(
    property_check: PropertyCheckData, 
    armature: Optional[bpy.types.Object], 
    value: str
) -> bool:
    json_list = _check_and_get_json_string_list(property_check, value)
    if not json_list:
        return False
        
    property_validity_basics.check_armature_and_bone_list_exist(property_check, armature, json_list)
    return True