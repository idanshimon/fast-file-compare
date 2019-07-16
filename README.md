# fast-compare
## Description
hash based file compare adapted for processing big files, uses multiprocessing for better performence

## Optimizations
Code is optimized to work with multiprocessing
Fast compare optimize usage for RAM and CPU cores depending on the file size in order not to exhoust the system resources.

## How to Run
```bash
>python fast_compare.py 5GB_FILE 5GB_FILE
CPU COUNT: 4
compute hash for file 5GB_FILE (starting index:0, size:1342177280)
compute hash for file 5GB_FILE (starting index:1342177280, size:1342177280)
compute hash for file 5GB_FILE (starting index:2684354560, size:1342177280)
compute hash for file 5GB_FILE (starting index:4026531840, size:1342177280)
Compute hash for 5GB_FILE Took 4.439167 seconds (Size:5076332544)
compute hash for file 5GB_FILE (starting index:0, size:1342177280)
compute hash for file 5GB_FILE (starting index:1342177280, size:1342177280)
compute hash for file 5GB_FILE (starting index:2684354560, size:1342177280)
compute hash for file 5GB_FILE (starting index:4026531840, size:1342177280)
Compute hash for 5GB_FILE Took 5.604822 seconds (Size:5076332544)
Compare Took 11.373840 seconds
All Good!
```

```bash
# Without DEBUG
> python fast_compare.py 5GB_FILE 5GB_FILE
Compare Took 10.133742 seconds
All Good!
```

```bash
# IN DEBUG
> python fast_compare.py md4sum64.exe md5sum64.exe
CPU COUNT: 4
compute hash for file md4sum64.exe (starting index:0, size:None)
compute hash for file md5sum64.exe (starting index:0, size:None)
Error: Files content is not the same
Compare Took 0.003990 seconds
Error: Files are not equal
```
