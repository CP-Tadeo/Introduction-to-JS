import random


class CorruptQueue:
    def __init__(self):
        self.RegularQueue = []
        self.VIPStack = []
        self.supervisor_present = False

    def lineup(self, name, client_type):
        if client_type == "VIP":
            self.VIPStack.append(name)
            print(f"VIP client {name} lines up at VIPStack")
        else:
            self.RegularQueue.append(name)
            print(f"Regular client {name} lines up at RegularQueue")

    def serve(self):
        if self.supervisor_present:
            if self.VIPStack:
                client = self.VIPStack.pop(0)
                print(f"Now serving VIP client {client} from VIPStack")
            elif self.RegularQueue:
                client = self.RegularQueue.pop(0)
                print(f"Now serving regular client {client} from RegularQueue")
            else:
                print("No clients in the queues.")
        else:
            if self.VIPStack:
                client = self.VIPStack.pop()
                print(f"Now serving VIP client {client} from VIPStack")
            elif self.RegularQueue:
                client = self.RegularQueue.pop(0)
                print(f"Now serving regular client {client} from RegularQueue")
            else:
                print("No clients in the queues.")

    def arrive_supervisor(self):
        self.supervisor_present = True
        print("Supervisor present")
        while self.VIPStack:
            client = self.VIPStack.pop()
            self.RegularQueue.append(client)

    def leave_supervisor(self):
        self.supervisor_present = False
        print("Supervisor not here")

    def process_command(self, command):
        if command.startswith("lineup"):
            _, name, client_type = command.split(",")
            self.lineup(name.strip(), client_type.strip())
        elif command == "serve":
            self.serve()
        elif command == "arrive,supervisor":
            self.arrive_supervisor()
        elif command == "leave,supervisor":
            self.leave_supervisor()

    def get_queue_status(self):
        if self.supervisor_present:
            print(f"Queue Status: {self.RegularQueue}")
        else:
            print(f"Queue Status: {self.RegularQueue}; {self.VIPStack}")


class CQSimulation:
    def __init__(self):
        self.queue = CorruptQueue()
        self.num_iterations = 0
        self.mu = 0
        self.sigma = 0
        self.lambda_value = 0
        self.total_wait_time = 0
        self.total_system_time = 0
        self.num_clients = 0

    def read_commands(self, filename):
        with open(filename, "r") as file:
            commands = file.readlines()
        return [command.strip() for command in commands]

    def simulate(self, num_iterations, mu, sigma, lambda_value, filename):
        self.num_iterations = num_iterations
        self.mu = mu
        self.sigma = sigma
        self.lambda_value = lambda_value

        for _ in range(self.num_iterations):
            commands = self.read_commands(filename)
            self.queue.RegularQueue = []
            self.queue.VIPStack = []
            self.queue.supervisor_present = False

            for command in commands:
                if command.startswith("lambda"):
                    self.lambda_value = float(command.split(",")[1])
                elif command.startswith("mu"):
                    self.mu = float(command.split(",")[1])
                else:
                    self.queue.process_command(command)

                arrival_time = random.expovariate(self.lambda_value)
                service_time = max(0, random.normalvariate(self.mu, self.sigma))

                self.total_wait_time += max(0, arrival_time - service_time)
                self.total_system_time += service_time
                self.num_clients += 1

                self.queue.get_queue_status()

        average_wait_time = self.total_wait_time / self.num_clients
        average_time_in_system = self.total_system_time / self.num_clients

        print(f"\nAverage Wait Time: {average_wait_time}")
        print(f"Average Time in System: {average_time_in_system}")


simulation = CQSimulation()
simulation.simulate(num_iterations=1, mu=7, sigma=1, lambda_value=0.1, filename="officeinput.txt")
