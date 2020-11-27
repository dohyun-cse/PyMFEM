# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _linearform
else:
    import _linearform

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _linearform.SWIG_PyInstanceMethod_New
_swig_new_static_method = _linearform.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

class intp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _linearform.intp_swiginit(self, _linearform.new_intp())
    __swig_destroy__ = _linearform.delete_intp

    def assign(self, value):
        return _linearform.intp_assign(self, value)
    assign = _swig_new_instance_method(_linearform.intp_assign)

    def value(self):
        return _linearform.intp_value(self)
    value = _swig_new_instance_method(_linearform.intp_value)

    def cast(self):
        return _linearform.intp_cast(self)
    cast = _swig_new_instance_method(_linearform.intp_cast)

    @staticmethod
    def frompointer(t):
        return _linearform.intp_frompointer(t)
    frompointer = _swig_new_static_method(_linearform.intp_frompointer)

# Register intp in _linearform:
_linearform.intp_swigregister(intp)

def intp_frompointer(t):
    return _linearform.intp_frompointer(t)
intp_frompointer = _linearform.intp_frompointer

class doublep(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _linearform.doublep_swiginit(self, _linearform.new_doublep())
    __swig_destroy__ = _linearform.delete_doublep

    def assign(self, value):
        return _linearform.doublep_assign(self, value)
    assign = _swig_new_instance_method(_linearform.doublep_assign)

    def value(self):
        return _linearform.doublep_value(self)
    value = _swig_new_instance_method(_linearform.doublep_value)

    def cast(self):
        return _linearform.doublep_cast(self)
    cast = _swig_new_instance_method(_linearform.doublep_cast)

    @staticmethod
    def frompointer(t):
        return _linearform.doublep_frompointer(t)
    frompointer = _swig_new_static_method(_linearform.doublep_frompointer)

# Register doublep in _linearform:
_linearform.doublep_swigregister(doublep)

def doublep_frompointer(t):
    return _linearform.doublep_frompointer(t)
doublep_frompointer = _linearform.doublep_frompointer

import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.matrix
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.mesh
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.bilininteg
import mfem._ser.vertex
import mfem._ser.vtk
class LinearForm(mfem._ser.vector.Vector):
    r"""Proxy of C++ mfem::LinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(LinearForm self, FiniteElementSpace f) -> LinearForm
        __init__(LinearForm self, FiniteElementSpace f, LinearForm lf) -> LinearForm
        __init__(LinearForm self) -> LinearForm
        __init__(LinearForm self, FiniteElementSpace f, double * data) -> LinearForm
        """
        _linearform.LinearForm_swiginit(self, _linearform.new_LinearForm(*args))

    def GetFES(self):
        r"""GetFES(LinearForm self) -> FiniteElementSpace"""
        return _linearform.LinearForm_GetFES(self)
    GetFES = _swig_new_instance_method(_linearform.LinearForm_GetFES)

    def FESpace(self, *args):
        r"""
        FESpace(LinearForm self) -> FiniteElementSpace
        FESpace(LinearForm self) -> FiniteElementSpace
        """
        return _linearform.LinearForm_FESpace(self, *args)
    FESpace = _swig_new_instance_method(_linearform.LinearForm_FESpace)

    def AddDomainIntegrator(self, lfi):
        r"""AddDomainIntegrator(LinearForm self, LinearFormIntegrator lfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(lfi)
        lfi.thisown=0 


        return _linearform.LinearForm_AddDomainIntegrator(self, lfi)


    def AddBoundaryIntegrator(self, *args):
        r"""
        AddBoundaryIntegrator(LinearForm self, LinearFormIntegrator lfi)
        AddBoundaryIntegrator(LinearForm self, LinearFormIntegrator lfi, intArray bdr_attr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        lfi = args[0]	     
        self._integrators.append(lfi)
        lfi.thisown=0


        return _linearform.LinearForm_AddBoundaryIntegrator(self, *args)


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(LinearForm self, LinearFormIntegrator lfi)
        AddBdrFaceIntegrator(LinearForm self, LinearFormIntegrator lfi, intArray bdr_attr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        lfi = args[0]
        self._integrators.append(lfi)
        lfi.thisown=0 


        return _linearform.LinearForm_AddBdrFaceIntegrator(self, *args)


    def GetDLFI(self):
        r"""GetDLFI(LinearForm self) -> mfem::Array< mfem::LinearFormIntegrator * > *"""
        return _linearform.LinearForm_GetDLFI(self)
    GetDLFI = _swig_new_instance_method(_linearform.LinearForm_GetDLFI)

    def GetDLFI_Delta(self):
        r"""GetDLFI_Delta(LinearForm self) -> mfem::Array< mfem::DeltaLFIntegrator * > *"""
        return _linearform.LinearForm_GetDLFI_Delta(self)
    GetDLFI_Delta = _swig_new_instance_method(_linearform.LinearForm_GetDLFI_Delta)

    def GetBLFI(self):
        r"""GetBLFI(LinearForm self) -> mfem::Array< mfem::LinearFormIntegrator * > *"""
        return _linearform.LinearForm_GetBLFI(self)
    GetBLFI = _swig_new_instance_method(_linearform.LinearForm_GetBLFI)

    def GetFLFI(self):
        r"""GetFLFI(LinearForm self) -> mfem::Array< mfem::LinearFormIntegrator * > *"""
        return _linearform.LinearForm_GetFLFI(self)
    GetFLFI = _swig_new_instance_method(_linearform.LinearForm_GetFLFI)

    def GetFLFI_Marker(self):
        r"""GetFLFI_Marker(LinearForm self) -> mfem::Array< mfem::Array< int > * > *"""
        return _linearform.LinearForm_GetFLFI_Marker(self)
    GetFLFI_Marker = _swig_new_instance_method(_linearform.LinearForm_GetFLFI_Marker)

    def Assemble(self):
        r"""Assemble(LinearForm self)"""
        return _linearform.LinearForm_Assemble(self)
    Assemble = _swig_new_instance_method(_linearform.LinearForm_Assemble)

    def AssembleDelta(self):
        r"""AssembleDelta(LinearForm self)"""
        return _linearform.LinearForm_AssembleDelta(self)
    AssembleDelta = _swig_new_instance_method(_linearform.LinearForm_AssembleDelta)

    def Update(self, *args):
        r"""
        Update(LinearForm self)
        Update(LinearForm self, FiniteElementSpace f)
        Update(LinearForm self, FiniteElementSpace f, Vector v, int v_offset)
        """
        return _linearform.LinearForm_Update(self, *args)
    Update = _swig_new_instance_method(_linearform.LinearForm_Update)

    def MakeRef(self, f, v, v_offset):
        r"""MakeRef(LinearForm self, FiniteElementSpace f, Vector v, int v_offset)"""
        return _linearform.LinearForm_MakeRef(self, f, v, v_offset)
    MakeRef = _swig_new_instance_method(_linearform.LinearForm_MakeRef)

    def __call__(self, gf):
        r"""__call__(LinearForm self, GridFunction gf) -> double"""
        return _linearform.LinearForm___call__(self, gf)
    __call__ = _swig_new_instance_method(_linearform.LinearForm___call__)
    __swig_destroy__ = _linearform.delete_LinearForm

# Register LinearForm in _linearform:
_linearform.LinearForm_swigregister(LinearForm)



