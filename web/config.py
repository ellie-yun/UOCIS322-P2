"""
Configure from
   app.ini
   credentials.ini
   command line  (unless invoked with proxied=True)
in that order (i.e., in opposite order of precedence).
A configuration namespace module returned by this module is
suitable for configuring a Flask applicaton object.
(Not relevant to project 1)
configparser makes all configuration variables  lower case;
Flask configuration object recognizes only upper case configuration
variables.  To resolve this conflict, we convert all configuration
variables from .ini files to upper case.
Potential extensions:
  - Use environment variables?  With what precedence relative
    to configuration files? (NO, for now)
"""


import configparser
import argparse
import os
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)

log = logging.getLogger(__name__)
HERE = os.path.dirname(__file__)

def command_line_args():
    """Returns namespace with settings from command line"""
    log.debug("-> Command line args")
    parser = argparse.ArgumentParser(description="CIS 322 Auto-Checker")
    cli_args = parser.parse_args()
    log.debug("<- Command line args: {}".format(cli_args))
    return cli_args

def config_file_args(config_file_paths):
    """Returns dict of values from the configuration files,
    accessing them in the order they appear in config_file_paths.
    """
    log.debug("-> config file args")
    config = configparser.ConfigParser()
    for path in config_file_paths:
        relative = os.path.join(HERE, path)
        if os.path.exists(path):
            log.info("Configuring from {}".format(path))
            config.read(path)
        elif os.path.exists(relative):
            log.info("Configuring from {}".format(relative))
            config.read(relative)
        else:
            log.info("No configuration file {}; skipping".format(path))
    args = config["DEFAULT"]
    return args

def configuration():
    """
    Returns namespace (that is, object) of configuration
    values, giving precedence to command line arguments over
    configuration file values.
    """
    log.debug("-> configuration")
    cli = command_line_args()
    cli_vars = vars(cli)  # Access the namespace as a dict
    log.debug("CLI variables: {}".format(cli_vars))
    config_file_paths = ["app.ini", "credentials.ini"]
    if cli_vars.get("config"):
        config_file_path.append(cli_vars.get("config"))
    log.debug("Will read config files from '{}'".format(config_file_paths))
    ini = config_file_args(config_file_paths)
    log.debug("Config file args: {}".format(ini))   
    # Fold into cli namespace with precedence for command line arguments
    for var_lower in ini:
        var_upper = var_lower.upper()
        log.debug("Variable '{}'".format(var_upper))
        if var_upper in cli_vars and cli_vars[var_upper]:
            log.debug("Overridden by cli val '{}'".format(cli_vars[var_upper]))
        else:
            log.debug("Storing in cli")
            cli_vars[var_upper] = ini[var_lower]
    return cli
