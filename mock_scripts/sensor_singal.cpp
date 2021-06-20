#include <raw_collector.h>
#include <raw_data.h>
#include <hdls_3rd_partner_cheap_sensor_type123_template_h>
#include "sensor_signal.h"

/**
  * TODO: Implement sensor signal capture and transform to labelled data.
  */

class OurSensorCollector: public RawCollector, private Cheap123Translate {

  OurSensorCollector() {

    // Weak soldering can couse changes in port numbers
    if (initial_response == NULL) {

      while (initial_response == NULL)  {

        sensor_port += 1;
        safe_reinit()

      }

    }

  }

}
