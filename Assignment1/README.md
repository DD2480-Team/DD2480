![made-with-python](https://img.shields.io/badge/Made%20with-Python3-brightgreen)

<!-- LOGO -->
<br />
<h1>
    <p align="center">
        <a href="https://emoji.gg/emoji/ngameboy"><img src="https://emoji.gg/assets/emoji/ngameboy.png"
    alt="Logo" width="110" height="110"> 
    </h1>
<p align="center">
    Software Engineering Fundamentals <br> Group 28
</p>

<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#usage">Usage</a> •
  <a href="#input-files-format">Input files format</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>  
                                                              
## About The Project

This project corresponds to Software Engineering (DD2480) Assignment 1.   

The DECIDE() function (hypothetical anti-ballistic system) generates a boolean signal which determines whether an interceptor should be
launched based on the input parameters described in the input file format.


The launch decision, is printed as ”YES” or ”NO” on the standard output.

## Usage

1. Clone this repository
2. Inside a shell, run:
```sh
$ python main.py True
```
or 

```sh
$ python main.py False
```


## Input files format

To use the parser (`parser.py`) with a text file, the arguments should follow this form, in this order, with a new line between each argument.



| Parameter type | Parameter name |
| -------------- | -------------- |
| int            | numpoints      |
| list           | points         |
| float          | length1        |
| float          | radius1        |
| float          | epsilon        |
| float          | area1          |
| float          | Q_PTS          |
| float          | quads          |
| float          | dist           |
| int            | N_PTS          |
| int            | K_PTS          |
| int            | A_PTS          |
| int            | B_PTS          |
| int            | C_PTS          |
| int            | D_PTS          |
| int            | E_PTS          |
| int            | F_PTS          |
| int            | G_PTS          |
| float          | length2        |
| float          | radius2        |
| float          | area2          |
| list           | LCM            |
| list           | PUV            |

## Credits
Work by Group 28. Our processes and workflow [are documented and summarised](https://docs.google.com/document/d/1Op0DMf0LeIO14TsSgexQ96vfdH4YPQFiMd0sS3l7H8Q/edit) in a separate document.

### Individual contributions

Yen Chen: CMV conditions, PUM.
Joel Lützow: CMV conditions, refactoring, organising workflow.
Ai Maiga: parser file, CMV conditions, Readme.
Gautam Manek: CMV conditions, refactoring.
Jacob Mimms: CMV conditions, parser file.


Group [logo](https://emoji.gg/emoji/ngameboy).

## License
Usage is provided under the [MIT License](http://http//opensource.org/licenses/mit-license.php). See LICENSE for the full details.