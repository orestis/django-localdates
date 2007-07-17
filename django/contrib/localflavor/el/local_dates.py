# -*- coding: utf-8 -*-


"Commonly-used date structures"

from django.utils.translation import gettext_lazy as _

#TODO this should be marked up translation messages, like:
# January_POS, February_POS etc. 
# or maybe this should go in the localflavor module instead, so we don't pollute the django translation, 
# and don't have to wait for the updates in django trunk

MONTHS_POS = {
    1:u'Ιανουαρίου', 2:u'Φεβρουαρίου', 3:u'Μαρτίου', 4:u'Απριλίου', 5:u'Μαΐου', 6:u'Ιουνίου',
    7:u'Ιουλίου', 8:u'Αυγούστου', 9:u'Σεπτεμβρίου', 10:u'Οκτωβρίου', 11:u'Νοεμβρίου',
    12:u'Δεκεμβρίου'
}

MONTHS_DIR = {
    1:u'Ιανουάριο', 2:u'Φεβρουάριο', 3:u'Μάρτιο', 4:u'Απρίλιο', 5:u'Μάιο', 6:u'Ιούνιο',
    7:u'Ιούλιο', 8:u'Αύγουστο', 9:u'Σεπτέμβριο', 10:u'Οκτώβριο', 11:u'Νοέμβριο',
    12:u'Δεκέμβριο'
}