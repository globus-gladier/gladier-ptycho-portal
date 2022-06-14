import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from globus_portal_framework.views.generic import SearchView
from globus_portal_framework.gclients import load_search_client

log = logging.getLogger(__name__)


class GlobusPilotSearchView(LoginRequiredMixin, SearchView):
    """Custom Search view automatically filters on the ptychography 'project'. This is old,
    based on the pilot project feature and will be going away eventually."""

    @property
    def filters(self):
        return super().filters + self.get_index_info().get('default_filters', [])
