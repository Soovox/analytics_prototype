from gearman import GearmanClient

class GMSIQClient(GearmanClient):
    def submit_job(self, *args, **kwargs):
        wait_until_complete = kwargs.get('wait_until_complete', False)
        background  = kwargs.get('background', True)
        kwargs['wait_until_complete'] = True if wait_until_complete else False
        kwargs['background'] = True if background else False

        return super(GMSIQClient, self).submit_job(*args, **kwargs)

job_servers = ['localhost:7005',]
gm_client = GMSIQClient(job_servers)
#gm_client = GearmanClient(job_servers)
completed_job_request = gm_client.submit_job("task_name", "arbitrary binary data")
