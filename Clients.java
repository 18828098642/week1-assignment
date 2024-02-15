

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
//This is the code of clients
public class Clients {
    public static void main(String[] args) throws IOException{
        int PORTNUM = 1324;//create a port number for connection
        DatagramSocket clients = new DatagramSocket();//create a new socket
        System.out.println("The clients ready now . What you want to say?");//tell the user the clients is available now
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        InetAddress ip = InetAddress.getByName("192.168.56.1");//the ipv4 address of my computer
        String buffer = null;
        while((buffer = in.readLine()) != null){
            byte[] sendbuffer = buffer.getBytes();//create a new packet
            DatagramPacket sendPacket = new DatagramPacket(sendbuffer, sendbuffer.length,ip,PORTNUM);
            clients.send(sendPacket);
            byte[] recvbuffer = new byte[256];//receive the packet from server
            DatagramPacket recvPacket = new DatagramPacket(recvbuffer, recvbuffer.length);//receive the packet from server
            clients.receive(recvPacket);//receive the packet from server
            byte[] buf2 = recvPacket.getData();//receive the packet from server
            int len = recvPacket.getLength();//receive the packet from server
            String result = new String(buf2, 0, len);//receive the packet from server
            System.out.println("server:" + result);//output the message from server
            if("exit".equals(buffer))
                break;
        }
        clients.close();
        in.close();
    }
}

