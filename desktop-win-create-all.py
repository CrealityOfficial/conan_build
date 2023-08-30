import sys;
sys.path.append('./cmake/python/')

import createUtil
import sys, getopt
import os
from xml.etree import ElementTree as ET

if __name__ == "__main__":
    directory = sys.path[0]
    xml_file = directory + "/cmake/conan/graph/libs.xml"
    
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    params = {'name':'xxx', 'version':'0.0.0', 'profile':'win', 'channel':'desktop/win'}

    recipes = []
    libs = root.findall("lib")
    for lib in libs:
        recipes.append(lib.attrib["name"])

    for recipe in recipes:
        seg = recipe.split('/')
        if len(seg) == 2:
            name = seg[0]
            version = seg[1]
            params['name'] = name
            params['version'] = version
            
            ref = recipe + '@desktop/win'
            cmd = 'conan upload ' + ref + ' -r artifactory --all -c'          
            
            subs = createUtil.create_sub_libs_from_xml(xml_file, name, version)
            createUtil.invoke_conan_build(params, subs)
            os.system(cmd)
               
    
    
    