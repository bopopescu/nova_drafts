#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo.config import cfg

from nova.scheduler import filters
from nova.virt import hardware


class HyperthreadingFilter(filters.BaseHostFilter):
    """Filter on host hyperthreading feature."""

    def _is_host_ht_enabled(self, host_state, flavor):
        return not (flavor.extra_specs.get("hw:cpu_policy") == 'dedicated' and
            flavor.extra_specs.get("hw:cpu_threads_policy") == 'avoid' and
            host_state['hyper_threaded'])

    def host_passes(self, host_state, filter_properties):
        flavor = filter_properties.get('instance_type')
        return self._is_host_ht_enabled(host_state, flavor)
