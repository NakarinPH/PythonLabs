from listqueue import ListQueue


def round_robin(job_queue):
    """ Each job in the job queue has a time slice of
    10 time units. An unfinished job will be returned
    to the rear of the queue. """
    while job_queue:
        current_job = job_queue.pop()
        print("Current job:", current_job)
        if current_job > 10:
            print("Job unfinished. Return to the rear of the queue.")
            current_job = current_job - 10
            job_queue.add(current_job)
        else:
            print("Job finished")
        print("Job queue:", job_queue)



def test_round_robin():
    job_list = [17, 5, 32, 8, 24]
    job_queue = ListQueue(job_list)
    print("Initial job queue:", job_queue)
    round_robin(job_queue)


test_round_robin()
