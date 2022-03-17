# Two_Do

## 1.To Install Two_Do

### 1.1 For Linux

#### 1.1.1 The easiest option to install.

Go to the releases tab of this repo and download the binary called two_do. After downloading the binary, you should now do something similiar to the following.

```bash
$ cd Downloads/ 
$ chmod +x two_do
```

You can now use this binary (if everything went well) by doing the following.

```bash
$ ./two_do
```

To use this binary no matter the directory you are in while using your terminal you will need to store it in location that is on path. On my linux device I have to go through this process.

```bash
$ cd Downloads/
$ sudo cp two_do /usr/local/bin/
```

You should now be able to run the program just by typing

```bash
$ two_do
```

When a installer prompt pops up proceed with the installation, do not worry about it. It is just creating the empty files on your computer where it will store the goals. If using the inbuilt installer which is discussed in 1.1.2. It does a bit more than that. I would highly suggest using this method and not the second one.

#### 1.1.2 Using the inbuilt installer

two_do installation using the inbuilt installer is currently very unstable. The installation will currently only work on some linux and mac devices. To install two_do just clone this repository and open your terminal. Change into the repo directory and do the following. 

```bash
$ python3 two_do.py
```  

This should do a bunch of commands for you to hopefully sucessfully install two_do as binary you can access anywhere.


## 2. Running Two Do For The First Time

### 2.1 Install Prompt

When running two_do for the first time regardless of the installation method, it will display a prompt that looks as follows.

```
Install/Reset todo program?[Installation will only work on some Linux devides)(y\n):
```

If you just press enter it will proceed with the installation process. This is primarily to just create the folders and files where your goals will be stored on your computer. After this it should display a bunch of output, you just need to worry about the last line that should say...

```
INSTALL COMPLETE
```

### 2.2 Running the program after installation again

When you run the program again it should not have a installation prompt, it should display the main menu that should look like this. 

```
[?] Main Menu: Complete Goal
 > Complete Goal
   View Goals
   Add Goal
   View Goal Classifications
   Add Goal Classification
   Reset
   Exit
```

If this menu is displayed, your installation was sucessful and your program is working!!

## 3. How to use the two_do program

### 3.1 Goal Classifications

#### 3.1.1 Add Goal Classification

This is the first thing you want to do after installing and running the two_do program. You need to have goal classifications to start creating goals.
To do this select the 'Add Goal Classification' option on the main menu in the two_do program. The following code block displays an example of what will happen and what is expected from the user when this command is run.

```
? Enter Goal Classification: MISC
? Enter Goal Classification Name: Other
Added Goal Classification
```

#### 3.1.2 View Goal Classification

This is how you will view the goal classifications you have created on your computer. To do this select the 'View Goal Classifications' option on the main menu. Example output is below.

```
Goal Classification    Goal Classification Name
---------------------  --------------------------
PF                     Portfolio
MISC                   Other
```

### 3.2 Goals

#### 3.2.1 Adding Goals

Now that you have added your goal classifications, you can start to add goals. To do this select the 'Add Goal' option on the main menu. The following code block displays an example of what will happen and what is expected from the user when this command is run.

```
[?] Main Menu: Add Goal
   Complete Goal
   View Goals
 > Add Goal
   View Goal Classifications
   Add Goal Classification
   Reset
   Exit

[?] Goal Term: Medium Term
   Short Term
 > Medium Term
   Long Term

? What is the goal?: Push my updated two_do program to Github
[?] Goal Classification: MISC-Other
 > MISC-Other
```

#### 3.2.2 Viewing Goals

##### 3.2.2.1 Using the main menu

This is how you will view the goals you have created on your computer. To do this select the 'View Goals' option on the main menu. Example output is below.

```
[?] Main Menu: View Goals
   Complete Goal
 > View Goals
   Add Goal
   View Goal Classifications
   Add Goal Classification
   Reset
   Exit


Goal                                            Term         Classification
----------------------------------------------  -----------  ----------------
Push my updated two_do program to Github        Medium Term  MISC-Other

```

##### 3.2.2.2 Using the program with an argument

You can also just view your goals by doing the following

```
$ two_do view
```

This will not spawn a main menu, this will just directly output the goals. 
This is so you can use grep on the program to filter the goals. Examples of this would be

```
$ two_do view | grep "Other"
$ two_do view | grep "MISC"
$ two_do view | grep "Medium"
$ two_do view | grep "Medium Term"
```

#### 3.2.3 Completing Goals

The final part is now to complete your goal. To do this select the 'Complete Goal' option on the main menu. Example output is below.

```
[?] Main Menu: Complete Goal
 > Complete Goal
   View Goals
   Add Goal
   View Goal Classifications
   Add Goal Classification
   Reset
   Exit

[?] Goals: Push my updated two_do program to Github - Medium Term - MISC-Other
 > Push my updated two_do program to Github - Medium Term - MISC-Other

Goal Marked As Complete
```

Now when you view the goals, it will have the goal selected removed.

### 3.3 Reset

This option is still under development to get it working, right now this option will not do much.
To actually reset your program do the following. Resetting your program will remove all your goals. There is no restore option for these goals.

```bash
$ cd
$ rm -r .todo/
$ rmdir .todo/
```
