from fabric.api import run
from fabric.context_managers import settings, shell_env


def _get_manage_dot_py(host):
    return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/manage.py'


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'greg@{host}'):
        run(f'{manage_dot_py} flush --noinput')


def _get_server_env_vars(host):
    pid = run(f'pgrep -n -f {host}/virtualenv/bin/gunicorn').strip()
    env_lines = run(f'cat /proc/{pid}/environ').split('\x00')
    current_env = dict(l.split('=') for l in env_lines if l)
    return {
        'DJANGO_DEBUG_FALSE': current_env['DJANGO_DEBUG_FALSE'],
        'DJANGO_SECRET_KEY': current_env['DJANGO_SECRET_KEY'],
        'SITENAME': current_env['SITENAME'],
    }


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'greg@{host}'):
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):
            session_key = run(f'{manage_dot_py} create_session {email}')
            return session_key.strip()
