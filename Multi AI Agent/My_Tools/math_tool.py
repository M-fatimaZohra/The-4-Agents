from agents import function_tool


@function_tool
def addition(a:int, b:int):
    """add two numbers and return value
     a:int
     b:int
     
     return a+b 
     
     """
    answer = f"Ansewr of following operation is {a+b}"
    return answer
