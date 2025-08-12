# config.py
import os

def set_django_env(default_env='dev'):
    env = os.getenv('DJANGO_ENV', default_env)

    env_map = {
        'dev': 'rsite.settings.dev',
        'prod': 'rsite.settings.prod',
        # 'local_gunicorn': 'rsite.settings.local_gunicorn',
    }

    settings_module = env_map.get(env)

    if settings_module:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    else:
        raise ValueError(f"❌ Unknown DJANGO_ENV: '{env}'. Expected one of {list(env_map.keys())}")