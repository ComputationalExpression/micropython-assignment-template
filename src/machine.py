import time
import random
from typing import Any

class Pin:

    IN = 0
    OUT = 1
    PULL_UP = 1

    def __init__(self, id: Any, mode: Any, *args, **kwargs):
        self.id = id
        self.mode = mode
        self.val = 0

    def value(self) -> int:
        return self.val
      
    def on(self):
        pass

    def off(self):
        pass
