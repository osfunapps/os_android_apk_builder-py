import os_android_apk_builder.ApkBuilderBp as bp
import os_tools.LoggerHandler as lh


##################################################################################
#
# This module aim is to build an Android apk.
# the name of the released apk will be the versionName.apk
#
##################################################################################


def run(project_path, apk_desired_path, gradle_path=None, sign_in_file_path=None):
    """
    Will create an Android apk file

    Args:
        project_path: the path to your android app's project
        apk_desired_path: the path in which the made apk will be stored
        gradle_path: the path to your gradle file (if left blank, will use the gradle wrapper in the project).
        you can also use the gradle on your system by setting 'gradle'
        sign_in_file_path: if you have a sign in file you can set it here (read the github repo for more info) to save
        you the hassle of inserting the key store props each time
    """

    logger = lh.Logger(__file__)  # build the logger

    # check if can release
    is_release_enabled = bp.check_if_release_enabled(project_path)

    # permission checker action for the apk
    if not is_release_enabled:
        sign_in_params_dict = bp.fetch_sign_in_params(sign_in_file_path)
        sign_in_config_file = bp.find_sign_in_config_file()[0]
        bp.append_sign_in_config_to_gradle(project_path, sign_in_config_file, sign_in_params_dict)

    logger.info('copy sign in completed. starting apk build up')

    # create the apk
    if gradle_path is None:
        gradle_path = bp.get_default_gradle_path(project_path)
    bp.assemble_release(project_path, gradle_path)

    # obtain the version code
    var_code = bp.obtain_version_code(project_path)

    # if the apk creation failed, throw an exception
    if not bp.is_apk_exists(project_path):
        raise Exception("ERROR: Failed to create apk file")

    logger.info('gradle finished! removing older apk files from the dir...')

    # remove previous apks in the directory
    bp.remove_older_apks(apk_desired_path)

    logger.info('copying the new apk...')
    # copy the apk to the user desired location (with the file name as the version code).
    built_apk_path = bp.copy_apk_to_path(project_path, apk_desired_path, var_code)

    logger.info('sanitizing build.gradle file...')
    # revert the build.gradle file to it's previous form
    bp.remove_sign_in_config_from_gradle(project_path)

    logger.info('apk built successfully in:\n' + built_apk_path)
