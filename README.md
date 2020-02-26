# links

https://github.com/DawesLab/Instruments/blob/master/instrument.py
https://github.com/rdpoor/rigol-grab/blob/master/rigol_grab.py
https://pyvisa.readthedocs.io/en/master/
https://groups.google.com/forum/#!searchin/python-ivi/trigger%7Csort:date/python-ivi/9FXwLXqP2NM/2THd9_CoAQAJ
https://askubuntu.com/questions/257636/how-to-connect-tektronix-tds10001b-to-ubuntu

https://hackaday.com/2016/11/16/how-to-control-your-instruments-from-a-computer-its-easier-than-you-think/

download.tek.com/manual/077009701_RevA_web.pdf

# install

visa seems better for the tek scope. well documented manual

    sudo pip install -r requirements.txt
    sudo apt-get install libusb-dev

make new udev rules containing

    # USBTMC instruments

    # ms2004b 0699, idProduct=039c
    SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="0699", ATTRS{idProduct}=="039c", GROUP="usbtmc", MODE="0660"

then

    sudo udevadm control --reload-rules

then should be able to list devices with 

    import visa, time
    resources = visa.ResourceManager('@py')
    print(resources.list_resources())

if this doesn't work, try running with sudo and fix permissions
