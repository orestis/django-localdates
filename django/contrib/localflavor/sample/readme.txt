Documentation for translators:

To add local date functionality for a new locale, follow these steps:

1. Add your locale directory in django.contrib.locale
2. Do a "make-messages"
3. Edit django.po and start specifying the date formats for your locale. Try to use as much of the presupplied django (see the template documentation) and localdates placeholders(for now, {Fp} and {Fd}).
4. If you use {Fp} and {Fd}, don't forget to fill-in the Month_POS and Month_DIR messages, too.
5. If you're covered with just that, do a "compile-messages" and you're good to go!
6. If not, you'll have to specify your own placeholders. Try to use the Django placeholder (eg. F for month) followed by a case identifier (eg. Fp for month possesive). Do this in localflavor/locale/dateformat.py. You are free to do as you please, though it is recommended to use an architecture like the one found in the sample localflavor directory.

Don't forget to send your patch!
