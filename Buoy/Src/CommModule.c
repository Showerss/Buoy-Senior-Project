#include "../include/CommModule.h"
#ifdef HOST_BUILD
   #include <stdio.h>
#endif

#ifdef HOST_BUILD


DataPacket comm_encrypt(const DataPacket *raw) {
    printf("[HOST] comm_encrypt: passing DataPacket to encryption function\n");
    return *raw;
}

bool comm_send_data(const DataPacket *packet) {
    printf("[HOST] comm_send_data: pretend sending DataPacket to radio module\n");
    return true;
}

bool comm_fallback(const DataPacket *packet) {
    (void) packet;
    printf("[HOST] comm_fallback: pretend fallback okay\n");
    return true;
}

#else

TODO: real code here

#endif

    