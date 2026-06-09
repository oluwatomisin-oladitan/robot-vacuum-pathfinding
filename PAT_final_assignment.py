#!/usr/bin/env python
# coding: utf-8

# In[3]:


def readMap(filename):
    map_grid = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip().split(',')
                map_grid.append(row)
                
    except Exception:
        return []
    
    return map_grid


# In[2]:


def locate(map_grid):
    start = None
    stains = []
    
    
    for i in range(len(map_grid)):
        row = map_grid[i]
        
        for j in range(len(row)):
            cell = row[j]
            
            if cell == '#':
                row_letter = chr(65 + i)    # in ASCII: 'A'=65
                start = f"{row_letter}{j}"
                
            elif cell == '@':
                row_letter = chr(65 + i) 
                stain_cd = f"{row_letter}{j}"
                stains.append(stain_cd)
    
    return start, stains


# In[4]:


def calculateDistances(start_cd, stains_list):
    import math
    
    distances = {}
    
    start_row_letter = start_cd[0] 
    start_col = int(start_cd[1:]) 
    
    start_row = ord(start_row_letter) - 65 
    
    for stain_cd in stains_list:
        stain_row_letter = stain_cd[0]
        stain_col = int(stain_cd[1:])
        stain_row = ord(stain_row_letter) - 65
        
        col_diff = stain_col - start_col
        row_diff = stain_row - start_row
        distance = math.sqrt(col_diff**2 + row_diff**2)
        
        distances[stain_cd] = round(distance, 2)
    
    return distances


# In[ ]:


def solveMap(map_grid, start_cd, stains_list, distances_dict):
    
    def cd_to_index(cd):
        row = ord(cd[0]) - 65
        col = int(cd[1:])
        return (row, col)
    
    def index_to_cd(row, col):
        return f"{chr(65 + row)}{col}"
    
    def get_path(start_row, start_col, target_row, target_col):
        rows = len(map_grid)
        cols = len(map_grid[0])
    
        if (start_row, start_col) == (target_row, target_col):
            return ""
    
        directions = [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]
    
        queue = [(start_row, start_col, "")]  # (row, col, path_so_far)
        visited = set()
        visited.add((start_row, start_col))
    
        while queue:
            r, c, path = queue.pop(0)  
        
            for dr, dc, move in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and map_grid[nr][nc] != 'x' and (nr, nc) not in visited:
                    new_path = path + move
                    if (nr, nc) == (target_row, target_col):
                        return new_path
                    visited.add((nr, nc))
                    queue.append((nr, nc, new_path))
    
    
        return ""

    
    if not stains_list:
        return ""
    
    stain_distance_pairs = []
    for stain in stains_list:
        stain_distance_pairs.append((distances_dict[stain], stain))
    
    
    stain_distance_pairs.sort()  # to sort by distance 
    
    sorted_stains = []
    
    for distance, stain in stain_distance_pairs: 
        sorted_stains.append(stain)
    
    current_row, current_col = cd_to_index(start_cd)
    total_path = ""
    
    
    for stain in sorted_stains:
        
        tr, tc = cd_to_index(stain) # this is to get path to this stain
        path_part = get_path(current_row, current_col, tr, tc) 
        total_path += path_part
        
       
        current_row, current_col = tr, tc 
    
    return total_path

