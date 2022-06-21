import unittest

from Babel_heureka_code import BabelCode, BabelVerwalter


class TestBabelBasisVerwalter(unittest.TestCase):
    """ Testet den Verwalter """
    def setUp(self) -> None:
        """ Legt einen neuen Verwalter an """
        self.verwalter = BabelVerwalter()

    def test_code(self):
        """ Testet, ob ein BabelCode angelegt werden kann """
        code1 = BabelCode("id#01")
        code1.verwalter_setzen(self.verwalter)
        self.assertTrue(self.verwalter.ist_code_registriert(code1.name))

    def test_attr(self):
        """ Testet die Attributschreibweise """
        code1 = BabelCode("id01")
        code2 = BabelCode.id01
        self.assertEqual(code1, code2)


if __name__ == '__main__':
    unittest.main()
