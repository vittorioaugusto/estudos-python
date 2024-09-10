# Ordenação alfabética crescente (lexicográfica)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  
print(linguagens)  # ['c', 'csharp', 'java', 'js', 'python']

# Ordenação alfabética decrescente (lexicográfica)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  
print(linguagens)  # ['python', 'js', 'java', 'csharp', 'c']

# Ordenação por tamanho da string (crescente)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  
print(linguagens)  # ['c', 'js', 'java', 'python', 'csharp']

# Ordenação por tamanho da string (decrescente)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  
print(linguagens)  # ['python', 'csharp', 'java', 'js', 'c']
