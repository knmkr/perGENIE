# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.utils.translation import ugettext as _
from django.conf import settings
from models import *

import sys, os
from pprint import pformat
import pymongo

from utils.clogging import getColorLogger
log = getColorLogger(__name__)


@login_required
def index(request):
    user_id = request.user.username
    msg, err, = '', ''
    n_out_dated_riskreports = 0
    intro_type, intros = [''], []

    while True:
        catalog_latest_new_records_data = get_latest_added_date()
        infos = get_data_infos(user_id)
        recent_catalog_records = get_recent_catalog_records()

        if not infos:
            intro_type = ['first']

        else:
            intro_type = ['wait_upload']
            # check if latest riskreports are outdated
            for info in infos:
                risk_report_latest_date = info.get('riskreport')

                if risk_report_latest_date:
                    # If there is at least one riskreported file,
                    intro_type = []

                    if risk_report_latest_date.date() < catalog_latest_new_records_data:
                        warns.append('risk report outdated: {}'.format(info['name']))
                        n_out_dated_riskreports += 1
                elif info['status'] == 100:
                    # If there is at least one 100% uploaded file,
                    intro_type = ['risk_report']
                else:
                    pass

        # Intro.js
        if intro_type == ['first']:
            # Translators: This message appears on the home page only
            intros.append(_('First, upload your genome file!'))
            intros.append(_('Next, ....'))
        elif intro_type == ['wait_upload']:
            intros.append('Please wait until your genome file uploaded...')
        elif intro_type == ['risk_report']:
            intros.append('Browse your Risk Report!')
        else:
            pass

        break

    msgs = dict(msg=msg, err=err, user_id=user_id, demo_user_id=settings.DEMO_USER_ID,
                catalog_latest_new_records_data=catalog_latest_new_records_data,
                n_out_dated_riskreports=n_out_dated_riskreports,
                recent_catalog_records=recent_catalog_records,
                intros=intros, intro_type=intro_type, infos=infos)

    return direct_to_template(request, 'dashboard/index.html', msgs)
