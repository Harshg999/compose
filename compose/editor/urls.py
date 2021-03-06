# -- coding: utf-8 --
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import re_path

from . import api

app_name = "editor"

urlpatterns = [
    re_path(r"^query/(?P<dialect>.+)/?$", api.query, name="query"),
    re_path(r"^execute/(?P<dialect>.+)/?$", api.execute, name="execute"),
    re_path(r"^check_status/?$", api.query, name="check_status"),
    re_path(r"^fetch_result_data/?$", api.query, name="fetch_result_data"),
    re_path(r"^get_logs/?$", api.query, name="get_logs"),
    re_path(r"^autocomplete/?$", api.autocomplete, name="autocomplete_databases"),
    re_path(
        r"^autocomplete/(?P<database>[^/?]*)/?$",
        api.autocomplete,
        name="autocomplete_tables",
    ),
    re_path(
        r"^autocomplete/(?P<database>[^/?]*)/(?P<table>[\w_\-]+)/?$",
        api.autocomplete,
        name="autocomplete_columns",
    ),
    re_path(
        r"^autocomplete/(?P<database>[^/?]*)/(?P<table>[\w_\-]+)/(?P<column>\w+)/?$",
        api.autocomplete,
        name="autocomplete_column",
    ),
    re_path(
        r"^autocomplete/(?P<database>[^/?]*)/(?P<table>[\w_\-]+)/(?P<column>\w+)/(?P<nested>.+)/?$",
        api.autocomplete,
        name="autocomplete_nested",
    ),
]
