# raspberry_LCD_ecowhen
Repository to deploy the renewable forecast of ecowhen on an old LDC display using a rapberry pi

# Contributer
Andreas Geiges

# Installation
```
git clone git@github.com:geiges/raspberry_LCD_ecowhen.git

%create service file (use template.service in this repo)
cp template.service /etc/systemd/system/lcd_reshare.service 

%Reload the service files to include the new service.
sudo systemctl daemon-reload

% Apply correct rights to startup file
sudo chmod 744 lcd_reshare.sh 

%Start your service
sudo systemctl start lcd_reshare.service

%To check the status of your service
sudo systemctl status lcd_reshare.service

%To enable your service on every reboot
sudo systemctl enable lcd_reshare.service

%To disable your service on every reboot
sudo systemctl disable lcd_reshare.service


```

# Operation

``` 
% restart deamon    
sudo systemctl restart lcd_reshare.service

% check status of deamon
sudo systemctl status  lcd_reshare.service
```
