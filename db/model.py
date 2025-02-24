from dataclasses import dataclass

class CRUD:
    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def get(self):
        pass


@dataclass
class Genre:
    id: int = None
    name: str = None  # Film janri (masalan, Drama, Comedy, Action)

@dataclass
class Movie:
    id: int = None
    name: str = None  # Film nomi
    genre_id: int = None  # Film qaysi janrga tegishli
    description: str = None  # Film haqida qisqacha ma'lumot
    image: str = None  # Film posteri yoki rasm URL
    file_id: str = None


