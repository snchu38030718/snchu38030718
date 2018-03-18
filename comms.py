import socket
import array

class Ethernet:
    
    BUF_SIZE = 1024
    HOST_IP = ''
    PORT = 45000
    
    
    def __init__(self):
        # Set up socket and bind socket to port and local host IP
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.HOST_IP, self.PORT))
        
        # Receive first message from microgrid to acquire message identification
        print('Waiting for connection from microgrid...')
        data, self.address = self.s.recvfrom(self.BUF_SIZE)
        data_doubles = array.array('d', data)
        self.message_header = data_doubles[0]
        print('Connected!')
        
        
        # Close socket to prevent accumulation of data
        self.s.close()
        
    def status(self):
        # Set up socket and bind socket to port and local host IP
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.HOST_IP, self.PORT))
        
        # Receive latest microgrid data
        data, self.address = self.s.recvfrom(self.BUF_SIZE)
        # Rearrange data from bytes into an array
        # data_doubles = array.array('d', data)
        
        # Close socket to prevent accumulation of data
        self.s.close()
        return data[1:]
    
    
    def send(self, commands):  # Why we need commands here? Command is the data from status.
        # Set up socket and bind socket to port and local host IP
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.HOST_IP, self.PORT))
        
        # Rearrange data from array and include message identification
        #n = len(commands)
        
        message=array.array('d', [self.message_header])
#        message_length = array.array('d', [commands]) # h represent unsinged short
#        message=array.array('d',[])
        for i in range(1):
             message.append(commands[i])
#        
        # message.append( message_length)
        
        # Send data
        self.s.sendto(message, self.address)
        
        # Close socket to prevent accumulation of data
        self.s.close()
