# Shekl-e dade-ha
from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    text: str
    answer: str
    kind: str = "text"
    choices: tuple[str, ...] = ()