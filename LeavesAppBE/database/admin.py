from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import gobeacc, goremal, gorsdav, nbrjobs, nbrbjob, spriden, pebempl, phraccr, perleav, perefml, perfmla, perbfml, perjtot, ptrearn, pdrdedn


@admin.register(gobeacc)
class gobeaccAdmin(ImportExportModelAdmin):
    pass

@admin.register(goremal)
class goremalAdmin(ImportExportModelAdmin):
    pass


@admin.register(gorsdav)
class gorsdavAdmin(ImportExportModelAdmin):
    pass


@admin.register(nbrbjob)
class nbrbjobAdmin(ImportExportModelAdmin):
    pass

@admin.register(nbrjobs)
class nbrjobsAdmin(ImportExportModelAdmin):
    pass


@admin.register(spriden)
class spridenAdmin(ImportExportModelAdmin):
    pass

@admin.register(pebempl)
class pebemplAdmin(ImportExportModelAdmin):
    pass

@admin.register(phraccr)
class phraccrAdmin(ImportExportModelAdmin):
    pass


@admin.register(perleav)
class perleavAdmin(ImportExportModelAdmin):
    pass


@admin.register(perefml)
class perefmlAdmin(ImportExportModelAdmin):
    pass

@admin.register(perfmla)
class perefmlaAdmin(ImportExportModelAdmin):
    pass

@admin.register(perbfml)
class perebfmlAdmin(ImportExportModelAdmin):
    pass

@admin.register(perjtot)
class perjtotAdmin(ImportExportModelAdmin):
    pass

@admin.register(ptrearn)
class ptrearnAdmin(ImportExportModelAdmin):
    pass

@admin.register(pdrdedn)
class pdedednAdmin(ImportExportModelAdmin):
    pass



