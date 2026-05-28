from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:

    jobs = [PrintJob(**job) for job in print_jobs]

    printer = PrinterConstraints(**constraints)

    # Сортування за пріоритетом та часом друку
    jobs.sort(key=lambda x: (x.priority, x.print_time))

    print_order = []
    total_time = 0

    current_group = []
    current_volume = 0

    for job in jobs:
        can_add = (
            len(current_group) < printer.max_items
            and current_volume + job.volume <= printer.max_volume
        )

        if can_add:
            current_group.append(job)
            current_volume += job.volume

        else:
            group_time = max(item.print_time for item in current_group)
            total_time += group_time

            for item in current_group:
                print_order.append(item.id)

            current_group = [job]
            current_volume = job.volume

    if current_group:
        group_time = max(item.print_time for item in current_group)
        total_time += group_time

        for item in current_group:
            print_order.append(item.id)

    return {
        "print_order": print_order,
        "total_time": total_time
    }


# Тест
def test_printing_optimization():

    # тест 1
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # тест 2
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    # тест 3
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1:")
    result1 = optimize_printing(test1_jobs, constraints)
    print(result1)

    print("\nТест 2:")
    result2 = optimize_printing(test2_jobs, constraints)
    print(result2)

    print("\nТест 3:")
    result3 = optimize_printing(test3_jobs, constraints)
    print(result3)


if __name__ == "__main__":
    test_printing_optimization()
