import mockro
import pytest


class FakePin:
    """A stateful stand-in for ``machine.Pin`` used by tests."""

    IN = 0
    OUT = 1
    PULL_UP = 1

    def __init__(self, id: int, mode: int = -1, pull: int = -1, *, value=None, **kwargs):
        self.id = id
        self.mode = mode
        self._value = 0 if value is None else int(value)

    def value(self, x=None):
        if x is not None:
            self._value = int(x)
        return self._value

    def on(self) -> None:
        self._value = 1

    def off(self) -> None:
        self._value = 0


@pytest.fixture
def pin():
    """Provide a stateful ``machine.Pin`` replacement during tests."""
    with mockro.override(machine_Pin=FakePin):
        yield FakePin
