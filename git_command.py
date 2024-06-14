from dataclasses import dataclass
from typing import List

@dataclass
class GitCommand:
    command_name: str
    description: str
    usage: str
    options: List[str]
    examples: List[str]
    details: str
