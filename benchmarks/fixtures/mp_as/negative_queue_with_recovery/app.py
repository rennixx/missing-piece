# MP-AS Negative Fixture: Async queue job WITH retry limit and DLQ
class JobWorker:
    def process_job(self, job_data):
        try:
            do_work(job_data)
        except Exception as e:
            if job_data.retries >= 3:
                self.dead_letter_queue.push(job_data, str(e))
            else:
                self.retry_queue.push(job_data)
