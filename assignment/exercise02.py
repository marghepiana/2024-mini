import machine
import time
import json
import os.path


def get_params(param_file: str) -> tuple[int, float]:
    """Reads parameters from a JSON file."""

    if not os.path.isfile(param_file):
        raise OSError(f"File {param_file} not found")

    with open(param_file, "r") as f:
        params = json.load(f)

    return params["loop_count"], params["sleep_time"]


if __name__ == "__main__":
    led = machine.Pin("LED", machine.Pin.OUT)

    tic: int = time.ticks_ms()

    N, delay = get_params("exercise02.json")

    for i in range(N):
        led.high()
        time.sleep(delay)
        led.low()
        time.sleep(delay)
        print(f"loop {i} / {N}")

    toc: int = time.ticks_ms()

    t_elapsed: float = time.ticks_diff(toc, tic) / 1000.0

    print(f"LED task done in {t_elapsed:.3f} sec")
