#!/usr/bin/env python3

import os

'''
{{ .wallet_id 
  | description "the id of the wallet"
  | required "wallet_id is required"
  | type "number"
  | asenv "WALLET_ID" }}

{{ .debug 
    | description "turn on debugging"
    | type "text"
    | asenv "DEBUG" }}
'''

def do_transfer(wal_id):
    print('performing wallet transfer to: {}'.format(wal_id))

def do_log():
    if os.environ.get("DEBUG") == "true":
        print('debug is turned on, debuggingg!!')

if __name__ == "__main__":
    wallet_id = os.environ['WALLET_ID']
    do_transfer(wallet_id)
    do_log()
