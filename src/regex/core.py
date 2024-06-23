from typing import Generic, TypeVar


T = TypeVar("T")
class RegexResult(Generic[T]):
  def __init__(self, value: T = None, error: str = '') -> None:
    self.value = value
    self.ok = value is not None
    self.error = error

class RegexToken():
  def __init__(self, value: str, pos: int, is_special = False) -> None:
    self.value = value
    self.is_special = is_special
    self.pos = pos
    
  def __str__(self) -> str:
    return str(self.value)