#include <Python.h>
#include <oject.h>
#include <listobject.h>
#include <stdio.h>
/**
 * print_python_list - prints basic python info
 * @p: pointer to python object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf(:[*] Size of the Python List = %d\n", size);
	printf(:[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_type(obj)->tp_name);
	}
}
