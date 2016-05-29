y # Food Co-op Simulation Program

import random

# Probabilties for Simulation (for values between 1-100)
#
# CLate_xx = chance of being late for work,
# CLEarly_xx = chance of leaving early from work,
# CNoshow = chance that a scheduled worker WILL NOT show up for work
# CShowup = chance that an unscheduled worker WILL show up to work


def eventOccurred(chances):

    ''' For given integer value chances as a percentage value (1-100),
        returns True if randomly generated number in range (1,100) is
        less than or equal to chances, otherwise returns False.
    '''
    if random.randint(1,100) <= chances:
        return True
    else:
        return False

def numWorkersShowedUp(indiv_chance, num_individuals):

    ''' For given integer values indiv_chance and num_individuals,
        returns how many times that num_individual calls to
        event_occurred with argument indiv_chance returns True.
    '''
    numworkers_arriving = 0

    for i in range(num_individuals):
        if eventOccurred(indiv_chance):
            numworkers_arriving = numworkers_arriving + 1

    return numworkers_arriving

def displayScheduledWorkerHours(workernum, probabilities):

    ''' For workernum equal to 1 or 2, and the proability values
        given in dictionary probabilities of the form,

         {'CLate_15':<num>, 'CLate_30':<num>, 'CLate_45':<num>,
          'CLEarly_15':<num>, 'CLEarly_30':<num>,'CNoshow':<num>}


       where each <num> is a value between 1-100, displays one of

         worker <worker_num> -- no show --   or
         worker <worker_num> <mins_late> mins late  and/or
         worker <worker_num> left <mins_early> mins early

       where <mins_late> is 15, 30, or 45,  <mins_early> is 15 or 30.
    '''

    # init
    mins_late = 0
    mins_left_early = 0

    if eventOccurred(probabilities['CNoshow']):
        mins_late = -1
    else:
        if eventOccurred(probabilities['CLate_15']):
            mins_late = 15
        elif eventOccurred(probabilities['CLate_30']):
            mins_late = 30
        elif eventOccurred(probabilities['CLate_45']):
            mins_late = 45

        if eventOccurred(probabilities['CLEarly_15']):
            mins_left_early = 15
        elif eventOccurred(probabilities['CLEarly_30']):
            mins_left_early = 30

    if workernum == 1:
        print('{0:>3}'.format('worker'), str(workernum) + ': ', end='')
    else:
        print('{0:>15}'.format('worker'), str(workernum) + ': ', end='')

    if mins_late == -1:
        print ('-- no show --', end='')
    else:
        if mins_late != 0:
            print(mins_late, 'mins late  ', end='')

        if mins_left_early != 0:
            print('left', mins_left_early, 'mins early', end='')

        if (mins_late == 0) and (mins_left_early == 0):
            print('whole time', end='')

def displayUnscheduledWorkerHours(workernum, probabilities):

    ''' For workernum equal to 1 or 2, and the proability values
        given in dictionary probabilities of the form,

         {'CLate_15':<num>, 'CLate_30':<num>, 'CLate_45':<num>,
          'CLEarly_15':<num>, 'CLEarly_30':<num>,'CShowup':<num>}


       where each <num> is a value between 1-100, displays one of

         worker <worker_num> -- no show --   or
         worker <worker_num> <mins_late> mins late  and/or
         worker <worker_num> left <mins_early> mins early

       where <mins_late> is 15, 30 or 45.
             <mins_early> is 15 or 30.
    '''
    mins_late = 0   # init
    mins_left_early = 0

    if eventOccurred(probabilities['CLate_15']):
        mins_late = 15
    elif eventOccurred(probabilities['CLate_30']):
        mins_late = 30
    elif eventOccurred(probabilities['CLate_45']):
        mins_late = 45

    if eventOccurred(probabilities['CLEarly_15']):
        mins_left_early = 15
    elif eventOccurred(probabilities['CLEarly_30']):
        mins_left_early = 30

    print('{0:>15}'.format('worker'), str(workernum) + ': ', end='')
    if mins_late != 0:
        print(mins_late, 'mins late  ', end='')

    if mins_left_early != 0:
        print('left', mins_left_early, 'mins early', end='')

    if (mins_late == 0) and (mins_left_early == 0):
        print('whole time', end='')

def executeScheduledSimulation(probabilities, days, time_slots):

    ''' Displays a simulated week of workers in attendance for all
        time slots, based on a scheduled worker schedule.
    '''

    # for each day of the week
    for day in days:
        print(day)
        print('-------')

        if (day == 'Sunday'):  # sunday?
            current_timeslot = '12:00pm'
            num_timeslots = 3
        elif day in days[1:5]: # mon-thurs?
            current_timeslot = '8:00am'
            num_timeslots = 5
        else:  # friday, saturday
            current_timeslot = '8:00am'
            num_timeslots = 6

        # find loc of current_timeslot in tuple time_slots
        index_val = time_slots.index(current_timeslot)

        # iterate through num_timeslots starting with current time slot
        for time_slot in time_slots[index_val:index_val + num_timeslots]:
            print('{0:>7}'.format(time_slot), ' ', end='')
            for k in range(0,2):
                displayScheduledWorkerHours(k+1, probabilities)
                print()
            print()

def executeUnscheduledSimulation(probabilities, days, time_slots):

    ''' Displays a simulated week of workers in attendance for all
        time slots, based on an unscheduled worker schedule.
    '''

    # for each day in the week
    for day in days:
        print(day)
        print('-------')

        if (day == 'Sunday'):   # sunday
            current_timeslot = '12:00pm'
            num_timeslots = 3
        elif day in days[1:5]: # mon-thurs?
            current_timeslot = '8:00am'
            num_timeslots = 5
        else:  # fri, sat
            current_timeslot = '8:00am'
            num_timeslots = 6

        # find loc of current_timeslot in tuple time_slots
        index_val = time_slots.index(current_timeslot)

        # iterate through num_timeslots starting with current time slot
        for time_slot in time_slots[index_val:index_val + num_timeslots]:
            numworkers = \
             numWorkersShowedUp(probabilities['CShowup'], num_members)
            print('{0:>7}'.format(time_slot), ' ', end='')

            if numworkers == 1:
                print(numworkers, 'worker came')
                num_stayed = 1
            elif numworkers == 0 or numworkers == 2:
                print(numworkers, 'workers came')
                num_stayed = numworkers
            else:
                print(numworkers, 'workers came (' + \
                str(numworkers - 2), 'went home)' )
                num_stayed = 2

            for k in range(num_stayed): # at most 2 workers stay to work
                displayUnscheduledWorkerHours(k+1, probabilities)
                print()
            print()

# ---- main

# init
num_members = 75
time_slots = ('8:00am', '10:00am', '12:00pm', '2:00pm', '4:00pm',
              '6:00pm')

days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')

sched_probabilities = {'CLate_15':15, 'CLate_30':5, 'CLate_45':2,
                       'CLEarly_15':5, 'CLEarly_30':3,'CNoshow':15}

unsched_probabilities = {'CLate_15':5, 'CLate_30':2, 'CLate_45':1,
                         'CLEarly_15':10, 'CLEarly_30':3,'CShowup':5}

# seed random number generator with system clock
random.seed()

# get type of simulation
print('Welcome to the Food Co-op Schedule Simulation Program')

valid_input = False
while not valid_input:
    try:
        response = int(input('(1)scheduled, (2)unscheduled simulation? '))

        while (response != 1) and (response != 2):
            print('Invalid Selection\n')
            response = \
                int(input('(1)scheduled, (2)unscheduled simulation? '))

        if response == 1:
            print('<< SCHEDULED WORKER SIMULATION >>\n')
            executeScheduledSimulation(sched_probabilities,
                                       days, time_slots)
        else:
            print('<< UNSCHEDULED WORKER SIMULATION >>\n')
            executeUnscheduledSimulation(unsched_probabilities,
                                         days, time_slots)

        valid_input = True

    except ValueError:
        print('Please enter numerical value 1 or 2\n')
