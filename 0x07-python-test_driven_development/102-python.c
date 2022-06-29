#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

void print_python_string(PyObject *p)
{
    const char *type = NULL;
    Py_ssize_t len = 0;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        type = "compact ascii";
    }
    else
    {
        type = "compact unicode object";
    }

    printf("  type: %s\n", type);
    printf("  length: %ld\n", len);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}
