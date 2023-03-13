import os
from pprint import pprint

def main():
    pprint(dict(os.environ))
    # {{ .amount | description "the amount to charge" | required "amount is required" | asenv "AMOUNT" }}
    # {{ .charge_id | type "text" | description "the id of the charge" | default "987" | asenv "CHARGE_ID" }}
    amount = os.getenv("AMOUNT")
    charge_id = os.getenv("CHARGE_ID")
    print('AMOUNT->>', amount)

if __name__ == '__main__':
    main()
