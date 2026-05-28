from nautobot.apps.jobs import Job, ObjectVar, register_jobs
from nautobot.dcim.models import Device

name = "test"

class PingJob(Job):
    class Meta:
        name = "Device Reachability Test"
        description = "This job pings all the devices in the database."

    device = ObjectVar(model=Device, required=True)

    def run(self, device):
        self.logger.info(f"Device {device.name}")




register_jobs(PingJob)
