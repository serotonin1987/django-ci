from django.core.exceptions import ValidationError
from django.test import TestCase
from core.models import Product


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
    def created_at(self):
        return "2024-01-01"  
    def test_1(self):
        assert self.title == "Тестовая заметка!"
        assert self.text == "Это тестовая заметка."
        assert self.created_at() == "2024-01-01"
        