from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list) -> int | None:
    try:
        with open("groups.pickle", "wb") as file:
            pickle.dump(groups, file)
        return max(len(group.students) for group in groups)
    except Exception as e:
        print(f"Error writing groups information: {e}")
        return None


def write_students_information(students: list[Student]) -> int | None:
    try:
        with open("students.pickle", "wb") as file:
            pickle.dump(students, file)
        return len(students)
    except Exception as e:
        print(f"Error writing students information: {e}")
        return None


def read_groups_information() -> list | None:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            specialties = set(group.specialty.name for group in groups)
            return list(specialties)
    except Exception as e:
        print(f"Error reading groups information: {e}")
        return None


def read_students_information() -> list:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
    except (EOFError, FileNotFoundError):
        pass
    return students
