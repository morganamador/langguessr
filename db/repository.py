from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def load_orthographies(self):
        """Return a dict mapping orthography name to a set of its graphemes."""
        pass