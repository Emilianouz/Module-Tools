#If we define "sadness" as the number of places down in someone's ranking 
#the operating system the ended up with (i.e. if your preferences were 
#[UBUNTU, ARCH, MACOS] and you were allocated a MACOS machine your sadness would be 2), 
#  0       1      2      100
#we want to minimize the total sadness of all people. If we allocate someone a laptop 
#with an operating system not in their preferred list, treat them as having a sadness of 100.

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: List[OperatingSystem]
    assigned_laptop: Optional[int] = None

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
    assigned: bool = False

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[str, int]:
    allocation = {}
    for person in people:
        for os in person.preferred_operating_system:
            for laptop in laptops:
                if (laptop.operating_system == os and not laptop.assigned):
                    allocation[person.name] = laptop.id
                    assigned = True
                    break
            if assigned:
                break
    return allocation

people = [
    Person(name="Imran", age=22, preferred_operating_system=[OperatingSystem.UBUNTU,OperatingSystem.ARCH,OperatingSystem.MACOS]),
    Person(name="Eliza", age=34, preferred_operating_system=[OperatingSystem.ARCH]),
    Person(name="Maria", age=38, preferred_operating_system=[OperatingSystem.MACOS,OperatingSystem.ARCH]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

if __name__ == "__main__":
    allocation = allocate_laptops(people, laptops)
    print("Allocation:", allocation)