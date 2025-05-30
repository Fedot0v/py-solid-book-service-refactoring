from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, data: dict) -> None:
        """Display the data in a specific format."""
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: dict) -> None:
        """Display data in the console."""
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: dict) -> None:
        """Display data in reverse."""
        print(content[::-1])
