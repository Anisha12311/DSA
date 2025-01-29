
import hashlib

file = 'Hash/file.txt'

def find_duplicate(filepath):
    
    line_hash_map = {}
    
    duplicate = []
    
    with open(filepath, 'r', encoding='utf-8') as file : 
        for line in file:
            
            line_strip = line.strip()
            
            line_hash = hashlib.sha256(line_strip.encode()).hexdigest()
            
            
            if line_hash in line_hash_map:
                duplicate.append((line_hash_map[line_hash], line_hash))
                
                if len(duplicate) == 2:
                    return duplicate

            else : 
                line_hash_map[line_hash] = line
     
    return duplicate   

print(find_duplicate(file))