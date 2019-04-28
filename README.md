# Systems-ProgrammingTGT


## Development tools

1. Python 3


### Prerequisites

There is only 1 Prerequisite which is very very important, that is to use python 3 do not use python2.


| Prerequisite                                                           |  Version  |
| -----------------------------------------------------------------------|-----------|
| [Python 3](https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz)|`~ ^ 3.5.2`|


## Note:-

1.) The file size is ordered in descending order for better readability by this the file with max size is always on top.

2.) Few fields have been added to the json like date_captured & path supplied which can be an important information for later point in time

3.) I have used OrderedDict so that Path supplied & Date captured can be read first for human readability 

4.) The output is appended to the to a textfile called as `FileSizeDump.txt`, this file will be created in the place for the path supplied

### Script Usage
python3 getFileSize.py 'supply path here'


### Output 1


hasan@hasan-550p5c-550p7c:~/Desktop/Development/Target/Systems-ProgrammingTGT$ python3 getFileSize.py /home/hasan/Desktop/FolderSize/important\ documents/

The path is  /home/hasan/Desktop/FolderSize/important documents/

Printing the json for temporary reference, json will be appended & dumped in a text file with the name FileSizeDump.txt inside the supplied path

```
{
    "pathSupplied": "/home/hasan/Desktop/FolderSize/important documents/",
    "date_captured": "2019-04-27 17:30:18.490180",
    "files": {
        "/home/hasan/Desktop/FolderSize/important documents/aadhar card 1.pdf": 931527,
        "/home/hasan/Desktop/FolderSize/important documents/person2/person2 passport, front aadhar card, front IT card, front Election card .pdf": 910980,
        "/home/hasan/Desktop/FolderSize/important documents/person4/person4 only passport,aadhar,elcetion and pan.pdf": 886875,
        "/home/hasan/Desktop/FolderSize/important documents/person3/person3 passport fron, election card front and aadhar card front.pdf": 857443,
        "/home/hasan/Desktop/FolderSize/important documents/person2/person2 passport, back aadhar card, back IT card, back election card.pdf": 832775,
        "/home/hasan/Desktop/FolderSize/important documents/person3/person3 passport back, election card back and aadhar back.pdf": 779144,
        "/home/hasan/Desktop/FolderSize/important documents/parents passport backside.pdf": 773233,
        "/home/hasan/Desktop/FolderSize/important documents/person4/person4 only passport,aadhar, election and pan backside.pdf": 766988,
        "/home/hasan/Desktop/FolderSize/important documents/kids passport back.pdf": 737781,
        "/home/hasan/Desktop/FolderSize/important documents/person1/person1 passport front and aadhar card front.pdf": 720376,
        "/home/hasan/Desktop/FolderSize/important documents/Scanned Document.pdf": 675664,
        "/home/hasan/Desktop/FolderSize/important documents/kids passport.pdf": 664393,
        "/home/hasan/Desktop/FolderSize/important documents/person1/person1 passport and aadhar card backside.pdf": 640048,
        "/home/hasan/Desktop/FolderSize/important documents/person4/ration card.pdf": 629704,
        "/home/hasan/Desktop/FolderSize/important documents/ration card.pdf": 629704,
        "/home/hasan/Desktop/FolderSize/important documents/person1/ration card.pdf": 629704,
        "/home/hasan/Desktop/FolderSize/important documents/person2/ration card.pdf": 629704,
        "/home/hasan/Desktop/FolderSize/important documents/person3/ration card.pdf": 629704,
        "/home/hasan/Desktop/FolderSize/important documents/parents passport.pdf": 601209,
        "/home/hasan/Desktop/FolderSize/important documents/aadhar card2.pdf": 461757,
        "/home/hasan/Desktop/FolderSize/important documents/person4/person4.pdf": 301293
    }
}
```


### Output 2

hasan@hasan-550p5c-550p7c:~/Desktop/Development/Target/Systems-ProgrammingTGT$ python3 getFileSize.py /home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/

The path is  /home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/

Printing the json for temporary reference, json will be appended & dumped in a text file with the name FileSizeDump.txt inside the supplied path

```
{
    "pathSupplied": "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/",
    "date_captured": "2019-04-27 17:24:58.462572",
    "files": {
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/pre-rebase.sample": 4898,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/FileSizeDump.txt": 4341,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/update.sample": 3610,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/getFileSize.py": 2908,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/pre-commit.sample": 1642,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/pre-push.sample": 1348,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/prepare-commit-msg.sample": 1239,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/objects/9f/52e0f2f636ce3f5757b12dc852415bc452a4c2": 1175,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/objects/eb/05517edec70bf1cab206be0c845cd7797b3ad7": 1158,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/commit-msg.sample": 896,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/objects/1f/4dad9b06b98ed0ee9853e7e0df2583fb03f0b7": 570,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/objects/5a/156ed94dabc4aaf1ade9836c3f68ee436fea46": 519,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/applypatch-msg.sample": 478,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/logs/refs/heads/master": 449,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/logs/HEAD": 449,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/pre-applypatch.sample": 424,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/index": 297,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/config": 282,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/info/exclude": 240,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/objects/a5/264c91fc648af1ac419f5ac25f1c1ebb03c1d2": 220,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/logs/refs/remotes/origin/HEAD": 209,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/hooks/post-update.sample": 189,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/logs/refs/remotes/origin/master": 154,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/objects/6d/9e27e61654cf6a8173b3124d37ba82d61d1eab": 128,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/packed-refs": 107,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/COMMIT_EDITMSG": 93,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/description": 73,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/objects/bf/ed04a5b847701433d96ad278f3c3b8301495d3": 54,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/objects/f8/b3f7dd1fdc2c4b79fd2b4a95199eff6febcf68": 47,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/README.md": 45,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/refs/heads/master": 41,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/refs/remotes/origin/master": 41,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/refs/remotes/origin/HEAD": 32,
        "/home/hasan/Desktop/Development/Target/Systems-ProgrammingTGT/.git/HEAD": 23
    }
}
```
