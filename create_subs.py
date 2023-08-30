import sys;
sys.path.append('./cmake/python/')

import createUtil
import sys, getopt
import os

if __name__ == "__main__":
    directory = sys.path[0]
    argv = sys.argv[1:]
    xml_file = directory + "/cmake/conan/graph/libs.xml"
    
    name = ''
    file = ''
    try:
        opts, args = getopt.getopt(argv,"n:f:")
    except getopt.GetoptError:
        print("create.py -n <name>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-n"):
            name = arg
        if opt in ("-f"):
            file = arg
            
    libs = createUtil.create_libs_from_txt(file)
    createUtil.build_recipes(libs, createUtil.get_channel_from_type(name), createUtil.get_profile_from_type(name), xml_file)