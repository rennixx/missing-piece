# MP-AS Positive Fixture: Async queue job without dead-letter recovery
class JobWorker:
    def process_job(self, job_data):
        # NOTE: If exception occurs, job is dropped without retry limit or dead-letter queue!
        do_work(job_data)
