## ecooper 2019-09-25
## take things in directories (such as VCTK data) and flatten them

## change these to your directories
indir='/Users/ecooper/data/VCTK-Corpus-0.91-trimmed2/wav48'
outdir='/Users/ecooper/data/vctk-flat'

import os

for f in os.listdir(indir):
    d = os.path.join(indir, f)
    if os.path.isdir(d):
        wavs = os.listdir(d)
        for w in wavs:
            cmd = 'cp ' + os.path.join(d, w) + ' ' + os.path.join(outdir, w)
            print(cmd)
            os.system(cmd)
