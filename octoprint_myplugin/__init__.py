# coding=utf-8
from __future__ import absolute_import

__author__ = ""
__license__ = ""
__copyright__ = ""

import octoprint.plugin
import time
import os
import sys
from octoprint.events import eventManager, Events
from octoprint.server.util.flask import restricted_access
from octoprint.server import admin_permission
import json
import flask
import logging

class myplugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.AssetPlugin,
			    octoprint.plugin.SimpleApiPlugin,
                            octoprint.plugin.SettingsPlugin):

    def __init__(self):
	self.commandss=0

    def on_after_startup(self):
	self._logger.info("Starting myplugin Plugin")


    def get_api_commands(self):
	self._logger.info("Manually triggered get_api")
	return dict(turnOn=["ip"])


    def on_api_commands(self, command, data):
	if command == 'turnOn':
		self._logger.info("Manually triggered!")

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=True)
        ]

    def get_assets(self):
        return dict(
            js= ["js/myplugin.js"],
	    css= ["css/myplugin.css"]
        )

    def get_update_information(self):
        return dict(
            myplugin=dict(
                displayName="myplugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
		user="",
                repo="octoPrint-myplugin",
                current=self._plugin_version,

                # update method: pip w/ dependency links
                pip=""
            )
        )

__plugin_name__ = "myplugin"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = myplugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
