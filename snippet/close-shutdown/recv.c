#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <pthread.h>

/*
 * gcc -lpthread -Dact_close
 * or
 * gcc -lpthread -Dact_shutdown
 */

int fd;

void* worker(void *data)
{
    int rc;
    usleep( 1000*100 );

#if act_close == 1
    rc = close( fd );
    printf("OK closed\n");
#else
    rc = shutdown( fd, SHUT_RDWR );
    printf("OK shutdown\n");
#endif
}

int main( int argc, char **argv )
{
    int rc;
    int cfd;
    struct sockaddr_in saddr;
    pthread_t tid;

    fd = socket( AF_INET, SOCK_STREAM, 0 );

    bzero( &saddr, sizeof( saddr ) );
    saddr.sin_family = AF_INET;
    saddr.sin_addr.s_addr = htonl( INADDR_ANY );
    saddr.sin_port = htons( 8000 );

    rc = bind( fd, (struct sockaddr*)&saddr, sizeof(saddr) );
    rc = listen( fd, 128 );

    rc = pthread_create( &tid, NULL, worker, NULL );

    printf("try to connect with: 'telnet 127.0.0.1 8000'\n");
    cfd = accept( fd, (struct sockaddr*)NULL, NULL );
    if (cfd < 0) {
        printf( "client fd=%d\n", cfd );
        printf( "error accept:%s\n", strerror( errno ) );
        exit(1);
    }
    else {
        printf( "client fd=%d\n", cfd );
    }

    return 0;
}
