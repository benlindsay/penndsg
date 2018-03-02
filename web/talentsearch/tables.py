#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# copyright (c) 2018 ben lindsay <benjlindsay@gmail.com>

from account.models import Profile
import django_tables2 as tables


class TalentTable(tables.Table):
    full_name = tables.Column(verbose_name='Name')
    email = tables.Column(accessor='user.email')
    all_schools = tables.Column(verbose_name='School(s)')
    all_degrees = tables.Column(verbose_name='Degree(s)')
    program = tables.Column()
    grad_year = tables.Column()
    resume = tables.FileColumn()
    class Meta:
        # model = Profile
        template_name = 'django_tables2/bootstrap.html'
