import os
import json
import shutil
import subprocess
def get_device_from_mount(fs):
    return subprocess.run([
        "findmnt",
        "-o",
        "source",
        "-n",
        "--target",
        fs,
        ],stdout=subprocess.PIPE).stdout.strip()
gb=1024*1024*1024
fs=['/var', '/usr', '/', '/opt']
need_free=2*gb
#find the low space directory/directories
for i in fs:
    usage = shutil.disk_usage(i)
    if usage.free <= need_free:
        print("fs {} has {} gb free".format(i, usage.free/gb)) #Tell the user that these directories are full or almost full.
       # print("fs {} has source {}".format(i, get_device_from_mount(i)))
        print("{}".format(get_device_from_mount(i).decode()))
        # this is the mount use to lvextend.

        UNIT = 'g'    #need to get it to check the filesystems pv
        THRESHOLD = 1
        pvs = json.loads(subprocess.run(["pvs", "--units", UNIT, "--reportformat", "json"], stdout=subprocess.PIPE).stdout)
        for pv in pvs['report'][0]['pv']:
            if float(pv['pv_free'].strip(UNIT)) > THRESHOLD:
                #print("VG {} has {} free".format(pv['vg_name'], pv['pv_free']))   ############ change if want to see space even is above threshold
                lvmname = ("{}".format(get_device_from_mount(i).decode()))
            #lvmname = get_device_from_mount(i).decode()     <--------- can possible be used to get lvm, not tested
                size = "2G"
                os.system(f"lvextend -L +{size} {lvmname} --resizefs")
        else:
            print("VG {} has {} free".format(pv['vg_name'], pv['pv_free']))