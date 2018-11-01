from os import environ

def get_env(env_name):
  return environ[env_name]

def get_env_or(env_name, default):
  return get_env(env_name) if env_name in environ else default

class FlaskConfig:
  ENV = get_env_or("ENV", "development")
  DEBUG = bool(get_env_or("DEBUG", "True"))
  PORT = float(get_env_or("PORT", "3000"))

MysqlConfig = {
  "user": get_env("MYSQL_USERNAME"),
  "password": get_env("MYSQL_PASSWORD"),
  "host": get_env("MYSQL_HOST"),
  "database": get_env("MYSQL_DATABASE")
}
