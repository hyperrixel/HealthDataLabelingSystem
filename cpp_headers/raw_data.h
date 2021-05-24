#pragma once
#ifndef RAW_DATA_H
#define RAW_DATA_H

#include <iostream>
#include <ctime>
#include <string>

class RawData {

public:

  RawData(const std::string &device_id, const std::string &source_id, const std::string &data, const std::time_t timestamp = 0, const unsigned short int time_section = 0);
  std::string data() const { return data_; };
  std::string device_id() const { return device_id_; };
  std::string source_id() const { return source_id_; };
  std::time_t timestamp() const { return timestamp_; };
  unsigned short int time_section() const { return time_section_; };

private:

  std::time_t timestamp_;
  unsigned short int time_section_;
  std::string device_id_;
  std::string source_id_;
  std::string data_;

};

#endif /* end of include guard: RAW_DATA_H */
