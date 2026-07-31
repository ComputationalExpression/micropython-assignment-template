import machine

from main import blink, main


def test_blink_toggles_pin_value(pin):
    led = machine.Pin(25, machine.Pin.OUT)
    led.value(0)
    blink(led)
    assert led.value() == 1
    blink(led)
    assert led.value() == 0


def test_main_runs_without_hardware(pin, capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
