#pragma once
#ifndef HDLS_INTEGRATOR_H
#define HDLS_INTEGRATOR_H

#include <string>

#include "hdls_data_object.h"

namespace hdls{

  class HDLSIntegrator {

  public:

    HDLSIntegrator();
    HDLSIntegrator(std::string & use_case_id);

    bool
    deleteData(std::string & conditions);

    bool
    match(std::string & current_use_case_id);

    void
    send(std::string & destination_id, std::string & output_data_profile_id,
         HDLSDataObject data, databool store = false);

  private:



  };

}

#endif /* end of include guard: HDLS_INTEGRATOR_H */
