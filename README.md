# raspberry_LCD_ecowhen
Repository to deploy the renewable forecast of ecowhen on an old LDC display using a rapberry pi

# Contributer
Andreas Geiges

# Installation
```
git clone git@github.com:geiges/raspberry_LCD_ecowhen.git

%create service file
/etc/systemd/system/your-service.service

%Reload the service files to include the new service.
sudo systemctl daemon-reload


%Start your service
sudo systemctl start your-service.service

%To check the status of your service
sudo systemctl status example.service

%To enable your service on every reboot
sudo systemctl enable example.service

%To disable your service on every reboot
sudo systemctl disable example.service
```

# Operation

sudo systemctl restart lcd_reshare.service
sudo systemctl status  lcd_reshare.service

