# -*- coding: UTF-8 -*-
import random

def gen_map(self,max_x = 10,max_y = 10):
    self.max_x,self.max_y = max_x,max_y
    self.mmap = [[None for j in range(self.max_y)] for i in range(self.max_x)]
    self.solution = []
    block_stack = [Block(self,0,0)]
    while block_stack:
        block = block_stack.pop()
        next_block = block.get_next_block()
        if next_block:
            block_stack.append(block)
            block_stack.append(block_stack)
            if next_block.x == self.max_x - 1 and next_block.y == self.max_y - 1:
                for o in block_stack:
                    self.solution.append((o.x,o.y))

def get_next_block_pos(self,direction):
    x = self.x
    y = self.y
    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    if direction == 2:
        y += 1
    if direction == 3:
        x -= 1
    return x,y

def get_next_block(self):
    directions = list(range(4))
    random.shuffle(directions)
    for direction in directions:
        x,y = self.get_next_block_pos(direction)
        if x >=self.mmap.max_x or x < 0 or y >= self.mmap.max_y or y < 0:
            continue
        if self.mmap.mmap[x][y]:
            continue
        self.walls[direction] = False
        return Block(self.mmap,x,y,direction)
    return None
