from turtle import title

from django.core.exceptions import ValidationError
from django.test import TestCase
from core.models import Product


from django.test import TestCase


# 1. Класс заметки (логика приложения)
class Note:

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def get_created_at(self):
        return "2024-01-01"

class TestNote(TestCase):

    def test_note_creation(self):
        Note.objects.create(
            title="Тестовая заметка!",
            text="Это тестовая заметка."
        )
        self.assertEqual(Note.objects.count(), 1)

    def setUp(self):
        # Инициализация объекта перед каждым тестом
        self.note = Note(title="Тестовая заметка!", text="Это тестовая заметка.")

    def test_note_creation_and_created_at(self):
        assert self.note.title == "Тестовая заметка!"
        assert self.note.text == "Это тестовая заметка."
        assert self.note.get_created_at() == "2024-01-01"
