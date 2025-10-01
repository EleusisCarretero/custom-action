import requests
import argparse


def execute_get(endpoint, params={}):
    response = requests.get(endpoint, params=params)
    print("================================")
    print(f"Status response: {response.status_code}")
    print("================================")
    print(f"Data response: {response.json()}")
    print("================================")

if __name__=="__main__":
    parser = argparse.ArgumentParser(
        prog='Getting API response',
        description='GET command from some API',
        epilog='The epilogation'
    )
    parser.add_argument(
        "-e",
        "--endpoint",
        help="The endppoint form the API",
        default="https://petstore.swagger.io/v2/pet/findByStatus"
    )
    parser.add_argument(
        "-p",
        "--params",
        help="The needed params for GET command if needed",
        default={'status':'avelable'}
    )
    args = parser.parse_args()
    execute_get(args.endpoint,args.params)
