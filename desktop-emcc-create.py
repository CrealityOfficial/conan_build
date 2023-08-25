import sys;
sys.path.append('./cmake/python/')

import createUtil
    
if __name__ == "__main__":
    params = createUtil.create_param_from_argv()
    params['channel'] = 'desktop/emscripten'
    params['profile'] = 'emscripten'
    subs = createUtil.create_sub_libs()
    
    createUtil.invoke_conan_build(params, subs)
    
    
    
