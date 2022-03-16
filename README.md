# Two_Do

## 1.To Install Two_Do

### 1.1 For Linux

#### 1.1.1 The easiest option to install.

Go to the releases tab of this repo and download the binary called two_do. After downloading the binary, you should now do something similiar to the following.

```
$ cd Downloads/ 
$ chmod +x two_do
```

You can now use this binary (if everything went well) by doing the following.

```
$ ./two_do
```

To use this binary no matter the directory you are in while using your terminal you will need to store it in location that is on path. On my linux device I have to go through this process.

```
$ cd Downloads/
$ sudo cp two_do /usr/local/bin/
```

You should now be able to run the program just by typing

```
$ two_do
```

When a installer prompt pops up proceed with the installation, do not worry about it. It is just creating the empty files on your computer where it will store the goals. If using the inbuilt installer which is discussed in 1.1.2. It does a bit more than that. I would highly suggest using this method and not the second one.

#### 1.1.2 Using the inbuilt installer

two_do installation using the inbuilt installer is currently very unstable. The installation will currently only work on some linux and mac devices. To install two_do just clone this repository and open your terminal. Change into the repo directory and do the following. 

```
$ python3 two_do.py
```  

This should do a bunch of commands for you to hopefully sucessfully install two_do as binary you can access anywhere.
