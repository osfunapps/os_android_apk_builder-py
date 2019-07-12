import fileinput
import sys
import os_tools.StringUtils as su
import os_tools.FileHandler as fh

##################################################################################
#
# just a handler script for the signin copying and deleting from the gradle file
#
##################################################################################

# build.gradle place holders
PH_ANDROID = ['android', '{']
PH_BUILD_TYPES = ['buildTypes', '{']
PH_RELEASE = ['release', '{']
PH_GRADLE_LOG_SIGNATURE = 'apk_builder'
PH_GRADLE_LOG_SIGN_IN_START = '    // ' + PH_GRADLE_LOG_SIGNATURE + ' -> auto generated sign in config start'
PH_GRADLE_LOG_SIGN_IN_END = '    // ' + PH_GRADLE_LOG_SIGNATURE + ' -> auto generated sign in config end'
PH_GRADLE_LOG_SIGN_IN_RELEASE = '            signingConfig signingConfigs.release  // ' + PH_GRADLE_LOG_SIGNATURE + ' -> auto generated sign in config release\n'


# will add the user signed in params to the gradle
def append_sign_in_config_to_gradle(project_path, sign_in_config_file, sign_in_params_dict):
    build_gradle_file = project_path + "/app/build.gradle"
    on_android_par = False
    on_build_types_par = False
    added_signin = False

    for line in fileinput.input(build_gradle_file, inplace=1):
        sys.stdout.write(line)
        sanitized_line = su.str_to_words(line, ['{'])
        if sanitized_line == PH_ANDROID:
            on_android_par = True

        # on android parenthesis (android {)
        if on_android_par:

            if not added_signin:
                sys.stdout.write(PH_GRADLE_LOG_SIGN_IN_START)
                sys.stdout.write('\n')
                append_signin_file_lines(sign_in_config_file, sign_in_params_dict)
                sys.stdout.write('\n')
                sys.stdout.write(PH_GRADLE_LOG_SIGN_IN_END)
                sys.stdout.write('\n')

                added_signin = True
                continue

            if sanitized_line == PH_BUILD_TYPES:
                on_build_types_par = True
                continue

            # on build types parenthesis (buildTypes {)
            if on_build_types_par:
                if sanitized_line == PH_RELEASE:
                    sys.stdout.write(PH_GRADLE_LOG_SIGN_IN_RELEASE)
                    continue


# will append the lines of the signin file, one by one, with the user sign in props
def append_signin_file_lines(sign_in_config_file, sign_in_params_dict):
    with open(sign_in_config_file) as f:
        build_settings_content = f.readlines()
        for line in build_settings_content:
            for key, val in sign_in_params_dict.items():
                if key in line:
                    line = line.replace(key, val)
                    break
            sys.stdout.write(line)


# will remove the user signed in params from the gradle, at the process end
def remove_sign_in_config_from_gradle(project_path):
    build_gradle_file = project_path + "/app/build.gradle"
    fh.remove_lines_from_file(build_gradle_file, [PH_GRADLE_LOG_SIGNATURE], PH_GRADLE_LOG_SIGN_IN_START, PH_GRADLE_LOG_SIGN_IN_END)
