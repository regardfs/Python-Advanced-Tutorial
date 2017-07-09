#!/usr/bin/env python

import commands
import re

ENV_PROJECT_MAP = {
    "DEV": {"athena": 9035},
    "SIT": {"athena": 8035},
    "PREPROD": {"athena": 7035},
    "PROD": {"athena": 6035}
}

ENV_GIT_BRANCH_MAP = {
    "DEV": re.compile("dev"),
    "SIT": re.compile('release/\d\.'),
    "PREPROD": re.compile('pre'),
    "PROD": re.compile('master')
}


class RuntimeEnvSet:

    def __init__(self):
        return None

    @staticmethod
    def get_runtime_git_branch():
        runtime_branch = commands.getstatusoutput('git branch|grep \"^\*\"|awk \'{ print $2}\'')[1]
        return runtime_branch

    @staticmethod
    def judge_runtime_env(branch_name=None):
        runtime_branch = branch_name if branch_name is not None else RuntimeEnvSet.get_runtime_git_branch()
        for key, value in ENV_GIT_BRANCH_MAP.iteritems():
            if value.match(runtime_branch):
                return key






