#include "../include/CommModule.h"
#include "../include/PowerManager.h"
#include "../include/SensorModule.h"
#include "../include/DataPacket.h"


#ifdef HOST_BUILD
   #include <unistd.h>
#endif

int main(void) {
    
    PowerManager *pm = pm_create();
    SensorModule sm = {0};
    DataPacket pkt = {0};

    while (1) {
        pm_wake(pm);
 

        measureTemperature(&sm);
        measurepH(&sm);
        measureTurbidity(&sm);
        measureDissolvedOxygen(&sm);
        measureConductivity(&sm);

        pkt = comm_encrypt(&pkt);
        comm_send_data(&pkt);

        pm_sleep(pm);


    #ifdef HOST_BUILD
        sleep(10);
    #endif

}

    pm_destroy(pm);
    return 0;
}


