import csv
from pathlib import Path
from src.lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8")

    def _read_all(self):
        if not self.path.exists() or self.path.stat().st_size == 0:
            return
        with self.path.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield Student(
                    fio=row["fio"],
                    birthdate=row["birthdate"],
                    group=row["group"],
                    gpa=float(row["gpa"])
                )

    def _rewrite(self, students):
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["fio", "birthdate", "group", "gpa"])
            for s in students:
                writer.writerow([s.fio, s.birthdate, s.group, s.gpa])

    def list(self):
        return list(self._read_all())

    def add(self, student: Student):
        file_empty = not self.path.exists() or self.path.stat().st_size == 0
        with self.path.open("a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            if file_empty:
                writer.writerow(["fio", "birthdate", "group", "gpa"])
            writer.writerow([student.fio, student.birthdate,
                            student.group, student.gpa])

    def find(self, substr: str):
        return [s for s in self.list() if substr.lower() in s.fio.lower()]

    def remove(self, fio: str):
        students = self.list()
        for i, student in enumerate(students):
            if student.fio == fio:
                students.pop(i)
                self._rewrite(students)
                return
        raise ValueError(f"Студент '{fio}' не найден")

    def update(self, fio: str, **fields):
        students = self.list()
        for student in students:
            if student.fio == fio:
                if "fio" in fields:
                    student.fio = fields["fio"]
                if "birthdate" in fields:
                    student.birthdate = fields["birthdate"]
                if "group" in fields:
                    student.group = fields["group"]
                if "gpa" in fields:
                    student.gpa = float(fields["gpa"])
                self._rewrite(students)
                return
        raise ValueError(f"Студент с ФИО '{fio}' не найден")

    def stats(self) -> dict:
        students = self.list()

        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }

        count = len(students)

        gpas = [s.gpa for s in students]

        min_gpa = min(gpas)
        max_gpa = max(gpas)
        avg_gpa = round(sum(gpas) / len(gpas), 2)

        groups = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1

        top_5_students = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted(students, key=lambda x: x.gpa, reverse=True)[:5]
        ]

        return {
            "count": count,
            "min_gpa": min_gpa,
            "max_gpa": max_gpa,
            "avg_gpa": avg_gpa,
            "groups": groups,
            "top_5_students": top_5_students
        }
