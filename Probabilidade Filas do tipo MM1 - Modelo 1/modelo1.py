import numpy as np
import matplotlib.pyplot as plt

class MM1Server:
    def __init__(self, arrival_rate, service_rate):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.queue = []
        self.queue_size = []
        self.event_times = []
        self.event_types = []

    def simulate(self, simulation_time):
        arrival_time = np.random.exponential(1 / self.arrival_rate)
        service_time = np.random.exponential(1 / self.service_rate)

        while arrival_time < simulation_time:
            if len(self.queue) == 0:
                departure_time = arrival_time + service_time
                self.queue.append(departure_time)
            else:
                queue_len = len(self.queue)
                last_departure = self.queue[queue_len - 1]
                queue_time = last_departure - arrival_time
                self.queue.append(last_departure + service_time - queue_time)

            self.queue_size.append(len(self.queue))
            self.event_times.append(arrival_time)
            self.event_types.append('chegada')

            arrival_time += np.random.exponential(1 / self.arrival_rate)
            service_time = np.random.exponential(1 / self.service_rate)

    def plot_queue_size(self):
        plt.step(self.event_times, self.queue_size, where='post')
        plt.xlabel('Tempo')
        plt.ylabel('Número de pessoas na fila')
        plt.title('Simulação do Sistema de Fila MM1')
        plt.grid(True)
        plt.show()

# Parâmetros do Modelo 1
arrival_rate_model1 = 1
service_rate_model1 = 2
simulation_time_model1 = 10

# Criar e simular o servidor do Modelo 1
server_model1 = MM1Server(arrival_rate_model1, service_rate_model1)
server_model1.simulate(simulation_time_model1)
server_model1.plot_queue_size()