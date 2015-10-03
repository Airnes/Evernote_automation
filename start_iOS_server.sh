#!/bin/bash

appium --command-timeout "7200" --debug-log-spacing --platform-version "8.4" --platform-name "iOS" --app "/Users/Airness/Projects/Evernote_automation/apps/evernote.app" --full-reset --show-ios-log --device-name "iPad Air" --native-instruments-lib &

