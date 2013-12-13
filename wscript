#!/usr/bin/env python
import sys, os

def options(opt):
    opt.load('gxx')
    opt.load('boost')
    opt.load('python')

def configure(cfg):
    cfg.load('gxx')
    cfg.load('boost')
    cfg.load('python')

    cfg.check_python_version(minver=(2,5))
    cfg.check_python_headers()
    cfg.check_boost(lib='python', uselib_store='PYUBLAS_BOOST')

    try:
        from numpy.distutils.misc_util import get_numpy_include_dirs
    except ImportError:
        cfg.fatal("Numpy is required")

def build(bld):
    from numpy.distutils.misc_util import get_numpy_include_dirs
    flags = { "cxxflags"  : ['-std=c++0x', '-fPIC',
                             '-Wall', '-Wextra', '-Wno-long-long', '-Wno-deprecated', '-Wno-format', ],
              "linkflags" : ['-Wl,-z,defs'],
    }

    sources = [
            'src/wrapper/converters.cpp',
    #        'src/wrapper/sparse_build.cpp',
    #        'src/wrapper/sparse_execute.cpp',
            'src/module/pyublas_module.cpp',
        ]

    bld(
            target  = 'pyublas_inc',
            export_includes = ['pyublas/include'] + \
                    get_numpy_include_dirs() + \
                    bld.env.INCLUDES_PYEMBED,
            use = ['PYUBLAS_BOOST'])

    bld(
            target          = 'pyublas',
            features        = 'cxx cxxshlib pyembed pyext',
            source          = sources,
            use             = ['pyublas_inc'],
            install_path    = '${PREFIX}/lib',
            **flags
    )
