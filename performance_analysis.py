import random
import time


def build_data(size: int) -> list[int]:
    """Create a dataset with repeated values to test duplicate detection."""
    return [random.randint(1, size // 2) for _ in range(size)]


def duplicates_with_list(values: list[int]) -> list[int]:
    """
    Unoptimized version:
    Uses repeated list searching, which is slower for larger inputs.
    """
    found_duplicates = []

    for i in range(len(values)):
        current = values[i]
        if current in values[i + 1:] and current not in found_duplicates:
            found_duplicates.append(current)

    return found_duplicates


def duplicates_with_set(values: list[int]) -> list[int]:
    """
    Optimized version:
    Uses a set for faster membership checks.
    """
    seen = set()
    found_duplicates = set()

    for item in values:
        if item in seen:
            found_duplicates.add(item)
        else:
            seen.add(item)

    return list(found_duplicates)


def run_comparison() -> None:
    sizes = [5000, 10000, 15000]

    print("Duplicate Detection Performance Test")
    print("-" * 45)

    for size in sizes:
        data = build_data(size)

        start_list = time.perf_counter()
        list_result = duplicates_with_list(data)
        end_list = time.perf_counter()

        start_set = time.perf_counter()
        set_result = duplicates_with_set(data)
        end_set = time.perf_counter()

        list_time = end_list - start_list
        set_time = end_set - start_set

        print(f"Dataset size: {size}")
        print(f"List-based method time: {list_time:.6f} seconds")
        print(f"Set-based method time:  {set_time:.6f} seconds")
        print(f"Duplicates found (list): {len(list_result)}")
        print(f"Duplicates found (set):  {len(set_result)}")
        print("-" * 45)


if __name__ == "__main__":
    run_comparison()