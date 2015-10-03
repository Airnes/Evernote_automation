#!/bin/bash

appium --command-timeout "7200" --debug-log-spacing --automation-name "Appium" --platform-name "Android" --platform-version "5.1" --app "/Users/Airness/Projects/Evernote_automation/apps/evernote.apk" --full-reset --avd "Nexus5" --device-name "Nexus 5" &

