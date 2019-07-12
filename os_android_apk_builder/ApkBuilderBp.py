import os
import os_tools.FileHandler as fh
import os_tools.Tools as tools
import os_android_apk_builder.SigninConfigHandler as sch

##################################################################################
#
# just a boilerPlate for the apk release
#
##################################################################################


# finals

# paths
PATH_APK_RELEASE = "/app/build/outputs/apk/release/app-release.apk"

# cmd commands
COMMAND_GRADLE_ASSEMBLE_RELEASE = " assembleRelease"


# this method meant to check if the option of automatic release is enabled in the gradle
def check_if_release_enabled(path):
    build_gradle_file = path + "/app/build.gradle"
    release_command = "signingConfig signingConfigs.release"
    return fh.is_line_exists_in_file(build_gradle_file, release_command)


# this method meant to create a new release
def assemble_release(path, gradle_path):
    cd_command = "cd " + path
    gradle_command = gradle_path + COMMAND_GRADLE_ASSEMBLE_RELEASE
    full_command = cd_command + " && " + gradle_command
    os.system(full_command)


def obtain_version_code(project_path):
    build_gradle_file = project_path + "/app/build.gradle"
    line = fh.get_line_from_file(build_gradle_file, "versionCode")
    last_space_idx = line.rfind(" ")
    new_line = line.rfind("\n")
    version_code = line[last_space_idx + 1:new_line]
    return version_code


# this method meant to move the apk made to a new location
def copy_apk_to_path(project_path, apk_desired_path, var_code):
    apk_path = apk_desired_path + "/" + var_code + ".apk"
    fh.copy_file(project_path + PATH_APK_RELEASE, apk_path)
    return apk_path


def is_apk_exists(project_path):
    return fh.is_file_exists(project_path + PATH_APK_RELEASE)


def remove_older_apks(apk_desired_path):
    fh.remove_all_files_with_extension(apk_desired_path, 'apk')


# will fetch the sign in params (key store props)
def fetch_sign_in_params(sign_in_file_path):
    if sign_in_file_path is not None:
        return fetch_params_from_sign_in_file(sign_in_file_path)
    else:
        return fetch_params_from_user_input()


# will fetch the sign in params from the json file
def fetch_params_from_sign_in_file(sign_in_file_path):
    return fh.json_file_to_dict(sign_in_file_path)


# will ask the user for his key store params
def fetch_params_from_user_input():
    sign_in_params_dict = {'$key_store_path': tools.ask_for_input('Key store (.jks file) path:'),
                           '$key_store_pass': tools.ask_for_input('Key store password:'),
                           '$key_store_alias_name': tools.ask_for_input('Key store alias name:'),
                           '$key_store_alias_pass': tools.ask_for_input('Key store alias password:')}
    tools.print_arr(sign_in_params_dict.values(), ',')
    return sign_in_params_dict


def append_sign_in_config_to_gradle(project_path, sign_in_config_file, sign_in_params_dict):
    sch.append_sign_in_config_to_gradle(project_path, sign_in_config_file, sign_in_params_dict)


def remove_sign_in_config_from_gradle(project_path):
    sch.remove_sign_in_config_from_gradle(project_path)


# will search for the buildConfigTemplate file and return it
def find_sign_in_config_file():
    return fh.search_file(fh.get_parent_path(__file__), 'buildConfigTemplate.txt')


# will get the default gradle path from the project
def get_default_gradle_path(project_path):
    return project_path + '/' + 'gradlew'
