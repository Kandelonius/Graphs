# An incomplete list of directions. Your task is to fill this with valid traversal directions.
from util import Queue

from world import World
from graph import Graph


class Player:
    graph = Graph()

    def __init__(self, starting_room):
        self.current_room = starting_room

    def travel(self, direction, show_rooms=False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")

    def clear_fog(self, starting_room):
        # first move to one end of the map
        # create a list to return when done
        direction = self.current_room.get_exits()[0]
        visited = {}
        print(f"start is {starting_room}")
        path = self.check_all_rooms(direction, visited)
        return path

    # def dft(self, starting_room, visited=None):
    #     if visited == None:
    #         visited = set()
    #     visited.add(starting_room)
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
        visited = set()
        queue = Queue()
        while self.current_room.get_exits()[0] == 'n':
            # print(rooms)
            rooms.append('n')
            visited.add(self.current_room.id)
            print(visited)
            self.travel('n')
        # now that we have gone as far north as we can we should do bft and enqueue all of the neighbors
        # of the rooms we are in.
        return rooms

    # recursive method that will create a dict for a room and
    def check_all_rooms(self, direction, visited, previous_room = None, rooms=None):
        # bread_crumb is used to look back when updating the room dict
        bread_crumb = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        if rooms == None:
            rooms = []
        if previous_room != None:
            rooms.append(direction)
            self.travel(direction)
        print(f"current room id is {self.current_room.id}")
        #     queue = Queue()
        # queue.enqueue(previous_room)
        # while queue.size() > 0:
        room_number = self.current_room.id
        if room_number not in visited:
            # create a dict for the room to store adjacency values
            visited[room_number] = {}
            exits = self.current_room.get_exits()
            for exit in exits:
                visited[room_number][exit] = '?'
                print(f"exit for room {room_number} is {exit}")
                print(visited)
            if previous_room != None:
                print(f"pre is {previous_room}")
                visited[previous_room][direction] = room_number
                visited[room_number][bread_crumb[direction]] = previous_room
        for dir in visited[room_number]:
            print(f"hi {visited[room_number][dir]}")
            if visited[room_number][dir] == '?':
                self.check_all_rooms(dir, visited, room_number, rooms)
        return rooms
