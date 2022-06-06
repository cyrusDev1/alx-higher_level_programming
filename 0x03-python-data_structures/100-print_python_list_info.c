#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p){

    int i;
    long int len = PyList_Size(p);
    PyListObject *object = (PyListObject *)p;
    PyObject *element;

    printf("[*] Size of the Python List = %li\n", len);
    printf("[*] Allocated = %li\n", object->allocated);
    for (i = 0; i < len; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
    }
}
