from dataclasses import dataclass
from typing import Dict

@dataclass
class Symbol:
    name: str
    kind: str

class SymbolTable:
    def __init__(self):
        self.scenes: Dict[str, Symbol] = {}
    
    def add_scene(self, name: str) -> bool:
        if name in self.scenes:
            return False
        self.scenes[name] = Symbol(name, 'scene')
        return True
    
    def scene_exists(self, name: str) -> bool:
        return name in self.scenes
