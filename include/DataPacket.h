#ifndef DATA_PACKET_H
#define DATA_PACKET_H

#include <stdint.h>

typedef struct {
    uint32_t timestamp;
    float temperature;
    float ph;
    float turbidity;
    float dissolved_oxygen;
    float conductivity;
    uint8_t device_id;
} DataPacket;

#endif //DATA_PACKET_H