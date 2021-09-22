#pragma once
#ifndef HDLS_EXTRACTOR_H
#define HDLS_EXTRACTOR_H

#include <string>

#include "hdls_data_object.h"

namespace hdls {

  class HDLSExtractor {

  public:

    HDLSExtractor();
    HDLSExtractor(std::string & use_case_id);

    bool
    deleteData(std::string & conditions);

    HDLSDataObject
    get(std::string & source_id, std::string & data_profile_id,
        bool store = false);

    bool
    match(std::string & current_use_case_id);

  private:

    std::string _use_case_id;

  };

}

#endif /* end of include guard: HDLS_EXTRACTOR_H */
