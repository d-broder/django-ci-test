from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_math(self):
        """Teste simples para garantir que o CI está rodando."""
        self.assertEqual(1 + 1, 2)
