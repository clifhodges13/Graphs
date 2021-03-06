import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')
        
        # Create friendships
        # Generate ALL possible friendships
        # Avoid duplicate friendships 
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # user_id == friend_id cannot happen
                # if friendship between user_id and user_id_2 already exists
                #   dont add friendship between user_id_2 and user_id
                possible_friendships.append( (user_id, friend_id) )
            
        # Randomly select X friendships
        # the formula for X is  num_users * avg_friendships  // 2 
        # shuffle the array and pick X elements from the front of it
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Create an empty queue and enqueue the PATH TO user_id
        q = Queue()
        q.enqueue([user_id])

        # while the queue is not empty:
        while q.size() > 0:
            # get the current friendship PATH (dequeue from queue)
            current_path = q.dequeue()
            # set the current user to the LAST element of the PATH
            current_user = current_path[-1]

            # check if current user has not been visited:
            if current_user not in visited:

                # mark the current user as visited
                visited[current_user] = current_path

                # queue up all NEW paths with each friendship:
                for friend in self.friendships[current_user]:
                    # take current path
                    new_path = current_path.copy()
                    # append the neighbor to it
                    new_path.append(friend)
                    # queue up the NEW path
                    q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
