#!/usr/bin/env python3
"""user module
"""


import datetime
import uuid
from models.base_model import BaseModel


class State(BaseModel):
    """state model inherits from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """init method for user class used in instantiation
        """
        super().__init__(*args, **kwargs)