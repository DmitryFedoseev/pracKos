#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <cstring>
#include <iostream>
using namespace std;


// char message[] = "Hello there!\n";
// char buf[sizeof(message)];

int main()
{
    int sock;
    struct sockaddr_in addr;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if(sock < 0)
    {
        perror("socket");
        exit(1);
    }

    addr.sin_family = AF_INET;
    addr.sin_port = htons(5001); 
    addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    char buf[1024];
    if(connect(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0)
    {
        perror("connect");
        exit(2);
    }
    while(true)
    {
        // cin.clear();
        // cin.sync();
        string response;
        getline(cin, response);
        if(response=="flag")
        {
            break;
        }
        char *message;
        message = new char[response.length()];
        strcpy(message, response.c_str());
        sendto(sock, message, sizeof(message), 0, (struct sockaddr *)&addr, sizeof(addr));
        // send(sock, message, sizeof(message), 0);
        // recv(sock, buf, sizeof(message), 0);
        delete message;

    }
    close(sock);

    return 0;
}