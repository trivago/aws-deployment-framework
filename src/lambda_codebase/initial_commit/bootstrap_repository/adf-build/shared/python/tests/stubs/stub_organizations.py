# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""
Stubs for testing organization.py
"""

describe_organization = {
    'Organization': {
        'Id': 'some_org_id',
        'Arn': 'string',
        'FeatureSet': 'ALL',
        'MasterAccountArn': 'string',
        'MasterAccountId': 'some_master_account_id',
        'MasterAccountEmail': 'string',
        'AvailablePolicyTypes': [
            {
                'Type': 'SERVICE_CONTROL_POLICY',
                'Status': 'ENABLED'
            },
        ]
    }
}

list_parents = {
    'Parents': [
        {
            'Id': 'some_id',
            'Type': 'ORGANIZATIONAL_UNIT'
        },
    ],
    'NextToken': 'string'
}

list_parents_root = {
    'Parents': [
        {
            'Id': 'some_id',
            'Type': 'ROOT'
        },
    ],
    'NextToken': 'string'
}

describe_organizational_unit = {
    'OrganizationalUnit': {
        'Id': 'some_org_unit_id',
        'Arn': 'string',
        'Name': 'some_ou_name'
    }
}


organization_map = {
            "Name": "root_name",
            "Id": "root_id",
            "Accounts": [
                {
                    "Name": "core",
                    "Id": "account_1"
                }
            ],
            "OrganizationalUnits": [
                {
                    "Name": "domain",
                    "Id": "ou_id_1",
                    "Accounts": [
                        {
                            "Name": "domain-sandbox",
                            "Id": "account_2"
                        }
                    ],
                    "OrganizationalUnits": [
                        {
                            "Name": "app1",
                            "Id": "ou_id_1_1",
                            "Accounts": [
                                {
                                    "Name": "app1-sandbox",
                                    "Id": "account_3"
                                }
                            ],
                            "OrganizationalUnits": [
                                {
                                    "Name": "prod",
                                    "Id": "ou_id_1_1_1",
                                    "Accounts": [
                                        {
                                            "Name": "app1-prod",
                                            "Id": "account_4"
                                        }
                                    ],
                                    "OrganizationalUnits":[]
                                }
                            ]
                        },
                        {
                            "Name": "app2",
                            "Id": "ou_id_1_2",
                            "Accounts": [
                                {
                                    "Name": "app2-sandbox",
                                    "Id": "account_5"
                                }
                            ],
                            "OrganizationalUnits": [
                                {
                                    "Name": "prod",
                                    "Id": "ou_id_1_2_1",
                                    "Accounts": [
                                        {
                                            "Name": "app2-prod",
                                            "Id": "account_6"
                                        }
                                    ],
                                    "OrganizationalUnits":[]
                                }
                            ]
                        }
                    ]
                }
            ]
        }


def find(key, dictionary):
    if dictionary["Id"] == key:
        return dictionary
    for d in dictionary["OrganizationalUnits"]:
        result = find(key, d)
        if result: 
            return result

def get_accounts_for_parent(ParentId):  
      
    return find(ParentId, organization_map)["Accounts"]

def get_child_ous(ParentId):
    return (find(ParentId, organization_map)["OrganizationalUnits"])

def list_roots():
    return {
        "Roots": [
            {
                "Name": "root_name",
                "Id": "root_id"
            }
        ]
    }