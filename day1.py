from typing import List, Tuple

from rich import print


def caluculate_distance(list1: List[int], list2: List[int]) -> int:
    combined = zip(sorted(list1), sorted(list2))

    total_distance = 0
    for i in combined:
        total_distance += abs(i[1] - i[0])

    return total_distance


def create_lists_from_file(file_path: str) -> Tuple[List[int], List[int]]:
    list1 = []
    list2 = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            num1, num2 = map(int, line.strip().split("   "))
            list1.append(num1)
            list2.append(num2)
    return list1, list2


def calculate_similarity_score(list1: List[int], list2: List[int]) -> int:

    similarity = 0
    for i in list1:
        multiplier = list2.count(i)

        similarity += i * multiplier

    return similarity


if __name__ == "__main__":
    list1, list2 = create_lists_from_file("day1_input.txt")
    print("Distance:", caluculate_distance(list1, list2))
    print("Similarity:", calculate_similarity_score(list1, list2))
