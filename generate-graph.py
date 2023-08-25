import os
import sys, getopt
from xml.etree import ElementTree as ET
from graphviz import Digraph

def toDotID(name, version):
    v = version.replace('.', '_')
    n = name + "_" + v
    return n
    
def toDotName(name, version):
    n = name + "." + version
    return n    
    
if __name__ == "__main__":
    directory = sys.path[0]
    xml_file = directory + "/cmake/conan/graph/libs.xml"
    
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    dot = Digraph(comment='Gragh2Print')
    dot.graph_attr['rankdir'] = 'LR'

    libs = root.findall("lib")
    for lib in libs:
        sublibs = lib.findall("sublib")
        name = lib.attrib["name"]
        version = lib.attrib["version"]
        
        if len(sublibs) == 0:
            dot.node(toDotID(name, version), toDotName(name, version))
            
        for sub in sublibs:
            n = sub.attrib["name"]
            v = sub.attrib["version"]
            dot.edge(toDotID(name, version), toDotID(n, v))
            
    dot.render('./cmake/conan/graph/output', view=True)