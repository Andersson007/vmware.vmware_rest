#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: vcenter_resourcepool
short_description: Creates a resource pool.
description: Creates a resource pool.
options:
    cpu_allocation:
        description:
        - Resource allocation for CPU.
        - 'Valid attributes are:'
        - ' - C(reservation) (int): Amount of resource that is guaranteed available
            to a resource pool. Reserved resources are not wasted if they are not
            used. If the utilization is less than the reservation, the resources can
            be utilized by other running virtual machines. Units are MB fo memory,
            and MHz for CPU. ([''present''])'
        - ' - C(expandable_reservation) (bool): In a resource pool with an expandable
            reservation, the reservation can grow beyond the specified value, if the
            parent resource pool has unreserved resources. A non-expandable reservation
            is called a fixed reservation. ([''present''])'
        - ' - C(limit) (int): The utilization of a resource pool will not exceed this
            limit, even if there are available resources. This is typically used to
            ensure a consistent performance of resource pools independent of available
            resources. If set to -1, then there is no fixed limit on resource usage
            (only bounded by available resources and shares). Units are MB for memory,
            and MHz for CPU. ([''present''])'
        - ' - C(shares) (dict): Shares are used in case of resource contention. ([''present''])'
        - '   - Accepted keys:'
        - '     - level (string): The C(level) defines the possible values for the
            allocation level.'
        - 'Accepted value for this field:'
        - '       - C(CUSTOM)'
        - '       - C(HIGH)'
        - '       - C(LOW)'
        - '       - C(NORMAL)'
        - '     - shares (integer): When {@link #level} is set to CUSTOM, it is the
            number of shares allocated. Otherwise, this value is ignored. There is
            no unit for this value. It is a relative measure based on the settings
            for other resource pools.'
        type: dict
    memory_allocation:
        description:
        - Resource allocation for CPU.
        - 'Valid attributes are:'
        - ' - C(reservation) (int): Amount of resource that is guaranteed available
            to a resource pool. Reserved resources are not wasted if they are not
            used. If the utilization is less than the reservation, the resources can
            be utilized by other running virtual machines. Units are MB fo memory,
            and MHz for CPU. ([''present''])'
        - ' - C(expandable_reservation) (bool): In a resource pool with an expandable
            reservation, the reservation can grow beyond the specified value, if the
            parent resource pool has unreserved resources. A non-expandable reservation
            is called a fixed reservation. ([''present''])'
        - ' - C(limit) (int): The utilization of a resource pool will not exceed this
            limit, even if there are available resources. This is typically used to
            ensure a consistent performance of resource pools independent of available
            resources. If set to -1, then there is no fixed limit on resource usage
            (only bounded by available resources and shares). Units are MB for memory,
            and MHz for CPU. ([''present''])'
        - ' - C(shares) (dict): Shares are used in case of resource contention. ([''present''])'
        - '   - Accepted keys:'
        - '     - level (string): The C(level) defines the possible values for the
            allocation level.'
        - 'Accepted value for this field:'
        - '       - C(CUSTOM)'
        - '       - C(HIGH)'
        - '       - C(LOW)'
        - '       - C(NORMAL)'
        - '     - shares (integer): When {@link #level} is set to CUSTOM, it is the
            number of shares allocated. Otherwise, this value is ignored. There is
            no unit for this value. It is a relative measure based on the settings
            for other resource pools.'
        type: dict
    name:
        description:
        - Name of the resource pool. Required with I(state=['present'])
        type: str
    parent:
        description:
        - Parent of the created resource pool. Required with I(state=['present'])
        type: str
    resource_pool:
        description:
        - Identifier of the resource pool to be deleted. Required with I(state=['absent',
            'present'])
        type: str
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    state:
        choices:
        - absent
        - present
        default: present
        description: []
        type: str
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that run the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 0.3.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: Get the existing resource pools
  vmware.vmware_rest.vcenter_resourcepool_info:
  register: resource_pools

- name: Create an Ad hoc resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    name: my_resource_pool
    parent: '{{ resource_pools.value[0].resource_pool }}'
    cpu_allocation:
      expandable_reservation: true
      limit: 40
      reservation: 0
      shares:
        level: NORMAL
    memory_allocation:
      expandable_reservation: false
      limit: 2000
      reservation: 0
      shares:
        level: NORMAL
  register: my_resource_pool

- name: Remove a resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    resource_pool: '{{ my_resource_pool.id }}'
    state: absent

- name: Create a generic resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    name: my_resource_pool
    parent: '{{ resource_pools.value[0].resource_pool }}'
  register: my_resource_pool

- name: Modify a resource pool
  vmware.vmware_rest.vcenter_resourcepool:
    resource_pool: '{{ my_resource_pool.id }}'
    cpu_allocation:
      expandable_reservation: true
      limit: -1
      reservation: 0
      shares:
        level: NORMAL
    memory_allocation:
      expandable_reservation: false
      limit: 1000
      reservation: 0
      shares:
        level: NORMAL
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Create a generic resource pool
id:
  description: moid of the resource
  returned: On success
  sample: resgroup-1009
  type: str
value:
  description: Create a generic resource pool
  returned: On success
  sample:
    cpu_allocation:
      expandable_reservation: 1
      limit: -1
      reservation: 0
      shares:
        level: NORMAL
    memory_allocation:
      expandable_reservation: 1
      limit: -1
      reservation: 0
      shares:
        level: NORMAL
    name: my_resource_pool
    resource_pools: []
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "delete": {"query": {}, "body": {}, "path": {"resource_pool": "resource_pool"}},
    "update": {
        "query": {},
        "body": {
            "cpu_allocation": "cpu_allocation",
            "memory_allocation": "memory_allocation",
            "name": "name",
        },
        "path": {"resource_pool": "resource_pool"},
    },
    "create": {
        "query": {},
        "body": {
            "cpu_allocation": "cpu_allocation",
            "memory_allocation": "memory_allocation",
            "name": "name",
            "parent": "parent",
        },
        "path": {},
    },
}  # pylint: disable=line-too-long

from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["cpu_allocation"] = {"type": "dict"}
    argument_spec["memory_allocation"] = {"type": "dict"}
    argument_spec["name"] = {"type": "str"}
    argument_spec["parent"] = {"type": "str"}
    argument_spec["resource_pool"] = {"type": "str"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["absent", "present"],
        "default": "present",
    }

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/vcenter/resource-pool").format(**params)


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _create(params, session):

    lookup_url = per_id_url = build_url(params)
    uniquity_keys = ["resource_pool"]
    comp_func = None

    async def lookup_with_filters(params, session, url):
        # e.g: for the datacenter resources
        if "folder" not in params:
            return
        if "name" not in params:
            return
        async with session.get(
            f"{url}?names={params['name']}&folders={params['folder']}"
        ) as resp:
            _json = await resp.json()
            if isinstance(_json, list) and len(_json) == 1:
                return await get_device_info(session, url, _json[0]["resource_pool"])

    _json = None

    if params["resource_pool"]:
        _json = await get_device_info(
            session, build_url(params), params["resource_pool"]
        )

    if not _json and (uniquity_keys or comp_func):
        _json = await exists(
            params,
            session,
            url=lookup_url,
            uniquity_keys=uniquity_keys,
            per_id_url=per_id_url,
            comp_func=comp_func,
        )

    if not _json:
        _json = await lookup_with_filters(params, session, build_url(params))

    if _json:
        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}
        if "_update" in globals():
            params["resource_pool"] = _json["id"]
            return await globals()["_update"](params, session)

        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = ("https://{vcenter_hostname}" "/api/vcenter/resource-pool").format(**params)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}

        if (resp.status in [200, 201]) and "error" not in _json:
            if isinstance(_json, str):  # 7.0.2 and greater
                _id = _json  # TODO: fetch the object
            elif isinstance(_json, dict) and "value" not in _json:
                _id = list(_json["value"].values())[0]
            elif isinstance(_json, dict) and "value" in _json:
                _id = _json["value"]
            _json_device_info = await get_device_info(session, _url, _id)
            if _json_device_info:
                _json = _json_device_info

        return await update_changed_flag(_json, resp.status, "create")


async def _delete(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["delete"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["delete"])
    subdevice_type = get_subdevice_type("/api/vcenter/resource-pool/{resource_pool}")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}" "/api/vcenter/resource-pool/{resource_pool}"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.delete(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


async def _update(params, session):
    payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = (
        "https://{vcenter_hostname}" "/api/vcenter/resource-pool/{resource_pool}"
    ).format(**params)
    async with session.get(_url, **session_timeout(params)) as resp:
        _json = await resp.json()
        if "value" in _json:
            value = _json["value"]
        else:  # 7.0.2 and greater
            value = _json
        for k, v in value.items():
            if k in payload:
                if isinstance(payload[k], dict) and isinstance(v, dict):
                    to_delete = True
                    for _k in list(payload[k].keys()):
                        if payload[k][_k] != v.get(_k):
                            to_delete = False
                    if to_delete:
                        del payload[k]
                elif payload[k] == v:
                    del payload[k]
                elif payload[k] == {}:
                    del payload[k]

        if payload == {} or payload == {"spec": {}}:
            # Nothing has changed
            if "value" not in _json:  # 7.0.2
                _json = {"value": _json}
            _json["id"] = params.get("resource_pool")
            return await update_changed_flag(_json, resp.status, "get")
    async with session.patch(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        # e.g: content_configuration
        if not _json and resp.status == 204:
            async with session.get(_url, **session_timeout(params)) as resp_get:
                _json_get = await resp_get.json()
                if _json_get:
                    _json = _json_get

        _json["id"] = params.get("resource_pool")
        return await update_changed_flag(_json, resp.status, "update")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
