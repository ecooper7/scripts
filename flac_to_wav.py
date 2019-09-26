## ecooper 2019-09-04
## convert vctk 0.91 mic2.flac files to wav

import os

## change these to your directrories
indir = '/tmp/cooper/data/VCTK-Corpus-0.91-trimmed2/wav48/'
outdir = '/tmp/cooper/data/vctk0.91_wav/'

for d in os.listdir(indir):
    if '.' not in d:
        flacs = os.listdir(indir + d)
        for f in flacs:
            if 'mic2' in f:
                cmd = 'sox ' + indir + d + '/' + f + ' ' + outdir + '_'.join(f.split('_')[0:2]) + '.wav'
                print(cmd)
                os.system(cmd)
