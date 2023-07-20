#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8484

int generate_random_number() {
    return (rand() % 999);
}

int main() {
    int sockfd, newsockfd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    char buffer[1024];

    // Create socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Error creating socket");
        return 1;
    }

    // Server address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    // Bind socket 
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Binding error");
        return 1;
    }

    // Listening
    if (listen(sockfd, 5) < 0) {
        perror("Listening error");
        return 1;
    }

    printf("Server listening on port %d...\n", PORT);

    while (1) {
        // Accept client 
        newsockfd = accept(sockfd, (struct sockaddr*)&client_addr, &client_len);
        if (newsockfd < 0) {
            perror("Error accepting connection");
            return 1;
        }

        // Random number
        int random_number = generate_random_number();

        // Send 
        snprintf(buffer, sizeof(buffer), "%d", random_number);
        send(newsockfd, buffer, strlen(buffer), 0);

        // Close
        close(newsockfd);
    }

    close(sockfd);
    return 0;
}
