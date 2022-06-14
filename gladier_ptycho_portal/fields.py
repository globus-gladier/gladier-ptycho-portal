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


def get_https_url(rfm_url):
    """
    Turn this: 
    https://80150e2e-5e88-4d35-b3cd-170b25b60538.e.globus.org/portal/ptychography/test_ryan1/probe_0_im.jpg
    into this:
    https://g-4bbfe.fd635.8443.data.globus.org/portal/ptychography/test_ryan1/probe_0_im.jpg
    """
    purl = urlsplit(rfm_url)
    rurl = urlunsplit(['https', 'g-4bbfe.fd635.8443.data.globus.org', purl.path, '', ''])
    return rurl




def fetch_all_previews(result):
    # Gather base previews from the remote file manifest
    base_previews = {
        entry['url']: {
            'caption': entry['filename'].rstrip('png'),
            'name': entry['filename'],
            'url': get_https_url(entry['url']),
            'filename': entry['filename'],
            'mime_type': entry['mime_type']
        } for entry in result[0].get('files', {})
        if entry['mime_type'] in ['image/jpeg']
    }    
    
    # If the user provided 'preview' info, overwrite the manifest entry with
    # the 'preview' entry
    base_previews.update(
        {entry['url']: entry
         for entry in result[0]['project_metadata'].get('preview', {})})
    # Add a preview id. The preview id is used by a javascript library to
    # determine how the data should be fetched/displayed.
    previews = list(base_previews.values())
    for idx, preview in enumerate(previews):
        preview['id'] = idx
    return sorted(previews, key=lambda p: p['url'], reverse=False)
