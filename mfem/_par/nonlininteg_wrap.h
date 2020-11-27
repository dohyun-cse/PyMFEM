/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_nonlininteg_WRAP_H_
#define SWIG_nonlininteg_WRAP_H_

#include <map>
#include <string>


class SwigDirector_NonlinearFormIntegrator : public mfem::NonlinearFormIntegrator, public Swig::Director {

public:
    SwigDirector_NonlinearFormIntegrator(PyObject *self, mfem::IntegrationRule const *ir = NULL);
    virtual void AssembleElementVector(mfem::FiniteElement const &el, mfem::ElementTransformation &Tr, mfem::Vector const &elfun, mfem::Vector &elvect);
    virtual void AssembleFaceVector(mfem::FiniteElement const &el1, mfem::FiniteElement const &el2, mfem::FaceElementTransformations &Tr, mfem::Vector const &elfun, mfem::Vector &elvect);
    virtual void AssembleElementGrad(mfem::FiniteElement const &el, mfem::ElementTransformation &Tr, mfem::Vector const &elfun, mfem::DenseMatrix &elmat);
    virtual void AssembleFaceGrad(mfem::FiniteElement const &el1, mfem::FiniteElement const &el2, mfem::FaceElementTransformations &Tr, mfem::Vector const &elfun, mfem::DenseMatrix &elmat);
    virtual double GetElementEnergy(mfem::FiniteElement const &el, mfem::ElementTransformation &Tr, mfem::Vector const &elfun);
    virtual void AssemblePA(mfem::FiniteElementSpace const &fes);
    virtual void AssemblePA(mfem::FiniteElementSpace const &trial_fes, mfem::FiniteElementSpace const &test_fes);
    virtual void AddMultPA(mfem::Vector const &x, mfem::Vector &y) const;
    virtual ~SwigDirector_NonlinearFormIntegrator();

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class NonlinearFormIntegrator doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[8];
#endif

};


#endif
