import re

MUL_PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def recover_memory(data: str) -> int:
    """
    Function to scan for mul(x,y) in corrupted data and return the sum of the products
    """
    # Use regex to find all instances of mul(x,y)
    mul_matches = MUL_PATTERN.findall(data)

    # Sum the products of the matches
    total = 0
    for match in mul_matches:
        x = int(match[0])
        y = int(match[1])
        total += x * y

    return total


def recover_memory_conditional(data: str) -> int:
    """
    Function to scan for mul(x,y) in corrupted data and return the sum of the products.

    This function will also handle do() and don't() operators.
    do() enables the next mul(x,y) to be included in the sum,
    don't() disables the next mul(x,y) from being included in the sum.
    """

    mul_matches = MUL_PATTERN.finditer(data)

    total = 0
    for match in mul_matches:
        preceding_text = data[: match.start()]

        last_dont = preceding_text.rfind("don't()")
        last_do = preceding_text.rfind("do()")

        # If don't() appears after do(), or there's a don't() and no do(),
        # this multiplication is disabled
        if last_dont > last_do and last_dont != -1:
            continue

        x = int(match.group(1))
        y = int(match.group(2))

        total += x * y

    return total


def read_input_data(file_path: str) -> str:
    with open(file_path, "r") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    data = read_input_data("day3_input.txt")
    print("Recovered memory:", recover_memory(data))
    print("Recovered memory with conditions:", recover_memory_conditional(data))
