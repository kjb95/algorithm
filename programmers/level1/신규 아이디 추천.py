def solution(new_id):
    one = new_id.lower()
    
    two = ""
    for i in one:
      if i in ["-", "_", "."] or i.isdigit() or i.isalpha():
            two += i
    
    three = two
    while ".." in three:
      three = three.replace("..", ".")
            
    four = three.strip(".")
    
    five = "a" if four=="" else four
    
    six = five[:15]
    six = six.strip(".")
    
    seven = six
    while len(seven)<3:
        seven += seven[-1]
    
    return seven