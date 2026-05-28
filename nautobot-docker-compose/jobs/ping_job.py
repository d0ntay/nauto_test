from nautobot.apps.jobs import Job, ObjectVar, register_jobs
from nautobot.dcim.models.devices import Device

class PingJob(Job):
    class Meta:
        name = "Device Reachability Test"
        description = "This job pings all the devices in the database."

    device = ObjectVar(model=Device.platform, required=True)

    def run(self):
        self.logger.info(f"Device {device}")




register_jobs(PingJob)
