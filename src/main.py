#!/home/carlos/miniconda3/envs/az_learn_cli/bin/python3.12

import subprocess
import inject
import json
from Command import Command
from Config import Config
from IConfig import IConfig
from ILogger import ILogger
from Logger import Logger


config = json.load(open("./data/config.json"))
# logger = Logger()

def configure(binder):
    binder.bind(ILogger, Logger())
    binder.bind(IConfig, Config())
    

inject.configure(configure)
command = Command()

# RESOURCE_GROUP_NAME = config["resource_group_name"]
# LOCATION = config["location"]
# APP_SERVICE_PLAN_NAME = config["app_service_plan_name"]
# APP_SERVICE_NAME = config["app_service_name"]
# SERVICE_TIER = config["service_tier"]
# SERVICE_RUNTIME = config["service_runtime"]
# print(config)
RG_CREATION = [
    'az', 
    'group', 
    'create', 
    '--name', 
    config["resource_group_name"],
    '--location',
    config["location"]
]

APP_SERVICE_PLAN_CREATION = [
    'az',
    'appservice',
    'plan',
    'create',
    '--resource-group',
    config["resource_group_name"],
    '-n',
    config["app_service_plan_name"],
    '--sku',
    config["service_tier"],
    '--is-linux'
]

APP_SERVICE_CREATION = [
    'az',
    'webapp',
    'create',
    '--resource-group',
    config["resource_group_name"],
    '--plan',
    config["app_service_plan_name"],
    '--name',
    config["app_service_name"],
    '--runtime',
    config["service_runtime"]
]

APP_TEST_VERSION = [
    'az',
    'version'
]

command.runCommand(APP_TEST_VERSION)

# def printResult(result):
#     print('stdout:', result.stdout)
#     print('stderr:', result.stderr)
     


# runCommand(RG_CREATION)
# runCommand(APP_SERVICE_PLAN_CREATION)
# runCommand(APP_SERVICE_CREATION)
