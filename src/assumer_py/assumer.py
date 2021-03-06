import shutil
import subprocess
import sys
import os
import assumer_py.colours as col

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
        print(f"{col.yellow}ERROR: The following required packages are not installed:")
        for package in missing_packages:
            print(f' - {package}')
        print(f"\n{col.reset}Install them using homebrew: https://brew.sh/ (macOS)")
        print("or using your system package manager (Linux)\n")
        sys.exit(1)
    

# For running a CLI command from Python
def aws_cli_command(command):
    try:
        command_output = subprocess.run(["sh", "-c", f"{command}"], 
                                        capture_output=True, 
                                        encoding="utf-8",
                                        check=True,
                                        timeout=3)                         

    except FileNotFoundError as e:
        print(f"{col.red}sh command not found:\n {e}{col.reset}")
        sys.exit(1)
    
    except subprocess.CalledProcessError as e:
        print(f"{col.red}AWS CLI raised error ({e.returncode}):")
        print(f"{e.stderr}{col.reset}")
        sys.exit(1)
        
    except subprocess.TimeoutExpired as e:
        print(f"{col.red}Command timed out:\n{e}{col.reset}")
        sys.exit(1)
    
    return command_output

# Check if AWS CLI is NOT version 1. (or  version specified)
#   Exit if this is not the case and show helpful error message!
def check_awscli_version():
    """Checks if AWS CLI is version 2 or above, error if not true."""   
    try:
        # TODO: this 'multisplit' can probably be done better
        check_result = aws_cli_command("aws --version").stdout.split('/')[1].split(" ")[0].split(".")[0]
        check_result_int = int(check_result)

    except AttributeError as error:
        print(f"{col.red}ERROR: {error}")
        sys.exit(1)

    match check_result_int:
        case x if x == 2:
            print(f"{col.green}SUCCESS{col.reset}")
            return True
        case x if x == 1:
            print(f"{col.red}ERROR: AWS CLI Version 1 is not supported")
            print(f"{col.reset} - Download and install AWS CLI version 2")
            sys.exit(1)
        case x if x > 2:
            print(f"{col.yellow}WARNING: AWS CLI Version is higher than 2") 
            print(f"{col.reset}Some things may be broken!!!")
        case _:
            print(f"{col.red}ERROR: Error while checking AWS CLI version")
            sys.exit(1)

# Check if AWS Config file exists.
#   Exit if this is not the case and show helpful error message!
def check_awscli_config():
    path = f"{os.path.expanduser('~')}/.aws/config"
    check = os.path.exists(path)
    if not check:
        print(f"{col.red}AWS config file does not exist in expected path:")
        print(f" - {path}{col.reset}\n")
        print(f"Check official documentation on how to set up an AWS SSO profile:")
        print(f" - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html")
        sys.exit(1)

# Spit out help message in case 
def assumer_help():
    """Spits out help"""

    help = """\n
    Command usage:
        - assumer [-r|--rolename ROLENAME]
        - assumer [-c|--createcsv]
        - assumer [-s|--superuser-role]
        - assumer [-d|--devops]
      
    EXAMPLES:
      Assume Role in account X
        - assumer 
    """
    return help


# Determine the current path and make check whether script is sourced 
#   Exit if this is not the case and show helpful error message!
def get_aws_profile_info(profile):

    #TODO: Broken, needs fix
    sso_account_id = aws_cli_command(f"aws configure get \"{profile}\".sso_account_id")
    sso_role_name  = aws_cli_command(f"aws configure get \"{profile}\".sso_role_name")
    sso_start_url  = aws_cli_command(f"aws configure get \"{profile}\".sso_start_url")
    
    return [sso_role_name,sso_account_id,sso_start_url]



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
