# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from enum import Enum


class Direction(Enum):
    up = "up"
    down = "down"
    right = "right"
    left = "left"


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        current_position = [0, 0]
        current_direction = Direction.right
        top_boundary, left_boundary, bottom_boundary, right_boundary = (
            0,
            0,
            m - 1,
            n - 1,
        )

        while head:
            matrix[current_position[0]][current_position[1]] = head.val

            match current_direction:
                case Direction.right:
                    if current_position[1] + 1 > right_boundary:
                        current_direction = Direction.down
                        top_boundary += 1
                        current_position[0] += 1
                    else:
                        current_position[1] += 1

                case Direction.down:
                    if current_position[0] + 1 > bottom_boundary:
                        current_direction = Direction.left
                        right_boundary -= 1
                        current_position[1] -= 1
                    else:
                        current_position[0] += 1

                case Direction.left:
                    if current_position[1] - 1 < left_boundary:
                        current_direction = Direction.up
                        bottom_boundary -= 1
                        current_position[0] -= 1
                    else:
                        current_position[1] -= 1

                case Direction.up:
                    if current_position[0] - 1 < top_boundary:
                        current_direction = Direction.right
                        left_boundary += 1
                        current_position[1] += 1
                    else:
                        current_position[0] -= 1

            head = head.next

        return matrix

