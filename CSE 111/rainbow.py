import time

def generate_rainbow(length, repeat_lines=10, delay=0.1):
    # ANSI escape codes for colors
    colors = [
        "\033[31m",  # Red
        "\033[33m",  # Yellow
        "\033[32m",  # Green
        "\033[34m",  # Blue
        "\033[35m"   # Magenta (Violet)
    ]
    reset = "\033[0m"  # Resets to default color

    count = 0  # Tracks color index

    # Part 1: Build the pyramid upwards
    for i in range(1, length + 1):
        # Repeat the same color `repeat_lines` times before switching
        for _ in range(repeat_lines):
            print(colors[count] + "0" * i + reset)
            time.sleep(delay)  # Add slight delay between lines
        count = (count + 1) % len(colors)  # Cycle through colors after repeating

    # Part 2: Shrink the pyramid downwards
    for i in range(length - 2, 0, -1):
        # Repeat the same color `repeat_lines` times before switching
        for _ in range(repeat_lines):
            print(colors[count] + "0" * i + reset)
            time.sleep(delay)  # Add slight delay between lines
        count = (count + 1) % len(colors)  # Cycle through colors after repeating

# Call the function to print the pyramid
while True:
    generate_rainbow(10, repeat_lines=2, delay=0.029)  # Adjust repeat_lines and delay as needed