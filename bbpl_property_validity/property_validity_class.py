# SPDX-FileCopyrightText: Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  https://github.com/xavier150/BBPL
# ----------------------------------------------

from typing import List, Literal
import enum

import bpy



class PropertyCheckResultType(enum.Enum):
    """Enum for property check results."""
    INFO = 0
    WARNING = 1
    ERROR = 2

    def get_icon(self) -> Literal["INFO", "ERROR", "CANCEL"]:
        """Returns the corresponding Blender icon for the result type."""

        # In Blender ERROR icon is just "/!\", and CANCEL icon is (X).
        # So I preffer to use CANCEL for errors and ERROR for warnings.
        if self.value == PropertyCheckResultType.INFO.value:
            return "INFO"
        elif self.value == PropertyCheckResultType.WARNING.value:
            return "ERROR"
        else:
            return "CANCEL"


class PropertyTypedResult():

    def __init__(self, type: PropertyCheckResultType, texts: List[str]):
        self.result_type: PropertyCheckResultType = type
        self.texts: List[str] = texts

    def is_info(self) -> bool:
        return self.result_type.value == PropertyCheckResultType.INFO.value
    
    def is_warning(self) -> bool:
        return self.result_type.value == PropertyCheckResultType.WARNING.value
    
    def is_error(self) -> bool:
        return self.result_type.value == PropertyCheckResultType.ERROR.value

    def draw_result(self, layout: bpy.types.UILayout) -> bpy.types.UILayout:
        grouped_text = layout.column()
        for x, text in enumerate(self.texts):
            if x == 0:
                grouped_text.label(text=text, icon=self.result_type.get_icon())
            else:
                grouped_text.label(text=text)

        return grouped_text

class PropertyCheckData():
    """Collects property validation messages (info, warnings, errors)."""

    def __init__(self):
        self.results: List[PropertyTypedResult] = []

    def add_info(self, text: str) -> None:
        """Adds an info message."""
        self.results.append(PropertyTypedResult(PropertyCheckResultType.INFO, [text]))

    def add_warning(self, text: str) -> None:
        """Adds a warning message."""
        self.results.append(PropertyTypedResult(PropertyCheckResultType.WARNING, [text]))

    def add_error(self, text: str) -> None:
        """Adds an error message."""
        self.results.append(PropertyTypedResult(PropertyCheckResultType.ERROR, [text]))

    def add_multi_line_info(self, texts: List[str]) -> None:
        """Adds multiple info messages."""
        self.results.append(PropertyTypedResult(PropertyCheckResultType.INFO, texts))

    def add_multi_line_warning(self, texts: List[str]) -> None:
        """Adds multiple warning messages."""
        self.results.append(PropertyTypedResult(PropertyCheckResultType.WARNING, texts))

    def add_multi_line_error(self, texts: List[str]) -> None:
        """Adds multiple error messages."""
        self.results.append(PropertyTypedResult(PropertyCheckResultType.ERROR, texts))

    def get_contains_infos(self) -> bool:
        """Returns True when at least one info message exists."""
        return any(result.is_info() for result in self.results)
    
    def get_contains_warnings(self) -> bool:
        """Returns True when at least one warning message exists."""
        return any(result.is_warning() for result in self.results)

    def get_contains_errors(self) -> bool:
        """Returns True when at least one error message exists."""
        return any(result.is_error() for result in self.results)

    def draw_check_report(self, layout: bpy.types.UILayout, draw_in_order: bool = True) -> bpy.types.UILayout:
        check_report = layout.column()
        check_report.alignment = "EXPAND"

        # In Blender ERROR icon is just "/!\", and CANCEL icon is (X).
        # So I preffer to use CANCEL for errors and ERROR for warnings.

        if draw_in_order:
            for result in self.results:
                result.draw_result(check_report)
        else:
            for result in self.results:
                if result.is_error():
                    for error_text in result.texts:
                        check_report.label(text=error_text, icon="CANCEL")
                elif result.is_warning():
                    for warning_text in result.texts:
                        check_report.label(text=warning_text, icon="ERROR")
                elif result.is_info():
                    for info_text in result.texts:
                        check_report.label(text=info_text, icon="INFO")
        return check_report

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