# Logs merger

[![Maintainability](https://api.codeclimate.com/v1/badges/eaf040e366ea6f93dd35/maintainability)](https://codeclimate.com/github/Corrosion667/merge-logs/maintainability)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![linter-and-test-check](https://github.com/Corrosion667/python-project-lvl3/actions/workflows/linter-and-test-check.yml/badge.svg)](https://github.com/Corrosion667/python-project-lvl3/actions/workflows/linter-and-test-check.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/eaf040e366ea6f93dd35/test_coverage)](https://codeclimate.com/github/Corrosion667/merge-logs/test_coverage)

---

## **Logs merger** is a tool for merging two JSON log files.


### Running **as script**

Just copy from that repo file *merge_logs.py* and run it as common python script with the following syntax:
```bash
python3 merge_logs.py path/to/log1 path/to/log2 -o path/to/merged/log
```
Script also includes a shebang, so you can run it easier:
```bash
./merge_logs.py path/to/log1 path/to/log2 -o path/to/merged/log
```


### Running **as program**

**Logs merger** at the moment is stored only at *github* so the quickest and the easiest way to install it is to use *pip* with URL of repository.
```bash
pip install git+https://github.com/Corrosion667/merge-logs.git
```
In that case, basic **Logs merger** syntax looks like this:
```bash
merge-logs path/to/log1 path/to/log2 --output path/to/merged/log
```
*output* is an optional argument. By default, program will create file *merged.json* with merged logs in current working directory.

You can also recall about main features and syntax of a program using *help command*:
```bash
merge-logs -h
```

