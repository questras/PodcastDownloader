import requests

RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
STOP = '\033[0m'


def print_error(message):
    print(f'{RED}[ERROR]: {message}{STOP}')


def print_info(message):
    print(f'{BLUE}[INFO]: {message}{STOP}')


def print_success(message):
    print(f'{GREEN}[SUCCESS]: {message}{STOP}')


def request_has_errors(request):
    """Print adequate error message if an error occures.
    Return True if errors occure, False otherwise.
    """

    try:
        request.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print_error("Could not connect.")
        return True

    return False
