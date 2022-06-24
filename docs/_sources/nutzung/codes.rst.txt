Codes
--------------------------------------------------------

BabelCode ist *die* Klasse für Codes, also Übersetzungsreferenzen

.. autoclass:: Babel_heureka_code.BabelCode
    :members:

Die Metaklasse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit Referenzen auch mit der Syntax ``BabelCode.referenz`` erstellt werden können,
wird eine Metaklasse dafür definiert, welche nur die Methode ``__getattr__`` überlädt.

.. autoclass:: Babel_heureka_code._babel_code_meta.BabelCodeMeta
    :members:

Folgende Schreibweisen sind äquivalent.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> from Babel_heureka_code import BabelCode
>>> variante1 = BabelCode.code01
>>> variante2 = BabelCode("code01")
>>> variante1 == variante2
True

Was nun kommt
~~~~~~~~~~~~~~~~~~~~~~~~

Diese Codes referenzieren zwar nun auf einen bestimmten Namen, aber sie wissen nicht,
woher sie eine Übersetzung nehmen sollten. Hierzu sind Verwalter erforderlich.
