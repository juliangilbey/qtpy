# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtStateMachine classes and functions."""

from . import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    QtBindingsNotFoundError,
    QtBindingMissingModuleError,
)

if PYQT5:
    raise QtBindingMissingModuleError(name='QtStateMachine')
elif PYQT6:
    raise QtBindingMissingModuleError(name='QtStateMachine')
elif PYSIDE2:
    raise QtBindingMissingModuleError(name='QtStateMachine')
elif PYSIDE6:
    from PySide6.QtStateMachine import *
else:
    raise QtBindingsNotFoundError()