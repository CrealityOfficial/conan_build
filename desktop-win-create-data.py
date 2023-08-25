import sys;
sys.path.append('./cmake/python/')

import createUtil
    
if __name__ == "__main__":
    params = createUtil.create_param_from_argv()
    params['channel'] = 'desktop/win'
    
    createUtil.invoke_conan_build_data(params)