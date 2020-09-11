# An incomplete list of directions. Your task is to fill this with valid traversal directions.
from graph import Graph
from util import Stack, Queue
class Player:
    graph = Graph()
    def __init__(self, starting_room):
        self.current_room = starting_room
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")

    def clear_fog(self, starting_room):
        # create a list to return when done
        path = self.move_to_top(starting_room)
        return path

    # def dft(self, starting_room, visited=None):
    #     if visited == None:
    #         visited = set()
    #     visited.add(starting_room)
    #     # first do a depth first traversal to get to one end of the map
    #     stack = Stack()
    #     stack.push(starting_room)
    #     while stack.size() > 0:
    #         v = stack.pop
    #         if v not in visited:
    #             self.travel('n')
    #             # path.add('n')
    #             visited.add(v)
    #             print(self.current_room.get_exits())
    #             if self.current_room.get_exits()[0] == 'n':
    #                 print(self.current_room.get_exits()[0])
    #                 stack.push(self.current_room.get_room_in_direction('n'))
    #     return visited
    def move_to_top(self, starting_room):
        rooms = []
        print("hi")
        while self.current_room.get_exits()[0] == 'n':
            # print(rooms)
            rooms.append('n')
            self.travel('n')
        return rooms