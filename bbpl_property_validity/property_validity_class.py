# SPDX-FileCopyrightText: Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  https://github.com/xavier150/BBPL
# ----------------------------------------------

from typing import List

import bpy

class PropertyCheckData():
    """Collects property validation messages (info, warnings, errors)."""

    def __init__(self):
        self.info_texts: List[str] = []
        self.warning_texts: List[str] = []
        self.error_texts: List[str] = []

    def add_info(self, text: str) -> None:
        """Adds an info message."""
        self.info_texts.append(text)

    def add_warning(self, text: str) -> None:
        """Adds a warning message."""
        self.warning_texts.append(text)

    def add_error(self, text: str) -> None:
        """Adds an error message."""
        self.error_texts.append(text)

    def get_contains_infos(self) -> bool:
        """Returns True when at least one info message exists."""
        return len(self.info_texts) > 0
    
    def get_contains_warnings(self) -> bool:
        """Returns True when at least one warning message exists."""
        return len(self.warning_texts) > 0

    def get_contains_errors(self) -> bool:
        """Returns True when at least one error message exists."""
        return len(self.error_texts) > 0

    def draw_check_report(self, layout: bpy.types.UILayout) -> None:
        for error_text in self.error_texts:
            layout.label(text=error_text, icon="ERROR")
        for warning_text in self.warning_texts:
            layout.label(text=warning_text, icon="CANCEL")
        for info_text in self.info_texts:
            layout.label(text=info_text, icon="INFO")


# -------------------------------------------------------------------
#   Register & Unregister
# -------------------------------------------------------------------

classes = (
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)  # type: ignore

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)  # type: ignore