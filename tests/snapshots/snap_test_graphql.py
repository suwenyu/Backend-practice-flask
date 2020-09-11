# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['APITestCase::test_api_me 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 1
                }
            ],
            'message': 'Field "allUsers" of type "UserGraphSchemaConnection" must have a sub selection.'
        }
    ]
}

snapshots['APITestCase::test_graphql_all_posts 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 4,
                    'line': 1
                }
            ],
            'message': 'Field "allPosts" of type "PostGraphSchemaConnection" must have a sub selection.'
        }
    ]
}

snapshots['APITestCase::test_graphql_all_users 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 1
                }
            ],
            'message': 'Field "allUsers" of type "UserGraphSchemaConnection" must have a sub selection.'
        }
    ]
}
