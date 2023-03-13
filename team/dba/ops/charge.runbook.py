import os
import http
import time

def main():
    print(os.environ)
    time.sleep(20)
    amount = {{ .amount 
    | type "number"
    | required "amount is required"
    | description "The amount to charge it" }}
    print('AMOUNT', amount)

if __name__ == '__main__':
    main()
