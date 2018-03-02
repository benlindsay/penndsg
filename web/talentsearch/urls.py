#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>
from django.conf.urls import url

from .views import talent_table_view


app_name = 'talentsearch'
urlpatterns = [
    url(r'^$', talent_table_view, name='talentsearch/talent_table.html'),
]
