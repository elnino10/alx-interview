#!/usr/bin/python3
'''
A method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
    '''
    Checks if all the boxes in a list of boxes containing the keys
    to other boxes can be openeed, the first box is open.
    '''
    n = len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))
    while len(unchecked_boxes) > 0:
        box_index = unchecked_boxes.pop()
        if not box_index or box_index >= n or box_index < 0:
            continue
        if box_index not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[box_index])
            checked_boxes.add(box_index)
    return n == len(checked_boxes)
