# 동적 import를 위한 __import__ 사용
import sys

sys.path.append('/bigdata/PycharmProject/python_modules')
mm = __import__('mymath')

print(mm.add(10, 20))
