#pragma once
#ifndef HDLS_DATA_OBJECT_H
#define HDLS_DATA_OBJECT_H

#include <chrono>
#include <map>
#include <string>

#include "hdls_attributes.h"

namespace hdls {

  class HDLSDataObject {

  public:

    HDLSDataObject();
    HDLSDataObject(std::string & value, std::string & unit);
    HDLSDataObject(std::string & value, std::string & unit,
                   HDLSAttributes & attributes);
    HDLSDataObject(std::string & value, std::string & unit,
                   std::map<std::string, std::string> & attributes);

    HDLSAttributes
    attributes() const { return _attributes.asReadOnly(); };

    static HDLSDataObject
    fromJSON(std::string & json_string);

    std::str
    get(std::str & key) const { return _attributes.get(key); };

    bool
    has(std::str & key) const { return _attributes.has(key); };

    bool
    isTrue(std::str & key) const { return _attributes.isTrue(key); };

    std::chrono::milliseconds
    time() const { return _time; };

    std::string
    toJSON();

    std::string
    unit() const { return _unit; };

    std::string
    value() const { return _value; };


  private:

    std::string _value;
    std::string _unit;
    HDLSAttributes _attributes;
    std::chrono::milliseconds _time;

  };


}

#endif /* end of include guard: HDLS_DATA_OBJECT_H */
