import sys
# pythonpath에 경로를 동적으로 추가해주는 방법
# sys.path.append('/bigdata/PycharmProject/python_modules')

# settings -> project inteepreter -> 설정부분에서 path 추가 
import mymath

# print(sys.path)
print(mymath.add(10, 20))
print(mymath.pi)
