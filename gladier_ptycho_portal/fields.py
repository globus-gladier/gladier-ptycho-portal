import os
from datetime import datetime
from urllib.parse import urlsplit, urlencode, urlunsplit


def title(record):
    return record[0]['dc']['titles'][0]['title']


def globus_app_link(result):
    rfm = remote_file_manifest(result)
    if rfm and rfm[0].get('url'):
        gurl = urlsplit(os.path.dirname(rfm[0].get('url')))
        endpoint = gurl.netloc.replace('.e.globus.org', '')
        query_params = {'origin_id': endpoint, 'origin_path': gurl.path}
        return urlunsplit(('https', 'app.globus.org', 'file-manager',
                           urlencode(query_params), ''))


def remote_file_manifest(result):
    return result[0].get('files')


def search_results(result):
    return [
        {'field': 'creator', 'name': 'Creator',
         'value': result[0]['dc']['creators'][0]['creatorName']},
        # {'field': 'acquisitionDate', 'name': 'Acquisition Date',
        #  'value': datetime.strptime(result[0]['dc']['dates'][0]['date'],
        #                             '%Y-%m-%dT%H:%M:%S'),
        #  'type': 'date'},
    ]
