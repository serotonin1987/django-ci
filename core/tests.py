from turtle import title
from django.core.exceptions import ValidationError
from django.db import models
from django.test import TestCase
from core.models import Product
from django.test import TestCase
from core.models import Note

class TestNote(TestCase):
    def test_note_creation(self):
        Note.objects.create(
            title="Тестовая заметка!",
            text="Это тестовая заметка."
        )
        self.assertEqual(Note.objects.count(), 1)

    def test_note_creation_and_created_at(self):
        note = Note.objects.create(
            title="Тестовая заметка!",
            text="Это тестовая заметка."
        )
        assert note.title == "Тестовая заметка!"
        assert note.text == "Это тестовая заметка."
        assert note.get_created_at() == "2024-01-01"
