from nautobot.apps.jobs import Job, ObjectVar, register_jobs
from nautobot.dcim.models import Location, Device
from nautobot.extras.models import Status
import socket

name = "test"

class PingJob(Job):
    class Meta:
        name = "Device Reachability Test"
        description = "This job pings all the devices in the database."

    location = ObjectVar(model=Location, required=True)

    def ping(self, ip):
        try:
            socket.create_connection((ip, 22), timeout=2)
            return True
        except OSError:
            return False

    def run(self, location):
        devices = Device.objects.filter(location=location, primary_ip4__isnull = False)
        for device in devices:
            ip = str(device.primary_ip4.address.ip)
            if self.ping(ip):
                self.logger.info(f"{device.name} ({ip}) is reachable")
                device.status = Status.objects.get(name="Active")
            else:
                self.logger.warning(f"device.name ({ip}) is unreachable")
                device.status = Status.objects.get(name="Offline")
            
            device.save()

register_jobs(PingJob)
