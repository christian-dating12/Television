# CHRISTIAN M. DATING | BSCPE 1-5

class Television:

    # Define self, channel, volume, status_TV.
    def __init__(self, channel, volume, status_TV):
        self.get_channel = channel
        self.get_volume = volume 
        self.status_TV = status_TV

        # channel (1-120)
        if self.get_channel > 120:
            self.get_channel = 120
        elif self.get_channel < 1:
            self.get_channel = 1
        # volume (1-7)  
        if self.get_volume > 7:
            self.get_volume = 7
        elif self.get_volume < 1:
            self.get_volume = 1

    # If true, turn on tv
    def turn_on(self):
        self.status_TV = True
    # If false, turn off tv
    def turn_off(self):
        self.status_TV = False

    # parameter in getting the channel
    def get_channel(self):
        if self.get_channel > 120:
            self.get_channel = 120
        elif self.get_channel < 1:
            self.get_channel = 1
        return self.get_channel
    # parameter in getting the volume
    def get_volume(self):
        if self.get_volume > 7:
            self.get_volume = 7
        elif self.get_volume < 1:
            self.get_volume = 1
        return self.get_volume
    
    # set new channel between 1-120
    def set_channel(self, any_channel):
        self.get_channel = any_channel
        if self.get_channel > 120:
            self.get_channel = 120
        elif self.get_channel < 1:
            self.get_channel = 1

    # set new volume between 1-7
    def set_volume(self, any_volume):
        self.get_volume = any_volume
        if self.get_volume > 7:
            self.get_volume = 7
        elif self.get_volume < 1:
            self.get_volume = 1

    # Increase the channel number by 1
    def channel_up(self):
        if self.get_channel <= 119:
            self.get_channel = self.get_channel + 1
    # Decrease the channel number by 1
    def channel_down(self):
        if self.get_channel >= 2:
            self.get_channel = self.get_channel - 1

    # Increase the volume level by 1
    def volume_up(self):
        if self.get_volume <= 6:
            self.get_volume = self.get_volume + 1
    # Decrease the volume level by 1
    def volume_down(self):
        if self.get_volume >= 2:
            self.get_volume = self.get_volume - 1