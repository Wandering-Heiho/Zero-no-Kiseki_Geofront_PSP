@echo off
if exist data.lst del data.lst
if exist output.iso del output.iso
if exist __pycache__ rmdir /s /q __pycache__
if exist arg\__pycache__ rmdir /s /q arg\__pycache__
if exist EBOOT\__pycache__ rmdir /s /q EBOOT\__pycache__
if exist misc\__pycache__ rmdir /s /q misc\__pycache__
if exist script\__pycache__ rmdir /s /q script\__pycache__
if exist text\__pycache__ rmdir /s /q text\__pycache__

if exist ISO rmdir /s /q ISO
if exist trashed rmdir /s /q trashed

del /s /q *.tsv >nul >2nul

if exist arg\orig rmdir /s /q arg\orig
if exist arg\output rmdir /s /q arg\output
del EBOOT\*.BIN >nul 2>nul
del misc\*.txt >nul 2>nul
del misc\*.orig >nul 2>nul
del misc\*.SFO >nul 2>nul

if exist script\dumped rmdir /s /q script\dumped
if exist script\HoL rmdir /s /q script\HoL
if exist script\merged rmdir /s /q script\merged
if exist script\orig rmdir /s /q script\orig
if exist script\output rmdir /s /q script\output
del script\*.ods >nul 2>nul

if exist text\orig rmdir /s /q text\orig
if exist text\output rmdir /s /q text\output