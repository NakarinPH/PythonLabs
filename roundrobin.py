from listqueue import ListQueue


def round_robin(job_queue):
    """ Each job in the job queue has a time slice of
    10 time units. An unfinished job will be returned
    to the rear of the queue. """
    pass


def test_round_robin():
    job_list = [17, 5, 32, 8, 24]
    job_queue = ListQueue(job_list)
    print("Initial job queue:", job_queue)
    round_robin(job_queue)


test_round_robin()