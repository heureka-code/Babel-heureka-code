import unittest

from Babel_heureka_code import (BabelCode, BabelVerwalter,
                                BasisBabelSprachVersion)


class Sprache(BasisBabelSprachVersion):
    """ Unterklasse zum Testen einer Sprache """
    def __init__(self, dic):
        """ Unterklasse zum Testen einer Sprache """
        self.__dic = dic

    def wert_fuer_code(self, code: str) -> str:
        """ Liefert den referenzierten Wert """
        return self.__dic.get(code, None)


class TestBabelSprache(unittest.TestCase):
    """ Testet die Sprache """
    def setUp(self) -> None:
        """ Erstellt einen Verwalter und neue Sprache """
        self.verwalter = BabelVerwalter()
        self.sprache1 = Sprache({"id01": "Wert", "id02": "Nummer"})
        self.sprache2 = Sprache({"id01": "Value", "id02": "Number"})

    def test_sprache1(self):
        """ Testet das Setzen der Sprache """
        code = BabelCode("id01")
        code.verwalter_setzen(self.verwalter)
        self.verwalter.setze_sprache(self.sprache1)
        self.assertEqual("Wert", str(code))
        self.verwalter.setze_sprache(self.sprache2)
        self.assertEqual("Value", str(code))

    def test_verwalter_code(self):
        """ Testet, ob ein Code von einem Verwalter generiert werden kann """
        code = self.verwalter("id01")
        self.verwalter.setze_sprache(self.sprache1)
        self.assertEqual("Wert", str(code))
        self.verwalter.setze_sprache(self.sprache2)
        self.assertEqual("Value", code.wert)


if __name__ == '__main__':
    unittest.main()
