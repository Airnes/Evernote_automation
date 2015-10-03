# Appium Automation for Evernote

##Environment:
####Appium
- brew install node
- npm install -g appium
- npm install wd

####Python library for Appium
- pip install Appium-Python-Client
- pip install behave
- pip install loremipsum

###How to run
1. Open terminal and execute sh file "*start_$PLATFORM_server.sh*" for choosen Platform
2. Open environment.py file and change app path
3. Cd to the Features folder and do "*cp .behaverc $HOME*"
4. Run Run "*behave -D platform=(iOS/Android)*"
