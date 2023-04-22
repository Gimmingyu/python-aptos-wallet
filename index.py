import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), 'aptos'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'server'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'proto'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'gen'))
print(sys.path)