# Learning-Compressor
Machine-Learning powered data compressor for command line

## Planned updates
1: Need to add auto-zip functionality to finishing error file
   • Large files have low clusters of errors. If M total errors in file prediction, and N total file length, expected magnitude of error file goes from Mlog(N) to        Mlog(N/M)+M for an average decrease of (M-1)log(M)~Mlog(M) error file size.
