import random, sys
from Person import Person
from Virus import Virus
from FileWriter import FileWriter

class Simulation:

    def __init__(self, initial_vaccinated, initial_infected, initial_healthy, virus, resultsfilename):
        '''Set up the initial simulation values'''

        self.virus = virus
        self.initial_infected = initial_infected
        self.initial_healthy = initial_healthy
        self.initial_vaccinated = initial_vaccinated

        self.population = []

        self.population_size = initial_infected + initial_healthy + initial_vaccinated


        self.total_dead = 0
        self.total_vaccinated = initial_vaccinated

        self.file_writer = FileWriter(resultsfilename)


    def create_population(self):
        '''Creates the population (a list of Person objects) consisting of initial infected people, initial healthy non-vaccinated people, and
        initial healthy vaccinated people. Adds them to the population list'''

        for i in range(self.initial_infected):
        	each_person = Person(False, virus)
        	self.population.append(each_person)

        for i in range(self.initial_healthy):
            each_person = Person(False, None)
            self.population.append(each_person)

        for i in range(self.initial_vaccinated):
            each_person = Person(True, None)
            self.population.append(each_person)

    def print_population(self):
        '''Prints out every person in the population and their current attributes'''
        num = 0
        for each_person in self.population:
            if each_person.infection != None:
                infection = True
            else:
                infection = False
            print(f"id: {str(num)} alive: {str(each_person.is_alive)} infected: {str(infection)} vacinated: {str(each_person.is_vaccinated)}.")
            num += 1

    def get_infected(self):
        '''Gets all the infected people from the population and returns them as a list'''
        infected = []
        for each_person in self.population:
            if each_person.infection != None:
                infected.append(each_person)
                return infected


    def simulation_should_continue(self):
        '''Determines whether the simulation should continue.
        If everyone in the population is dead then return False, the simulation should not continue
        If everyone in the population is vaccinated return False
        If there are no more infected people left and everyone is either vaccinated or dead return False
        In all other cases return True'''
        #TODO: finish this method
        for each_person in self.population:
            if each_person.is_alive == False or each_person.is_vaccinated == True:
                return False
            else:
                return True


    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''

        self.create_population()
        random.shuffle(self.population)

        self.print_population()

        time_step_counter = 0

        self.file_writer.init_file(self.virus, self.population_size, self.initial_vaccinated, self.initial_healthy, self.initial_infected)

        #keep looping until the simulation ends
        while self.simulation_should_continue():

            #save the current infected
            old_infected = self.get_infected()
            self.time_step(old_infected)
            #time step will create newly infected people, just determine the survivial of the previous infected people
            self.determine_survival(old_infected)

            time_step_counter += 1

        print(f'The simulation has ended after {time_step_counter} turns.')
        self.file_writer.write_results(time_step_counter, self.total_dead, self.total_vaccinated)

    def determine_survival(self, infected):
        for each_person in infected:
            if each_person.did_survive_infection() == False:
                self.total_dead += 1
            else:
                each_person.is_vaccinated = True
                self.total_vaccinated += 1



    def time_step(self, infected):
        ''' For every infected person interact with a random person from the population 10 times'''

        for infected_person in infected:

            for _ in range(10):
                #TODO: get a random index for the population list
                index = random.randint(0, len(self.population)) - 1
                #TODO: using the random index get a random person from the population
                random_person = self.population[index]
                #TODO: call interaction() with the current infected person and the random person
                self.interaction(infected_person, random_person)


    def interaction(self, infected_person, random_person):
        '''If the infected person is the same object as the random_person return and do nothing
        if the random person is not alive return and do nothing
        if the random person is vaccinated return and do nothing
        if the random person is not vaccinated:
            generate a random float between 0 and 1
            if the random float is less then the infected person's virus reproduction number then the random person is infected
            otherwise the random person is vaccinated and one is added to the total vaccinated'''
        #TODO: finish this method
        if infected_person == random_person or random_person.is_alive == False or random_person.is_vaccinated == True:
            pass
        elif random_person.is_vaccinated == False:
            num = random.random()
            if num < self.virus.reproduction_num:
                random_person.infection = self.virus
                return random_person
            else:
                random_person.is_vaccinated = True
                return random_person



if __name__ == "__main__":

    #Set up the initial simulations values
    virus_name = "Malaise"
    reproduction_num = 0.20
    mortality_num = .99

    initial_healthy = 3
    initial_vaccinated = 5

    initial_infected = 2

    virus = Virus(virus_name, reproduction_num, mortality_num)
    num = initial_healthy + initial_vaccinated + initial_infected
    simulation = Simulation(initial_vaccinated, initial_infected, initial_healthy, virus, f"results{num}.txt")

    #run the simulation
    simulation.run()
