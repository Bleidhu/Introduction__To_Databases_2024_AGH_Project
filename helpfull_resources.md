
## Markdown
https://www.markdownguide.org/cheat-sheet/

Markdown Editor:

https://hackmd.io/

HackMd will be used, but due to it's limited push count it's hard to push all changes to github. I think about ubgrading to premium plan, but for now workflow is like that:
- Note is created on someones account
- It should be shared -> throught share
- Every consecutive version should be added to github by downloading file and placing it in directory folder

For now i am generating pdf documents by this command on linux 

```bash
pandoc -V geometry:margin=1in -V colorlinks=true -V linkcolor=blue -o output.pdf ./docs/pbd_13_15_zesp_1_raportx.md ./docs/database_specification.md ./docs/functionalities.md
```

to save minutes of runs of github actions (because now i am using gh pages to publish materials)

Usage guide for this is:
- open repository root folder
- run `pandoc -V geometry:margin=1in -V colorlinks=true -V linkcolor=blue -o output.pdf ./docs/pbd_13_15_zesp_1_raportx.md ./docs/file1 ./docs/file2 ./docs/file3`
- You can use any number of files - they will be merged in order they were supplied. Only thing required is `./docs/pbd_13_15_zesp_1_raportx.md` where You should edit number of the report to match desired numbering. This file is template for report header.

Also all of the images should be placed in ./docs/images and referenced using
```markdown
![alt_text](./docs/images/your_image.image_extension)
```

## Github Pages

All of the docs are published by running github publish action. 
