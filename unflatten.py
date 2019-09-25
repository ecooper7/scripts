## ecooper 2019-09-04
## re-sort flattened data, e.g. VCTK
## makes directories based on the first part of the filename before a _

## change these to your directories
indir='/Users/ecooper/data/vctk_hpf_48k_flat'
outdir='/Users/ecooper/data/vctk_hpf/wav48'

import os

wavs = [x for x in os.listdir(indir)]

for w in wavs:
    parts = w.split('_')
    spkr = parts[0]
    outpath = os.path.join(outdir, spkr)
    try:
        os.mkdir(outpath)
    except:
        pass
    cmd = 'cp ' + os.path.join(indir, w) + ' ' + os.path.join(outpath, w)
    print(cmd)
    os.system(cmd)
