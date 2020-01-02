from django.contrib import admin
from .models import *


class DEPAdmin(admin.ModelAdmin):
    list_display = [
            'ID',
            'NAME_DEP',
    ]
    search_fields = ('ID', 'NAME_EDP')


class CLAAdmin(admin.ModelAdmin):
    list_display = [
            'ID',
            'NAME_CLA',
    ]
    search_fields = ('ID', 'NAME_CLA')


class STUAdmin(admin.ModelAdmin):
    list_display = [
            'STUDENTID',
            'NAME_STU',
            'PASSWORD',
            'SEX',
            'NAME_CLA',
            'NAME_DEP',
            'BIRTHDAY',
            'NATIVE_PLACE',
    ]
    list_filter = ('NAME_DEP', 'NAME_CLA', 'NATIVE_PLACE')
    search_fields = ('STUDENTID', 'NAME_STU')

            
class CHAAdmin(admin.ModelAdmin):
    list_display = [
            'ID',
            'STUDENTID',
            'CODE',
            'DESCRIPTION',
    ]
    search_list = ('ID', 'STUDENTID')
    list_filter = ('CODE', )


class REWAdmin(admin.ModelAdmin):
    list_display = [
            'ID',
            'STUDENTID',
            'LEVELS',
            'REC_TIME',
            'DESCRIPTION',
    ]
    search_fields = ('ID', 'STUDENTID')
    list_filter = ('LEVELS', 'REC_TIME')


class PUNAdmin(admin.ModelAdmin):
    list_display = [
            'ID',
            'STUDENTID',
            'ENABLE',
            'LEVELS',
            'DESCRIPTION',
            'REC_TIME',
    ]
    search_fields = ('ID', 'STUDENTID')
    list_filter = ('LEVELS', 'ENABLE')

admin.site.register(CHANGE_CODE)
admin.site.register(PUNISH_LEVELS)
admin.site.register(REWARD_LEVELS)
admin.site.register(DEPARTMENT, DEPAdmin)
admin.site.register(CLASS, CLAAdmin)
admin.site.register(STUDENT, STUAdmin)
admin.site.register(REWARD, REWAdmin)
admin.site.register(CHANGE, CHAAdmin)
admin.site.register(PUNISH, PUNAdmin)
admin.AdminSite.site_header = "学生管理系统"
admin.AdminSite.site_title = "管理"
# Register your models here.
