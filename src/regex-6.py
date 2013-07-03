'''
Created on Jul 3, 2013

@author: zeroshiiro
'''
lngList = ["C", "CPP", "JAVA", "PYTHON", "PERL", "PHP", "RUBY", "CSHARP", 
           "HASKELL", "CLOJURE", "BASH", "SCALA", "ERLANG", "CLISP", "LUA",
           "BRAINFUCK", "JAVASCRIPT", "GO", "D", "OCAML", "R", "PASCAL", 
           "SBCL", "DART", "GROOVY", "OBJECTIVEC"]

def findLang(NumReq):
    req = []
    for i in range(0, NumReq) :
        print("VALID") if input().split(" ")[1] in lngList else print("INVALID")

findLang(int(input()))