# -*- coding: utf-8 -*-


"Commonly-used date structures"

from django.utils.translation import gettext_lazy as _

#TODO this should be marked up translation messages, like:
# January_POS, February_POS etc.
# or maybe this should go in the localflavor module instead, so we don't pollute the django translation, 
# and don't have to wait for the updates in django trunk

MONTHS_POS = {
    1:u'tammikuuta', 2:u'helmikuuta', 3:u'maaliskuuta', 4:u'huhtikuuta', 5:u'toukokuuta', 6:u'kesäkuuta',
    7:u'heinäkuuta', 8:u'elokuuta', 9:u'syyskuuta', 10:u'lokakuuta', 11:u'marraskuuta',
    12:u'joulukuuta'
}

MONTHS_DIR = {
    1:u'tammikuussa', 2:u'helmikuussa', 3:u'maaliskuussa', 4:u'huhtikuussa', 5:u'toukokuussa', 6:u'kesäkuussa',
    7:u'heinäkuussa', 8:u'elokuussa', 9:u'syyskuussa', 10:u'lokakuussa', 11:u'marraskuussa',
    12:u'joulukuussa'
}
