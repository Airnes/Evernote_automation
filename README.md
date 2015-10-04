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
1. Open *environment.py*, *start_$PLATFORM_server.sh* files and change app path
2. Open terminal and execute sh file ```start_$PLATFORM_server.sh``` for choosen Platform
3. Cd to the Features folder and do ```cp .behaverc $HOME```
4. Run ```$behave -D platform=iOS or Android --tags @iOS or Android```. Please add ```--junit``` option if needed 
5. Run ```killall -9 node``` to stop Appium server

#####Please make sure that Android SDK is installed and configured. At least one virtual/real android device must running before executing test script

#---------------------------------------#

######Pros
1. Python support
2. Unmodified test app
3. Cross Platform

######Cons
1. Very Slow
2. Limited API
3. Unsupported iOS 9 and Android M
4. Complicated setup and support
5. Server side required
6. Unable to check Runtime actions due to poor performance
7. No predefined steps available
8. Element_exists = true even if element is hidded or out of the screen

#Calabash

##Environment:
1. Open terminal and run ```gem install calabash-cucumber```
2. Cd to the project folder with *features* folder inside

###How to Run
- Run ```RESET_BETWEEN_SCENARIOS=1 cucumber features/evernote.feature```

#---------------------------------------#

######Pros
1. Huge Ruby API
2. iOS 9 support and Android M
3. Performance
4. Very easy to setup and configure
5. Easy to debug
6. Crossplatform
7. Stable

######Cons
1. Modefied iOS ipa/app file
2. Ruby language support only


