#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# copyright (c) 2018 ben lindsay <benjlindsay@gmail.com>

from django.shortcuts import render

from .tables import TalentTable
from account.models import Profile
from django_tables2 import RequestConfig


def talent_table_view(request):
    # https://stackoverflow.com/a/18211441/2680824
    # turn queryset into list before passing to table to allow sorting by
    # non database properties in html table
    searchable_profiles = list(Profile.objects.filter(searchable=True))
    table = TalentTable(
        searchable_profiles,
        exclude=('email_confirmed', 'searchable',),
    )
    RequestConfig(request).configure(table)

    # https://stackoverflow.com/a/18211441/2680824
    # pagination
    try:
        page_number = int(request.GET.get('page'))
    except (ValueError, TypeError):
        page_number = 1

    try:
        table.paginate(page=page_number, per_page=10)
    except InvalidPage:
        table.paginate(page=1, per_page=10)

    return render(request, 'talentsearch/talent_table.html', {'table': table})
