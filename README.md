

  ![Adorn](Adorn.gif)

        A one click support of black code formatter for IDEs and text editors.


### Requirements

* You must have any of the following text editor
   * [Gedit](https://wiki.gnome.org/Apps/Gedit)
   * Sublime Text 3

### Demo

* Gedit Demo

     ![gedit Demo](gedit/gedit.gif)

* Sublime Demo
       
     ![sublime Demo](sublime/sublime.gif)
        

### General Info
 * currently there is support for gedit and sublim only
 * Tested for root user only so A permission error may arise if used by another user(And these are visible only  though console).
 * For now run gedit or sublim with sudo only ``sudo gedit filename``
 
### Using
Sublim Text 3
 * steps
   * Select the snippet you want to format 
   * Right click on the window and then click on Adorn 

### Install
* Install with script
  * find install.sh file inside the folder gedit/sublime 
  * Open terminal and execute `sudo ./install.sh`
  
* Manual Install
  * Copy all contents of **folder that matches your gedit version** to path `~/.local/share/gedit/plugins/`
  * Install **python3** and **pip3** by `sudo apt-get install python3-all-dev python3-pip`
  * Install **black** by `sudo pip3 install black`


