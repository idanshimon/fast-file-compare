# fast-compare
## Description
hash based file compare adapted for processing big files, uses multiprocessing for better performence

## Optimizations
Code is optimized to work with multiprocessing
Fast compare optimize usage for RAM and CPU cores depending on the file size in order not to exhoust the system resources.

## Configuration 
You may configure the hashing algorithm that is used to compare the files / chunks 

the default is md4

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

```bash
# More errors
>python fast_compare.py md5sum64.exe md4sum64.exe
CPU COUNT: 4
compute hash for file md5sum64.exe (starting index:0, size:None)
compute hash for file md4sum64.exe (starting index:0, size:None)
Error: Files content is not the same
src file hash data:
[(0, '4252fcfd67b793dd4f6720460e6600e5')]
dest file hash data:
[(0, '4989ee08179957531959ecb7d84b980a')]
Compare Took 0.044446 seconds
Error: Files are not equal
```

## Benchmarks
### Other Checksum Tools (Single File)
```powershell
PS C:\tmp> Measure-Command {.\ed2ksum64.exe "5GB_FILE"} | findstr 'TotalMilliseconds'                                   TotalMilliseconds : 10063.4238
PS C:\tmp> Measure-Command {.\md5sum64.exe "5GB_FILE"} | findstr 'TotalMilliseconds'                                    TotalMilliseconds : 13034.5479
PS C:\tmp> Measure-Command {.\md4sum64.exe "5GB_FILE"} | findstr 'TotalMilliseconds'                                    TotalMilliseconds : 9225.0143
PS C:\tmp> Measure-Command {.\crc32sum64.exe "5GB_FILE"} | findstr 'TotalMilliseconds'                                  TotalMilliseconds : 14036.2998
```
### Fast Compare
**Compute hash for 5GB_FILE Took 4.439167 seconds (Size:5076332544)**

Fast compare - Single file result shows an improvement of over 50% ! rather than using the traditional tools like md4sum etc.
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
