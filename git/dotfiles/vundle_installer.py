import os
import re
import subprocess


def get_vimrc_locations():
    version_info = subprocess.check_output("vim --version", shell=True)
    return [os.path.expandvars(x) for x in re.findall(r'"(.*[_\.]g?vimrc)"', version_info.decode('utf-8'))]


def get_git_repo(bundle_str):
    parts = bundle_str.split("/")
    if len(parts) == 2:
        return 'https://github.com/%s/%s.git' % (parts[0], parts[1])
    else:
        return bundle_str


def getstatusoutput(cmd):
    try:
        data = subprocess.check_output(cmd, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
        status = 0
    except subprocess.CalledProcessError as ex:
        data = ex.output
        status = ex.returncode
    if data[-1:] == '\n':
        data = data[:-1]
    return status, data


def main():
    # Find Bundles
    bundles = []
    regex = re.compile('(?:plugin|bundle)\s+\'(.*)\'', re.IGNORECASE)
    for vimrc_file in get_vimrc_locations():
        vimrc = open(vimrc_file, "r").read()
        bundles += re.findall(regex, vimrc)

    # Create Bundle Directory for Vundle to install to
    bundle_dir = os.path.expandvars("$HOME/.vim/bundle/")
    if not os.path.exists(bundle_dir):
        os.makedirs(bundle_dir)

    # Install Plugins to Bundle Dir
    for bundle in set(bundles):
        url = get_git_repo(bundle)
        dest_folder = url.split("/")[-1].split(".git")[0]
        clone_command = 'git clone --depth 1 --recursive %(git_repo)s %(destination)s' % {
            'git_repo': url,
            'destination': os.path.normpath('%s/%s' % (bundle_dir, dest_folder)),
        }
        print("Installing %s" % bundle)
        status = getstatusoutput(clone_command)
        if status[0] is not 0:
            print(status[1])

if __name__ == '__main__':
    main()
