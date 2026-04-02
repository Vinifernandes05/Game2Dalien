import sys
import os

# caminho até a pasta src
SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

# adiciona ao path
sys.path.append(SRC_PATH)