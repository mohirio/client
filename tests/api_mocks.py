import pytest, os
from six import binary_type

def _files():
    return {
        'edges': [
            {'node': {
                'name': 'weights.h5',
                'url': 'https://weights.url'
            }},
            {'node': {
                'name': 'model.json',
                'url': 'https://model.url'
            }},
        ]
    }

def _model(name='test'):
    return {
        'name': name,
        'description': 'Test model',
        'bucket': {
            'framework': 'keras',
            'files': _files()
        }
    }

def _buckets(name='test'):
    return {
        'name': name,
        'description': "Description of the tag",
        'framework': 'keras',
        'files': _files()
    }

def _success_or_failure(payload=None):
    def wrapper(mocker, status_code=200, error=None):
        if error:
            body = {'error': error}
        else:
            body = {'data': payload}

        mocker.register_uri('POST', 'https://api.wandb.ai/graphql', 
            json=body, status_code=status_code)
    return wrapper

def _query(key, json):
    payload = {}
    if type(json) == list:
        json = {'edges': [{'node': item} for item in json]}
    payload[key] = json
    return _success_or_failure(payload=payload)

def _mutate(key, json):
    payload = {}
    payload[key]=json
    return _success_or_failure(payload=payload)

@pytest.fixture
def query_model():
    return _query('model', _model())

@pytest.fixture
def query_models():
    return _query('models', [_model("test_1"), _model("test_2"), _model("test_3")])

@pytest.fixture
def query_buckets():
    return _query('buckets', [_bucket("default"), _bucket("test_1")])

@pytest.fixture
def upload_url():
    def wrapper(mocker, status_code=200, headers={}):
        mocker.register_uri('PUT', 'https://weights.url', status_code=status_code, headers=headers)
        mocker.register_uri('PUT', 'https://model.url', status_code=status_code, headers=headers)
    return wrapper

@pytest.fixture
def download_url():
    def wrapper(mocker, status_code=200, error=None, size=5000):
        mocker.register_uri('GET', 'https://weights.url', 
            content=os.urandom(size), status_code=status_code)
        mocker.register_uri('GET', 'https://model.url', 
            content=os.urandom(size), status_code=status_code)
    return wrapper