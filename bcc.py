""" Black Code Collective Meetup Api """
import os
import requests
from pprint import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta


class BCC(object):
    def __init__(self):
        self.base_url = 'https://api.meetup.com'
        self.key = "key={}".format(os.environ.get('MEETUP_API'))
        self.members = self.members()

    def members(self):
        url = "{}/2/members?{}&group_urlname=Black-Code-Collective".format(self.base_url, self.key)
        next_page = True
        data = []
        while next_page:
            resp = requests.get(url).json()
            if resp['meta']['next'] == '':
                next_page = False
            else:
                url = resp['meta']['next']

            data += resp['results']

        return data

    def joined_one_year_from_founding(self):
        more_than_1_year_members = []
        for member in self.members:
            founding_date = datetime(day=18, month=8, year=2016)
            join_date = datetime.fromtimestamp((int(member['joined']) / 1000.0))
            one_yrs_ago = relativedelta(join_date, founding_date)

            # Offsetting by 4 days to account for members besides founders.
            if one_yrs_ago.years == 0 and one_yrs_ago.days < 4 and one_yrs_ago.months == 0:
                more_than_1_year_members.append(member)

        print(len(more_than_1_year_members))
        # for member in more_than_1_year_members:
        #     pprint(member)

    def joined_one_year_from_now(self):
        more_than_1_year_members = []
        for member in self.members:
            join_date = datetime.fromtimestamp((int(member['joined']) / 1000.0))
            one_yrs_ago = relativedelta(join_date, datetime.now())

            # Offsetting by 4 days to account for members besides founders.
            if one_yrs_ago.years < 0:
                more_than_1_year_members.append(member)

        print(len(more_than_1_year_members))
        # for member in more_than_1_year_members:
        #     pprint(member)