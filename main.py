class Ast:
  def __init__(self):
    pass

class Main(Ast):
  def __init__(self, children):
    self.children = children
    self.history = []

class Loop(Ast):
  def __init__(self, loop_variable, limit, children):
    self.loop_variable = loop_variable
    self.limit = limit
    self.children = children
    self.history = []

class Assign(Ast):
  def __init__(self, variable, value):
    self.variable = variable
    self.value = value
    self.children = []
    self.history = []

class MethodCall(Ast):
  def __init__(self, name, children, *arguments):
    self.name = name
    self.children = children
    self.arguments = arguments
    self.history = []
    
  def __str__(self):
    return self.name

main = Main([Loop("i", 100, [

  Assign("i", 0),
  MethodCall("process",
             [
               MethodCall("thing1", [], "i"),
               MethodCall("thing2", [], "i"),
             ], "i"),
  MethodCall("send", [], "i")
  
])])

class Context:
  def __init__(self, value):
    self.value = value
  def newid(self, item):
    self.value = self.value + 1
    print("Assigning {} to {}".format(self.value, item))
    return self.value

def renumber(ast, context, new_ids):
  
  ast.id = context.newid(ast)
  new_ids = list(new_ids) + [ast.id]
  ast.history = new_ids
  for child in ast.children:
    new_ids = renumber(child, context, new_ids)
  return new_ids
      

renumber(main, Context(-1), [])

def printids(ast):
  print("{} {}". format(ast, ast.history))
  for child in ast.children:
    printids(child)

printids(main)
