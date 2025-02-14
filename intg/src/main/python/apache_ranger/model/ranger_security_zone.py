#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from apache_ranger.model.ranger_base import RangerBase, RangerBaseModelObject
from apache_ranger.utils             import *


class RangerSecurityZoneService(RangerBase):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}

        RangerBase.__init__(self, attrs)

        self.resources = attrs.get('resources')

    def type_coerce_attrs(self):
        super(RangerSecurityZoneService, self).type_coerce_attrs()

        self.resources = type_coerce_list_dict(self.resources, list)


class RangerSecurityZone(RangerBaseModelObject):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}

        RangerBaseModelObject.__init__(self, attrs)

        self.name            = attrs.get('name')
        self.services        = attrs.get('services')
        self.tagServices     = attrs.get('tagServices')
        self.adminUsers      = attrs.get('adminUsers')
        self.adminUserGroups = attrs.get('adminUserGroups')
        self.auditUsers      = attrs.get('auditUsers')
        self.auditUserGroups = attrs.get('auditUserGroups')
        self.description     = attrs.get('description')

    def type_coerce_attrs(self):
        super(RangerSecurityZone, self).type_coerce_attrs()

        self.services = type_coerce_dict(self.services, RangerSecurityZoneService)

class RangerSecurityZoneHeaderInfo(RangerBaseModelObject):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}

        RangerBaseModelObject.__init__(self, attrs)

        self.name = attrs.get('name')
