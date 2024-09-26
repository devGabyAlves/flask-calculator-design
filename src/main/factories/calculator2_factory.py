from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    numpy_hanler = NumpyHandler()
    calc = Calculator2(numpy_hanler)
    return calc