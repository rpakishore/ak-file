<!--- Heading --->
<div align="center">
  <img src="assets/banner.png" alt="banner" width="auto" height="auto" />
  <h1>ak-file</h1>
  <p>
    A base module to manipulate files and folders
  </p>
<h4>
    <a href="https://github.com/rpakishore/ak-file/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak-file">Documentation</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak-file/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak-file/issues/">Request Feature</a>
  </h4>
</div>
<br />

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rpakishore/ak-file)
![GitHub last commit](https://img.shields.io/github/last-commit/rpakishore/ak-file)
<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. About the Project](#1-about-the-project)
  - [1.2. Features](#12-features)
- [2. Getting Started](#2-getting-started)
  - [2.2. Dependencies](#22-dependencies)
  - [2.3. Installation](#23-installation)
- [3. Usage](#3-usage)
- [8. License](#8-license)
- [9. Contact](#9-contact)
- [10. Acknowledgements](#10-acknowledgements)

<!-- About the Project -->
## 1. About the Project
A base project to simplify file manipulation

<!-- Features -->
### 1.2. Features

- Can sanitize filename based on windows limitaions
- Can search for and return files with specified filenames

<!-- Getting Started -->
## 2. Getting Started

### 2.2. Dependencies
The repo comes pre-compiled with all dependencies.

<!-- Installation -->
### 2.3. Installation

Install my-project with npm

```bash
python -m venv .venv

venv\Scripts\activate.bat

pip install ak_file
```
<!-- Usage -->
## 3. Usage


```python
import ak_file
file = ak_file.File("<path/to/file>")
file.exists()

file.properties()
```

To sanitize filename
```python
from ak_file import sanitize
sanitize("Dirty_windows_file_name.ext")
```

To search for files with extension
```python
from ak_file import find_files_w_extension
find_files_w_extension(folder_path="Folder\path", extension="py", search_subdir=True)
```

<!-- License -->
## 8. License
See LICENSE.txt for more information.

<!-- Contact -->
## 9. Contact

Arun Kishore - [@rpakishore](mailto:pypi@rpakishore.co.in)

Project Link: [https://github.com/rpakishore/](https://github.com/rpakishore/)


<!-- Acknowledgments -->
## 10. Acknowledgements

Use this section to mention useful resources and libraries that you have used in your projects.

 - [Awesome README Template](https://github.com/Louis3797/awesome-readme-template/blob/main/README-WITHOUT-EMOJI.md)
 - [Banner Maker](https://banner.godori.dev/)
 - [Shields.io](https://shields.io/)
 - [Carbon](https://carbon.now.sh/)