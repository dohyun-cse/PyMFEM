# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_coefficient')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_coefficient')
    _coefficient = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_coefficient', [dirname(__file__)])
        except ImportError:
            import _coefficient
            return _coefficient
        try:
            _mod = imp.load_module('_coefficient', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _coefficient = swig_import_helper()
    del swig_import_helper
else:
    import _coefficient
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


MFEM_VERSION = _coefficient.MFEM_VERSION
MFEM_VERSION_STRING = _coefficient.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _coefficient.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _coefficient.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _coefficient.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _coefficient.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _coefficient.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _coefficient.MFEM_VERSION_PATCH
MFEM_GIT_STRING = _coefficient.MFEM_GIT_STRING
MFEM_TIMER_TYPE = _coefficient.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _coefficient.MFEM_HYPRE_VERSION
import array
import ostream_typemap
import matrix
import vector
import operators
import intrules
import sparsemat
import densemat
import eltrans
import fe
class Coefficient(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Coefficient, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Coefficient, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetTime(self, t):
        return _coefficient.Coefficient_SetTime(self, t)

    def GetTime(self):
        return _coefficient.Coefficient_GetTime(self)

    def Eval(self, *args):
        return _coefficient.Coefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_Coefficient
    __del__ = lambda self: None
Coefficient_swigregister = _coefficient.Coefficient_swigregister
Coefficient_swigregister(Coefficient)

class ConstantCoefficient(Coefficient):
    __swig_setmethods__ = {}
    for _s in [Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ConstantCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ConstantCoefficient, name)
    __repr__ = _swig_repr
    __swig_setmethods__["constant"] = _coefficient.ConstantCoefficient_constant_set
    __swig_getmethods__["constant"] = _coefficient.ConstantCoefficient_constant_get
    if _newclass:
        constant = _swig_property(_coefficient.ConstantCoefficient_constant_get, _coefficient.ConstantCoefficient_constant_set)

    def __init__(self, c=1.0):
        this = _coefficient.new_ConstantCoefficient(c)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, T, ip):
        return _coefficient.ConstantCoefficient_Eval(self, T, ip)
    __swig_destroy__ = _coefficient.delete_ConstantCoefficient
    __del__ = lambda self: None
ConstantCoefficient_swigregister = _coefficient.ConstantCoefficient_swigregister
ConstantCoefficient_swigregister(ConstantCoefficient)

class PWConstCoefficient(Coefficient):
    __swig_setmethods__ = {}
    for _s in [Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PWConstCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PWConstCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _coefficient.new_PWConstCoefficient(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def UpdateConstants(self, c):
        return _coefficient.PWConstCoefficient_UpdateConstants(self, c)

    def __call__(self, i):
        return _coefficient.PWConstCoefficient___call__(self, i)

    def GetNConst(self):
        return _coefficient.PWConstCoefficient_GetNConst(self)

    def Eval(self, T, ip):
        return _coefficient.PWConstCoefficient_Eval(self, T, ip)
    __swig_destroy__ = _coefficient.delete_PWConstCoefficient
    __del__ = lambda self: None
PWConstCoefficient_swigregister = _coefficient.PWConstCoefficient_swigregister
PWConstCoefficient_swigregister(PWConstCoefficient)

class FunctionCoefficient(Coefficient):
    __swig_setmethods__ = {}
    for _s in [Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FunctionCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, FunctionCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _coefficient.new_FunctionCoefficient(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, T, ip):
        return _coefficient.FunctionCoefficient_Eval(self, T, ip)
    __swig_destroy__ = _coefficient.delete_FunctionCoefficient
    __del__ = lambda self: None
FunctionCoefficient_swigregister = _coefficient.FunctionCoefficient_swigregister
FunctionCoefficient_swigregister(FunctionCoefficient)

class GridFunctionCoefficient(Coefficient):
    __swig_setmethods__ = {}
    for _s in [Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GridFunctionCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GridFunctionCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, gf, comp=1):
        this = _coefficient.new_GridFunctionCoefficient(gf, comp)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetGridFunction(self, gf):
        return _coefficient.GridFunctionCoefficient_SetGridFunction(self, gf)

    def GetGridFunction(self):
        return _coefficient.GridFunctionCoefficient_GetGridFunction(self)

    def Eval(self, T, ip):
        return _coefficient.GridFunctionCoefficient_Eval(self, T, ip)
    __swig_destroy__ = _coefficient.delete_GridFunctionCoefficient
    __del__ = lambda self: None
GridFunctionCoefficient_swigregister = _coefficient.GridFunctionCoefficient_swigregister
GridFunctionCoefficient_swigregister(GridFunctionCoefficient)

class TransformedCoefficient(Coefficient):
    __swig_setmethods__ = {}
    for _s in [Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TransformedCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TransformedCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _coefficient.new_TransformedCoefficient(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, T, ip):
        return _coefficient.TransformedCoefficient_Eval(self, T, ip)
    __swig_destroy__ = _coefficient.delete_TransformedCoefficient
    __del__ = lambda self: None
TransformedCoefficient_swigregister = _coefficient.TransformedCoefficient_swigregister
TransformedCoefficient_swigregister(TransformedCoefficient)

class DeltaCoefficient(Coefficient):
    __swig_setmethods__ = {}
    for _s in [Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DeltaCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DeltaCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _coefficient.new_DeltaCoefficient(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetDeltaCenter(self, center):
        return _coefficient.DeltaCoefficient_SetDeltaCenter(self, center)

    def SetScale(self, _s):
        return _coefficient.DeltaCoefficient_SetScale(self, _s)

    def SetFunction(self, f):
        return _coefficient.DeltaCoefficient_SetFunction(self, f)

    def SetTol(self, _tol):
        return _coefficient.DeltaCoefficient_SetTol(self, _tol)

    def SetWeight(self, w):

        w.thisown=0 


        return _coefficient.DeltaCoefficient_SetWeight(self, w)


    def Center(self):
        return _coefficient.DeltaCoefficient_Center(self)

    def Scale(self):
        return _coefficient.DeltaCoefficient_Scale(self)

    def Tol(self):
        return _coefficient.DeltaCoefficient_Tol(self)

    def Weight(self):
        return _coefficient.DeltaCoefficient_Weight(self)

    def GetDeltaCenter(self, center):
        return _coefficient.DeltaCoefficient_GetDeltaCenter(self, center)

    def EvalDelta(self, T, ip):
        return _coefficient.DeltaCoefficient_EvalDelta(self, T, ip)

    def Eval(self, T, ip):
        return _coefficient.DeltaCoefficient_Eval(self, T, ip)
    __swig_destroy__ = _coefficient.delete_DeltaCoefficient
    __del__ = lambda self: None
DeltaCoefficient_swigregister = _coefficient.DeltaCoefficient_swigregister
DeltaCoefficient_swigregister(DeltaCoefficient)

class RestrictedCoefficient(Coefficient):
    __swig_setmethods__ = {}
    for _s in [Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RestrictedCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RestrictedCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, _c, attr):
        this = _coefficient.new_RestrictedCoefficient(_c, attr)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        self._ref_to_c = _c




    def Eval(self, T, ip):
        return _coefficient.RestrictedCoefficient_Eval(self, T, ip)
    __swig_destroy__ = _coefficient.delete_RestrictedCoefficient
    __del__ = lambda self: None
RestrictedCoefficient_swigregister = _coefficient.RestrictedCoefficient_swigregister
RestrictedCoefficient_swigregister(RestrictedCoefficient)

class VectorCoefficient(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorCoefficient, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorCoefficient, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetTime(self, t):
        return _coefficient.VectorCoefficient_SetTime(self, t)

    def GetTime(self):
        return _coefficient.VectorCoefficient_GetTime(self)

    def GetVDim(self):
        return _coefficient.VectorCoefficient_GetVDim(self)

    def Eval(self, *args):
        return _coefficient.VectorCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_VectorCoefficient
    __del__ = lambda self: None
VectorCoefficient_swigregister = _coefficient.VectorCoefficient_swigregister
VectorCoefficient_swigregister(VectorCoefficient)

class VectorConstantCoefficient(VectorCoefficient):
    __swig_setmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorConstantCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, VectorConstantCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, v):
        this = _coefficient.new_VectorConstantCoefficient(v)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, *args):
        return _coefficient.VectorConstantCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_VectorConstantCoefficient
    __del__ = lambda self: None
VectorConstantCoefficient_swigregister = _coefficient.VectorConstantCoefficient_swigregister
VectorConstantCoefficient_swigregister(VectorConstantCoefficient)

class VectorFunctionCoefficient(VectorCoefficient):
    __swig_setmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorFunctionCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, VectorFunctionCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _coefficient.new_VectorFunctionCoefficient(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, *args):
        return _coefficient.VectorFunctionCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_VectorFunctionCoefficient
    __del__ = lambda self: None
VectorFunctionCoefficient_swigregister = _coefficient.VectorFunctionCoefficient_swigregister
VectorFunctionCoefficient_swigregister(VectorFunctionCoefficient)

class VectorArrayCoefficient(VectorCoefficient):
    __swig_setmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorArrayCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, VectorArrayCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, dim):
        this = _coefficient.new_VectorArrayCoefficient(dim)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetCoeff(self, i):
        return _coefficient.VectorArrayCoefficient_GetCoeff(self, i)

    def GetCoeffs(self):
        return _coefficient.VectorArrayCoefficient_GetCoeffs(self)

    def Set(self, i, c):

        c.thisown=0 


        return _coefficient.VectorArrayCoefficient_Set(self, i, c)


    def Eval(self, *args):
        return _coefficient.VectorArrayCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_VectorArrayCoefficient
    __del__ = lambda self: None
VectorArrayCoefficient_swigregister = _coefficient.VectorArrayCoefficient_swigregister
VectorArrayCoefficient_swigregister(VectorArrayCoefficient)

class VectorGridFunctionCoefficient(VectorCoefficient):
    __swig_setmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorGridFunctionCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, VectorGridFunctionCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, gf):
        this = _coefficient.new_VectorGridFunctionCoefficient(gf)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetGridFunction(self, gf):
        return _coefficient.VectorGridFunctionCoefficient_SetGridFunction(self, gf)

    def GetGridFunction(self):
        return _coefficient.VectorGridFunctionCoefficient_GetGridFunction(self)

    def Eval(self, *args):
        return _coefficient.VectorGridFunctionCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_VectorGridFunctionCoefficient
    __del__ = lambda self: None
VectorGridFunctionCoefficient_swigregister = _coefficient.VectorGridFunctionCoefficient_swigregister
VectorGridFunctionCoefficient_swigregister(VectorGridFunctionCoefficient)

class VectorDeltaCoefficient(VectorCoefficient):
    __swig_setmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorDeltaCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, VectorDeltaCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _coefficient.new_VectorDeltaCoefficient(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetDeltaCoefficient(self, _d):
        return _coefficient.VectorDeltaCoefficient_SetDeltaCoefficient(self, _d)

    def GetDeltaCoefficient(self):
        return _coefficient.VectorDeltaCoefficient_GetDeltaCoefficient(self)

    def SetDirection(self, _d):
        return _coefficient.VectorDeltaCoefficient_SetDirection(self, _d)

    def GetDeltaCenter(self, center):
        return _coefficient.VectorDeltaCoefficient_GetDeltaCenter(self, center)

    def EvalDelta(self, V, T, ip):
        return _coefficient.VectorDeltaCoefficient_EvalDelta(self, V, T, ip)

    def Eval(self, *args):
        return _coefficient.VectorDeltaCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_VectorDeltaCoefficient
    __del__ = lambda self: None
VectorDeltaCoefficient_swigregister = _coefficient.VectorDeltaCoefficient_swigregister
VectorDeltaCoefficient_swigregister(VectorDeltaCoefficient)

class VectorRestrictedCoefficient(VectorCoefficient):
    __swig_setmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorRestrictedCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, VectorRestrictedCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, vc, attr):
        this = _coefficient.new_VectorRestrictedCoefficient(vc, attr)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        self._ref_to_vc = vc




    def Eval(self, *args):
        return _coefficient.VectorRestrictedCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_VectorRestrictedCoefficient
    __del__ = lambda self: None
VectorRestrictedCoefficient_swigregister = _coefficient.VectorRestrictedCoefficient_swigregister
VectorRestrictedCoefficient_swigregister(VectorRestrictedCoefficient)

class MatrixCoefficient(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatrixCoefficient, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MatrixCoefficient, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetTime(self, t):
        return _coefficient.MatrixCoefficient_SetTime(self, t)

    def GetTime(self):
        return _coefficient.MatrixCoefficient_GetTime(self)

    def GetHeight(self):
        return _coefficient.MatrixCoefficient_GetHeight(self)

    def GetWidth(self):
        return _coefficient.MatrixCoefficient_GetWidth(self)

    def GetVDim(self):
        return _coefficient.MatrixCoefficient_GetVDim(self)

    def Eval(self, K, T, ip):
        return _coefficient.MatrixCoefficient_Eval(self, K, T, ip)
    __swig_destroy__ = _coefficient.delete_MatrixCoefficient
    __del__ = lambda self: None
MatrixCoefficient_swigregister = _coefficient.MatrixCoefficient_swigregister
MatrixCoefficient_swigregister(MatrixCoefficient)

class MatrixConstantCoefficient(MatrixCoefficient):
    __swig_setmethods__ = {}
    for _s in [MatrixCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatrixConstantCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [MatrixCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MatrixConstantCoefficient, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Eval(self, *args):
        return _coefficient.MatrixConstantCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_MatrixConstantCoefficient
    __del__ = lambda self: None
MatrixConstantCoefficient_swigregister = _coefficient.MatrixConstantCoefficient_swigregister
MatrixConstantCoefficient_swigregister(MatrixConstantCoefficient)

class MatrixFunctionCoefficient(MatrixCoefficient):
    __swig_setmethods__ = {}
    for _s in [MatrixCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatrixFunctionCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [MatrixCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MatrixFunctionCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _coefficient.new_MatrixFunctionCoefficient(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, K, T, ip):
        return _coefficient.MatrixFunctionCoefficient_Eval(self, K, T, ip)
    __swig_destroy__ = _coefficient.delete_MatrixFunctionCoefficient
    __del__ = lambda self: None
MatrixFunctionCoefficient_swigregister = _coefficient.MatrixFunctionCoefficient_swigregister
MatrixFunctionCoefficient_swigregister(MatrixFunctionCoefficient)

class MatrixArrayCoefficient(MatrixCoefficient):
    __swig_setmethods__ = {}
    for _s in [MatrixCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatrixArrayCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [MatrixCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MatrixArrayCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, dim):
        this = _coefficient.new_MatrixArrayCoefficient(dim)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetCoeff(self, i, j):
        return _coefficient.MatrixArrayCoefficient_GetCoeff(self, i, j)

    def Set(self, i, j, c):

        c.thisown=0 


        return _coefficient.MatrixArrayCoefficient_Set(self, i, j, c)


    def Eval(self, *args):
        return _coefficient.MatrixArrayCoefficient_Eval(self, *args)
    __swig_destroy__ = _coefficient.delete_MatrixArrayCoefficient
    __del__ = lambda self: None
MatrixArrayCoefficient_swigregister = _coefficient.MatrixArrayCoefficient_swigregister
MatrixArrayCoefficient_swigregister(MatrixArrayCoefficient)

class MatrixRestrictedCoefficient(MatrixCoefficient):
    __swig_setmethods__ = {}
    for _s in [MatrixCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatrixRestrictedCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [MatrixCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MatrixRestrictedCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, mc, attr):
        this = _coefficient.new_MatrixRestrictedCoefficient(mc, attr)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        self._ref_to_mc = mc




    def Eval(self, K, T, ip):
        return _coefficient.MatrixRestrictedCoefficient_Eval(self, K, T, ip)
    __swig_destroy__ = _coefficient.delete_MatrixRestrictedCoefficient
    __del__ = lambda self: None
MatrixRestrictedCoefficient_swigregister = _coefficient.MatrixRestrictedCoefficient_swigregister
MatrixRestrictedCoefficient_swigregister(MatrixRestrictedCoefficient)


def ComputeLpNorm(*args):
    return _coefficient.ComputeLpNorm(*args)
ComputeLpNorm = _coefficient.ComputeLpNorm

def ComputeGlobalLpNorm(*args):
    return _coefficient.ComputeGlobalLpNorm(*args)
ComputeGlobalLpNorm = _coefficient.ComputeGlobalLpNorm

def fake_func(x):
    return _coefficient.fake_func(x)
fake_func = _coefficient.fake_func

def fake_func_vec(x, Ht):
    return _coefficient.fake_func_vec(x, Ht)
fake_func_vec = _coefficient.fake_func_vec

def fake_func_mat(x, Kt):
    return _coefficient.fake_func_mat(x, Kt)
fake_func_mat = _coefficient.fake_func_mat
class PyCoefficientBase(FunctionCoefficient):
    __swig_setmethods__ = {}
    for _s in [FunctionCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyCoefficientBase, name, value)
    __swig_getmethods__ = {}
    for _s in [FunctionCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PyCoefficientBase, name)
    __repr__ = _swig_repr

    def __init__(self, tdep):
        if self.__class__ == PyCoefficientBase:
            _self = None
        else:
            _self = self
        this = _coefficient.new_PyCoefficientBase(_self, tdep)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, T, ip):
        return _coefficient.PyCoefficientBase_Eval(self, T, ip)

    def _EvalPy(self, arg0):
        return _coefficient.PyCoefficientBase__EvalPy(self, arg0)

    def _EvalPyT(self, arg0, arg1):
        return _coefficient.PyCoefficientBase__EvalPyT(self, arg0, arg1)
    __swig_destroy__ = _coefficient.delete_PyCoefficientBase
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _coefficient.disown_PyCoefficientBase(self)
        return weakref_proxy(self)
PyCoefficientBase_swigregister = _coefficient.PyCoefficientBase_swigregister
PyCoefficientBase_swigregister(PyCoefficientBase)

class VectorPyCoefficientBase(VectorFunctionCoefficient):
    __swig_setmethods__ = {}
    for _s in [VectorFunctionCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorPyCoefficientBase, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorFunctionCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, VectorPyCoefficientBase, name)
    __repr__ = _swig_repr

    def __init__(self, dim, tdep, q=None):
        if self.__class__ == VectorPyCoefficientBase:
            _self = None
        else:
            _self = self
        this = _coefficient.new_VectorPyCoefficientBase(_self, dim, tdep, q)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, *args):
        return _coefficient.VectorPyCoefficientBase_Eval(self, *args)

    def _EvalPy(self, arg0, arg1):
        return _coefficient.VectorPyCoefficientBase__EvalPy(self, arg0, arg1)

    def _EvalPyT(self, arg0, arg1, arg2):
        return _coefficient.VectorPyCoefficientBase__EvalPyT(self, arg0, arg1, arg2)
    __swig_destroy__ = _coefficient.delete_VectorPyCoefficientBase
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _coefficient.disown_VectorPyCoefficientBase(self)
        return weakref_proxy(self)
VectorPyCoefficientBase_swigregister = _coefficient.VectorPyCoefficientBase_swigregister
VectorPyCoefficientBase_swigregister(VectorPyCoefficientBase)

class MatrixPyCoefficientBase(MatrixFunctionCoefficient):
    __swig_setmethods__ = {}
    for _s in [MatrixFunctionCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatrixPyCoefficientBase, name, value)
    __swig_getmethods__ = {}
    for _s in [MatrixFunctionCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MatrixPyCoefficientBase, name)
    __repr__ = _swig_repr

    def __init__(self, dim, tdep):
        if self.__class__ == MatrixPyCoefficientBase:
            _self = None
        else:
            _self = self
        this = _coefficient.new_MatrixPyCoefficientBase(_self, dim, tdep)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, K, T, ip):
        return _coefficient.MatrixPyCoefficientBase_Eval(self, K, T, ip)

    def _EvalPy(self, arg0, arg1):
        return _coefficient.MatrixPyCoefficientBase__EvalPy(self, arg0, arg1)

    def _EvalPyT(self, arg0, arg1, arg2):
        return _coefficient.MatrixPyCoefficientBase__EvalPyT(self, arg0, arg1, arg2)
    __swig_destroy__ = _coefficient.delete_MatrixPyCoefficientBase
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _coefficient.disown_MatrixPyCoefficientBase(self)
        return weakref_proxy(self)
MatrixPyCoefficientBase_swigregister = _coefficient.MatrixPyCoefficientBase_swigregister
MatrixPyCoefficientBase_swigregister(MatrixPyCoefficientBase)


class PyCoefficient(PyCoefficientBase):
   def __init__(self):
       PyCoefficientBase.__init__(self, 0)
   def _EvalPy(self, x):
       return self.EvalValue(x.GetDataArray())
   def EvalValue(self, x):
       return 0.0

class PyCoefficientT(PyCoefficientBase):
   def __init__(self):
       PyCoefficientBase.__init__(self, 1)
   def _EvalPyT(self, x, t):
       return self.EvalValue(x.GetDataArray(), t)
   def EvalValue(self, x, t):
       return 0.0

class VectorPyCoefficient(VectorPyCoefficientBase):
   def __init__(self, dim):
       self.sdim = dim
       VectorPyCoefficientBase.__init__(self, dim, 0)
   def _EvalPy(self, x, V):
       v = self.EvalValue(x.GetDataArray())
       for i in range(self.sdim):
           V[i] = v[i]
   def _EvalPyT(self, x, t, V):
       v = self.EvalValue(x.GetDataArray())  
       for i in range(self.sdim):
           V[i] = v[i]
   def EvalValue(self, x):
       return [0,0,0]

class VectorPyCoefficientT(VectorPyCoefficientBase):
   def __init__(self, dim):
       self.sdim = dim  
       VectorPyCoefficientBase.__init__(self, dim, 1)
   def _EvalPy(self, x, V):
       v = self.EvalValue(x.GetDataArray(), 0)
       for i in range(self.sdim):
           V[i] = v[i]
   def _EvalPyT(self, x, t, V):
       v = self.EvalValue(x.GetDataArray(), t)  
       for i in range(self.sdim):
           V[i] = v[i]
   def EvalValue(self, x, t):
       return [0,0,0]

class MatrixPyCoefficient(MatrixPyCoefficientBase):
   def __init__(self, dim):
       self.sdim = dim
       MatrixPyCoefficientBase.__init__(self, dim, 0)
   def _EvalPy(self, x, K):
       k = self.EvalValue(x.GetDataArray())
       for i in range(self.sdim):
           for j in range(self.sdim):
               K[i, j] = k[i, j]
   def EvalValue(self, x):
       return np.array([[0,0,0], [0,0,0] [0,0,0]])

class MatrixPyCoefficientT(MatrixPyCoefficientBase):
   def __init__(self, dim):
       self.sdim = dim  
       MatrixPyCoefficientBase.__init__(self, dim, 1)
   def _EvalPyT(self, x, t, K):
       k = self.EvalValue(x.GetDataArray(), t)  
       for i in range(self.sdim):
           for j in range(self.sdim):
               K[i, j] = k[i, j]
   def EvalValue(self, x, t):
       return np.array([[0,0,0], [0,0,0] [0,0,0]])


# This file is compatible with both classic and new-style classes.


