from flask import Flask
from flask import request
from flask import render_template
from psutil import disk_partitions
import logging
from src.disks.utils import get_disk_uuid

app = Flask(__name__)

@app.route("/")
def hello():
    disk_partitions_ret = disk_partitions(all=True)
    all_disk_partitions = []
    for disk in disk_partitions_ret:
        disk_info = {}
        if disk.device != "":
            disk_info["uuid"] = get_disk_uuid(disk.device)
        disk_info["device"] = disk.device
        disk_info["mountpoint"] = disk.mountpoint
        disk_info["fstype"] = disk.fstype
        disk_info["opts"] = disk.opts
        all_disk_partitions.append(disk_info)
        pass
    return render_template("index.html", all_disk_partitions=all_disk_partitions)

if __name__ == "__main__":
    app.run(debug=True)
