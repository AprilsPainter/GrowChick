# source/model/chick.py

import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
if os.path.join(BASE_DIR, "source") not in sys.path:
    sys.path.append(os.path.join(BASE_DIR, "source"))

import config

class Chick:
    """병아리 객체 클래스"""
    
    def __init__(self):
        self.stats = config.DEFAULT_STATS
    
    def get_stats(self):
        """외부에서 스탯 값 접근"""
        
        return self.stats
