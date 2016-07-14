try:
    foo()
except Exception as exception:
    print("Caught", exception.__class__.__name__)


