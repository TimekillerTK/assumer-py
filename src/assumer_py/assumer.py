import shutil

green = '\x1b[38;5;76m'
grey = '\x1b[38;21m'
yellow = '\x1b[38;5;226m'
red = '\x1b[38;5;196m'
bold_red = '\x1b[31;1m'
reset = '\x1b[0m'

# Check if required packages are installed: aws, jq, fzf
#   Exit if this is not the case and show helpful error message!
def check_package_installed(package_list: list):
    """Checks if required packages are installed
    
    package_list(type list):
        List of packages to verify that they're installed"""
    
    missing_packages = []
    for package in package_list:
        result = shutil.which(package)
        if not result:
            missing_packages.append(package)
    
    if not missing_packages == []:
        print(f"{yellow}ERROR: The following required packages are not installed:")
        for package in missing_packages:
            print(f' - {package}')
        print(f"\n{reset}Install them using homebrew: https://brew.sh/ (macOS)")
        print("or using your system package manager (Linux)\n")
    

# Check if AWS CLI is NOT version 1.
#   Exit if this is not the case and show helpful error message!
def check_awscli_version():
    pass

# Check if AWS Config file exists.
#   Exit if this is not the case and show helpful error message!

# Determine the current path and make check whether script is sourced
#   Exit if this is not the case and show helpful error message!

# In case of arguments, check each arguments value and set var value, if exists
#    -h|--help)
#    -r|--role-name)
#    -e|--environment)
#    -f|--force)
#    -c|--create-csv)
#    -s|--superuser-role)
#    -p|--generate-profiles)
#    -d|--devops)
#    *) (bad syntax)

# This could be helpful with facilitating this issue
# if (__name__ == '__main__'):
#     import sys
#     if len(sys.argv) > 1:
#         print(fact(int(sys.argv[1])))

# Setting the environment default to prod

# Set Paths used by fzf_account_selector & default_roles

# Check if SSO token is active or has expired
#   Exit if this is not the case and show helpful error message!

# Removes other credentials that might conflict with assuming role
# (unset environment variables)

# Main Case Statement here 
# createcsv)
# superuserrole)
# devops)
# generateprofiles)
# *) (set default profile)

# Cleanup 
# unset SUFFIX ACCOUNT_LIST ASSUME_PATH RUN_FUNCTION AWSACCOUNT ROLE_NAME ACC_NAME FORCE_FLAG AWS_CONFIG_PROFILE_SSO_START_URL AWS_CONFIG_PROFILE_SSO_ROLE_NAME AWS_CONFIG_PROFILE_SSO_ACCOUNT_ID 
