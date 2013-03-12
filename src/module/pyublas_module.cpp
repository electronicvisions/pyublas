#include <boost/python.hpp>

void pyublas_expose_converters();

BOOST_PYTHON_MODULE(pyublas)
{
	pyublas_expose_converters();
}
