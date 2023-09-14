import sys;
sys.path.append('./cmake/python/')

import createUtil
import sys, getopt
import os

if __name__ == "__main__":
    directory = sys.path[0]
    argv = sys.argv[1:]
    xml_file = directory + "/cmake/conan/graph/libs.xml"
    
    recipe = ''
    channel = ''
    upload = True
    try:
        opts, args = getopt.getopt(argv,"r:c:u:")
    except getopt.GetoptError:
        print("create.py -n <name>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-r"):
            recipe = arg
        if opt in ("-c"):
            channel = arg
        if opt in ("-u"):
            if arg != "True":
                upload = False
            
    libs = []
    libs.append(recipe)
    print('create recipes :' + str(libs))
    libDict = createUtil.create_base_libs_from_xml(xml_file)
    if not recipe in libDict.keys():
        sys.exit(-1)
        
    createUtil.build_recipes(libs, createUtil.get_channel_from_type(channel), createUtil.get_profile_from_type(channel), xml_file, upload)