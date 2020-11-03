import argparse
import logging

import pandas as pd

from politylink.graphql.client import GraphQLClient

LOGGER = logging.getLogger(__name__)


def main(fp):
    gql_client = GraphQLClient()
    df = pd.read_csv(fp)
    gql_client.bulk_link(from_ids=df['from_id'], to_ids=df['to_id'])
    LOGGER.info(f'merged {len(df)} relationships')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Linkを手動で定義する')
    parser.add_argument('-f', '--file', default='./data/link.csv')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    logging.getLogger('sgqlc').setLevel(logging.INFO)
    main(args.file)
