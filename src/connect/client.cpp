#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <cstring>
#include <iostream>
#include <fcntl.h>
using namespace std;


// char message[] = "Hello there!\n";
// char buf[sizeof(message)];

int main()
{
    int sock;
    struct sockaddr_in addr;
    char buf[512];
    int bytes_read = 0;
    string response;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if(sock < 0)
    {
        perror("socket");
        exit(1);
    }

    addr.sin_family = AF_INET;
    addr.sin_port = htons(5000); 
    addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    
    if(connect(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0)
    {
        perror("connect");
        exit(2);
    }
        while(true)
        { 
            bytes_read = read(sock, buf, sizeof(buf));
            if(bytes_read <= 0)
            {
                break;
            }
            buf[bytes_read] = '\0';
            cout << buf;
        }
    close(sock);

    return 0;
}