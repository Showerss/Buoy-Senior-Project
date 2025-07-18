#ifndef COMM_MODULE_H
#define COMM_MODULE_H

#include <stdint.h>

typedef struct CommModule {
    int8_t is_connected;
    int8_t is_transmitting;
    int8_t is_receiving;
    int8_t is_error;
    int8_t is_busy;
    int8_t is_idle;
    int8_t is_ready;
} CommModule;


#endif