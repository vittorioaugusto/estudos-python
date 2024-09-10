linguagens = ["python", "js", "c", "java", "csharp"]

# Ordenação por tamanho da string (crescente) usando sorted()
print(sorted(linguagens, key=lambda x: len(x)))  
# ['c', 'js', 'java', 'python', 'csharp']

# Ordenação por tamanho da string (decrescente) usando sorted()
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  
# ['python', 'csharp', 'java', 'js', 'c']
