Sprachen
===============================================

Basisklasse
-----------------------------------------------

Für Sprachen wird eine abstrakte Klasse definiert

.. autoclass:: Babel_heureka_code.BasisBabelSprachVersion
    :members:


Implementierung
-----------------------------------------------

Es gibt mehr als eine Standardimplementierung

Eine Sprache kann innerhalb des Codes über ein Dictionary definiert werden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: Babel_heureka_code.DictSprache
    :members:

Auch kann eine Sprache über eine Konfigurationsdatei definiert werden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: Babel_heureka_code.SprachConfig
    :members:

Anwendung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> from Babel_heureka_code import BabelCode, BabelVerwalter, DictSprache
>>> verwalter = BabelVerwalter()
>>> code1: BabelCode = verwalter.code01
>>> code1
<BabelCode code01>
>>> de = DictSprache({"code01": "Erster code"})
>>> en = DictSprache(code01="First code")  # Eine Sprache kann auch über kwargs erstellt werden
>>> de.wert_fuer_code("code01")
'Erster code'
>>> en.wert_fuer_code("code01")
'First code'
>>> verwalter.setze_sprache(de)
>>> code1.wert
'Erster code'
>>> verwalter.setze_sprache(en)
>>> str(code1)
'First code'
