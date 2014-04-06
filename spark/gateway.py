import purl
import logging
import pprint

from . import exceptions

SCHEME = 'https'
HOST = 'api.spark.io'
DEFAULT_VERSION = 'v1'

# URL templates
URL_TEMPLATES = {
    'get_events': purl.Template('{/version}/devices{/device_id}/events/'),
    'post_message': purl.Template('{/version}/devices{/device_id}/'),
}

logger = logging.getLogger('Spark')


def fetch(method, url_template, url_params=None, payload=None):
    """
    Make an HTTP round-trip to Spark Cloud API
    """
    # Build URL
    if url_params is None:
        url_params = {}
    if not url_params.get('version', False):
        url_params['version'] = DEFAULT_VERSION
    url = url_template.expand(url_params)
    url = url.scheme(SCHEME).host(HOST).as_string()

    # Make request
    headers = {
        'Accept': 'application/json'}
    payload_json = None
    if payload:
        headers['Content-type'] = 'application/json'
        payload_json = json.dumps(payload)
    response = requests.request(method, url, data=payload_json, headers=headers)
    data = response.json()

    # Handle errors
    if not data.get('ok', False):
        error_messages = data.get('errors', [])
        logger.warning("Errors in response: %s", pprint.pformat(error_messages))
        raise exceptions.SparkException("Request was unsuccessful")
    return data


def get_events(coords, amount):
    """
    Open an event stream from a device

    http://docs.sparkdevices.com/
    """
    return fetch('GET', URL_TEMPLATES['get_events'])


def post_message(device_id, payload, api_version=None):
    """
    Post a message to a spark device

    http://docs.sparkdevices.com/
    """
    url_template = URL_TEMPLATES['post_message']
    url_params = {
        'device_id': device_id,
        'version': api_version
    }
    return fetch('POST', url_template, url_params=url_params, payload=payload)
