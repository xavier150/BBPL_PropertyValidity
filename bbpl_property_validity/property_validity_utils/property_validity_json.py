# SPDX-FileCopyrightText: Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  https://github.com/xavier150/BBPL
# ----------------------------------------------

import json
from typing import List, Optional, Any, cast

from ..property_validity_class import PropertyCheckData

def _check_modifier_json(property_check: PropertyCheckData, value: str) -> Optional[object]:
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

def check_is_a_valid_json_string(property_check: PropertyCheckData, value: str) -> bool:
    """Checks if a string is a valid JSON string. Returns True if the bone exists, False otherwise."""

    return _check_modifier_json(property_check, value) is not None

def check_json_string_list(property_check: PropertyCheckData, value: str) -> bool:
    """Checks if a string is a valid JSON list of strings. Returns True if the list is valid, False otherwise."""

    json_result = _check_modifier_json(property_check, value)

    if not json_result:
        return False
    
    if not isinstance(json_result, list):
        property_check.add_error("Json not a list: " + str(json_result))
        return False

    json_list = cast(List[Any], json_result)
    for x, o in enumerate(json_list):
        if not isinstance(o, str):
            property_check.add_error(f"Index {str(x)} is not a String (str): {str(o)}")
            return False
        elif o == "":
            property_check.add_error(f"Index {str(x)} is empty!")
            return False

    return True