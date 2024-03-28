from dataclasses import dataclass


@dataclass
class Idea:
    content: str
    extras: dict[str, str]
