#ifndef COMM_MODULE_H
#define COMM_MODULE_H

#include <stdint.h>
#include <stdbool.h>
#include "DataPacket.h"

typedef struct CommModule {
    bool is_connected;
    bool is_transmitting;
    bool is_receiving;
    bool is_error;
    bool is_busy;
    bool is_idle;
    bool is_ready;
} CommModule;

DataPacket comm_encrypt(const DataPacket *raw);

bool comm_send_data(const DataPacket *packet);

bool comm_fallback(const DataPacket *packet);

#endif //COMM_MODULE_H