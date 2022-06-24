Verwalter
--------------------------------------------------------

Basisklasse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Für Verwalter wird eine abstrakte Klasse definiert

.. autoclass:: Babel_heureka_code.BabelBasisVerwalter
    :members:


Implementierung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es gibt auch eine Standardimplementierung

.. autoclass:: Babel_heureka_code.BabelVerwalter
    :members:

Anwendung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> from Babel_heureka_code import BabelCode, BabelVerwalter
>>> verwalter = BabelVerwalter()
>>> code1: BabelCode = BabelCode.code01
>>> code1.verwalter_setzen(verwalter)
>>> code1
<BabelCode code01>
>>> code1.wert
Traceback (most recent call last):
Babel_heureka_code.exceptions.KeineSpracheGesetzt

Oder

>>> from Babel_heureka_code import BabelCode, BabelVerwalter
>>> verwalter = BabelVerwalter()
>>> code1: BabelCode = verwalter.code01
>>> code1
<BabelCode code01>
>>> code1.wert
Traceback (most recent call last):
Babel_heureka_code.exceptions.KeineSpracheGesetzt

Der Verwalter muss jetzt noch wissen, welche Sprache verwendet werden soll, um die Codes zu übersetzen.
