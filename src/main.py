import machine


def blink(pin: machine.Pin) -> None:
    """Toggle the value of a MicroPython Pin."""
    pin.value(not pin.value())


def main() -> None:
    led = machine.Pin(25, machine.Pin.OUT)
    blink(led)
    print("Hello, World!")


if __name__ == "__main__":
    main()
