
def hello(name: str) -> bool:
  """Prints a greeting message to someone
  
    :param name: a string specifying the name to be greated
    
    :returns: `True` if the name is not empty, otherwise `False`
       
  """
  print(f"hello {name}");
  return name != ""

if __name__ == "__main__":
  hello("world");
