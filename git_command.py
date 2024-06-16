from dataclasses import dataclass
from typing import List

@dataclass
class Option:
    name: str
    long_name: str
    description: str

@dataclass
class GitCommand:
    command_name: str
    description: str
    usage: str
    options: List[Option]
    examples: List[str]
    details: str
