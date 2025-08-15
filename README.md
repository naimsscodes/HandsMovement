Hands Detection Movement
Introduction

This guide will help you set up a Python environment for the Hands Detection Movement project.
⚠ Important: Mediapipe currently does not support Python 3.13 or above. You must use Python 3.11.

Output di GitHub:
---

## Step 1: Check Your Python Version
 - Make sure you have Python 3.11 installed.
- Open a terminal (Command Prompt, PowerShell, or Terminal) and run:
  ```bash
  python --version
  ```
  - If the version is 3.11.x, you are good to go.
  - If the version is 3.11.x, you are good to go.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**If You Already Have Python 3.13 or Above**
You do not need to uninstall your current Python.
Instead, create a virtual environment using Python 3.11.

- Create a Virtual Environment
```bash
  py -3.11 -m venv myenv
```
- py -3.11 → Use Python version 3.11
- -m venv → Module for creating a virtual environment
- myenv → Name of your environment folder (you can change it to anything you like)

  After running this, a folder named myenv will appear in your project directory.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Step 2: Activate the Virtual Environment**
- Windows (Command Prompt)
```bash
myenv\Scripts\activate
```
- Windows (PowerShell)
```bash
.\myenv\Scripts\Activate.ps1
```
- Mac / Linux
```bash
source myenv/bin/activate
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Step 3: Install Required Packages**
Once your virtual environment is activated, install the required Python libraries.
Install Mediapipe

- Midepipe is used for hand tracking and gesture recognition.
- Make sure you are inside the activated virtual environment/env python 3.11 before runinng the command
```bash
pip install mediapipe
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Install PyAutoGUI**
- PyAutoGUI allows you to control the mouse, keyboard, and screen automation.
```bash
pip install pyautogui
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Verify the Installation**
- After installing, you can check if both packages are installed:
  ```bash
  pip list
  ```
- You should see:
  ```bash
  mediapipe   <version>
  pyautogui   <version>
   ```
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Optional: Install OpenCV (Recommended)**
- OpenCV will help in video capturing and image processing.

```bash
pip install opencv-python
```



  

  



