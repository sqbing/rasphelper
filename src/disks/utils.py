def get_disk_uuid(device):
    import commands
    try:
        return commands.getstatusoutput("blkid "+device)[1].split(' ')[1].split('=')[1][1:-1]
    except Exception, data:
        return ""
    pass
