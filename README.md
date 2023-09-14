conan_build
=======

conan_build is tool-project used for build pre-compiled libraries for [Creality 创想三维](https://www.creality.cn/) desktop software.
It's based on conan.

relates
-------------

- [Python 3.9](https://www.python.org/)
- [CMake 3.23 or higher](https://cmake.org/)
- [Conan >=1.50 <=1.56.0](https://conan.io/)
- [Qt5.13.2](https://www.qt.io/)
- Compile toolchains
  - Windows: Visual Studio with MSVC 2019 or higher
  - MacOS: XCode 13.2
  - Linux: GCC9

libs repositories
-----------

- [spdlog](https://github.com/CrealityOfficial/cxlog)
- [cxbin](https://github.com/CrealityOfficial/cxbin)
- [osswrapper](https://github.com/CrealityOfficial/osswrapper)
- [thumbnail](https://github.com/CrealityOfficial/thumbnail)
- [libnest2d](https://github.com/CrealityOfficial/libnest2d)
- [nestplacer](https://github.com/CrealityOfficial/nestplacer)
- [qhullwrapper](https://github.com/CrealityOfficial/qhullwrapper)
- [quazip](https://github.com/CrealityOfficial/quazip)
- [enchase](https://github.com/CrealityOfficial/enchase)
- [clipper](https://github.com/CrealityOfficial/clipper)
- [clipper3r](https://github.com/CrealityOfficial/clipper3r)
- [polyclipping](https://github.com/CrealityOfficial/polyclipping)
- [sensors_analytics_sdk](https://github.com/CrealityOfficial/sensors_analytics_sdk)
- [splitslot](https://github.com/CrealityOfficial/splitslot)
- [ffmpeglib](https://github.com/CrealityOfficial/ffmpeglib)

- [libqrencode](https://github.com/CrealityOfficial/libqrencode)
- [cpr](https://github.com/CrealityOfficial/cpr)
- [glew](https://github.com/CrealityOfficial/glew)
- [qrlib](https://github.com/CrealityOfficial/qrlib)
- [cereal](https://github.com/CrealityOfficial/cereal)
- [stb](https://github.com/CrealityOfficial/stb)
- [fmt](https://github.com/CrealityOfficial/fmt)
- [ovdbutil](https://github.com/CrealityOfficial/ovdbutil)
- [aliyunoss](https://github.com/CrealityOfficial/aliyunoss)
- [eigen](https://github.com/CrealityOfficial/eigen)
- [clipper2](https://github.com/CrealityOfficial/clipper2)
- [opencascade](https://github.com/CrealityOfficial/opencascade)
- [admesh](https://github.com/CrealityOfficial/admesh)
- [freetype](https://github.com/CrealityOfficial/freetype)
- [tbb](https://github.com/CrealityOfficial/tbb)
- [libtess2](https://github.com/CrealityOfficial/libtess2)

## build 

windows

```Shell
set QT5_DIR=%QTDIR%
git clone https://github.com/CrealityOfficial/conan_build.git
cd conan-build
git submodule update --init
copy file conan-build/profiles/desktop/win to the location of conan .conan/profiles/
create_patch.py -n opensource-win -f patches/CrealityPrint.patch -u False
```

Mac

```Shell
export QT5_DIR=$QTDIR
git clone https://github.com/CrealityOfficial/conan_build.git
cd conan-build
git submodule update --init
copy file conan-build/profiles/desktop/mac to the location of conan .conan/profiles/
python3 create_patch.py -n opensource-mac -f patches/CrealityPrint.patch -u False
```

Linux

```Shell
export QT5_DIR=$QTDIR
git clone https://github.com/CrealityOfficial/conan_build.git
cd conan-build
git submodule update --init
cp ./profiles/desktop/linux ~/.conan/profiles/linux
python3 create_patch.py -n opensource-linux -f patches/CrealityPrint.patch -u False
```

You can also build conan libs separately

```Plain
python3 create_patch.py -n opensource-linux -f patches/sub1.patch
python3 create_patch.py -n opensource-linux -f patches/sub2.patch
python3 create_patch.py -n opensource-linux -f patches/sub3.patch
python3 create_patch.py -n opensource-linux -f patches/sub4.patch
```



license
-------

conan_build as a whole is licensed under the GNU General Public License, Version 3.
