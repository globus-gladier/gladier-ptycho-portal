from gladier_ptycho_portal import fields

SEARCH_INDEXES = {
    'ptycho': {
        'name': 'APS Ptychography',
        'uuid': '93e343cc-b555-4d60-9aab-80ff191a8abb',
        'fields': [
            ('title', fields.title),
            # ('truncated_description', fields.get_truncated_description),
            # ('description', fields.get_full_description),
            ('search_results', fields.search_results),
            ('globus_app_link', fields.globus_app_link),
            # ('filename', fields.filename),
            ('remote_file_manifest', fields.remote_file_manifest),
            'dc',
            # 'ncipilot',
            # ('https_url', fields.https_url),
            # ('copy_to_clipboard_link', fields.https_url),
            ('all_preview', fields.fetch_all_previews),
            ('image_preview', fields.image_preview),
            ('text_outputs', fields.text_outputs),
            ('resource_server', lambda r: '80150e2e-5e88-4d35-b3cd-170b25b60538')
        ],
        'facets': [
            {
                'name': 'Creator',
                'field_name': 'dc.creators.creatorName',
            },
            {
                'name': 'Dates',
                'field_name': 'dc.dates.date',
                'type': 'date_histogram',
                'date_interval': 'day',
            },
            {
                'name': 'File Sizes',
                'field_name': 'files.length',
                'type': 'numeric_histogram',
                'histogram_range': {'low': 0, 'high': 10000}
            },
        ],
        # Automatically append these filters to all searches
        # Currently, this is used to hide a globus-pilot record used for tracking project data
        'default_filters': [{
            'type': 'match_all',
            'field_name': 'project_metadata.project-slug',
            'values': ['ptychography']
        }],
        'collection': '80150e2e-5e88-4d35-b3cd-170b25b60538',
        'base_templates': 'globus-portal-framework/v2/',
        'filter_match': 'match-all',
        'template_override_dir': 'ptychography',

    }
}