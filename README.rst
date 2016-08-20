Langsea - Allow to manage easily objects provided by the Langsea API
========================================================

WordManager
-----------

	>>> from langsea import WordManager
    >>> word_manager = WordManager()

	-	Get words by category

    >>> word_manager.all(category='fruits')
    >>> [ Word(id=1, name="apple", image="http://www.langsea.org/media/library/apple.png"), Word(..), Word(..), ..]

	-	Get a word

    >>> word_manager.get(name="apple")
    >>>  Word(id=1, name="apple", image="http://www.langsea.org/media/library/apple.png")

CategoryManager
---------------

	>>> from langsea import CategoryManager
	>>> category_manager = CategoryManager()

	-	Get all categories

	>>> category_manager.all()
	>>> [Category(id=1, name="fruits", image="http://www.langsea.org/media/site/categories/fruits.png"), Category(..), Category(..)]

	-	Get a category by name

	>>> category_manager.get(name="fruits")
	>>> Category(id=1, name="fruits", image="http://www.langsea.org/media/site/categories/fruits.png")

MessageManager
--------------

	>>> from langsea import MessageManager
	>>> message_manager = MessageManager()

	-	Get all messages

	>>> message_manager.all()
	>>> [Message(id=0, words=[ Word, Word, ..]), ..]

	-	Get message by id

	>>> message_manager.get()
	>>> Message(id=0, words=[ Word, Word, ..])
