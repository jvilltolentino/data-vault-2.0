import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from dv_repo import api_clients


print("Running test.py... " + str(sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))))

print("Current working directory: " + os.getcwd())
print("Contents of current directory: " + str(os.listdir('.')))
print("Contents of syspath  directory: " + str(sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))))
print("Contents of ospath directory: " + os.path.join(os.path.dirname(__file__), '../..'))
print("Contents of sys.path: " + os.path.dirname(__file__))

# from api_clients import hello

print(api_clients.__version__)
print(api_clients.__file__)
print(api_clients.__dict__)

# .hello.hello()
# print("api_clients version: " + str(api_clients.__version__))


