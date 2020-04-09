Introduction
------------

This module will create an Android apk programmatically (dynamically), from an Android project, faster and without Android Studio.

## Installation
Install via pip:

    pip install os-android-apk-builder

## Quick Usage       
From Python:
    
    import os_android_apk_builder.ApkBuilder as ab
    
    ab.run('/path/to/android/project', '/apk/desired/path')
  
Or from the command line:

    python3 -c 'import os_android_apk_builder.ApkBuilder as ab; ab.run("/path/to/android/project", "/apk/desired/path")'

## Advanced Usage
You can save your Key Store properties in a file, to avoid supplying them again in each apk build.

Todo so, create a json file (or copy this [sign_in_example.json](sign_in_example.json) file): 

        {
          "storeFile": "path/to/keystore_file.keystore",
          "storePassword": "myCoolKeyStorePass",
          "keyAlias": "myAliasName",
          "keyPassword": "myAliasPassword"
        }

 file) and then point to this file from the command:

    ab.run('/path/to/android/project', '/apk/desired/path', sign_in_file_path='/home/programming/jks_passes.json')
    

If the gradle wrapper isn't good enough, you can run the gradle from your system. Just supply it's path:

    ab.run('/path/to/android/project', '/apk/desired/path', '/path/to/gradle') 
(you can write just 'gradle' if it's already recognized by your environment variables).


## Licence
MIT