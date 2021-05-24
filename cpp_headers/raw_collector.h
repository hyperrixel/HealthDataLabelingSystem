#pragma once
#ifndef RAW_COLLECTOR_H
#define RAW_COLLECTOR_H

#include <ctime>
#include <string>
#include <vector>

#include "raw_data.h"

template<typename ANY>

class RawCollector {

public:

  RawCollector();
  void clean();
  virtual void collect(const ANY &device_id, const ANY &source_id, const ANY &data) = 0;
  virtual void collect(const ANY &device_id, const ANY &source_id, const ANY &data, const std::time_t &timestamp) = 0;
  virtual void collect(const ANY &device_id, const ANY &source_id, const ANY &data, const std::time_t &timestamp, const unsigned short int &time_section) = 0;
  std::vector<RawData> flush();
  std::vector<RawData> get(const unsigned int &from);
  std::vector<RawData> get(const unsigned int &from, const unsigned int &to);
  RawData get_by_id(const unsigned int &data_id) const { return content_.at(data_id); };
  bool has_new() const { return content_.size() >= new_from_ - start_id_ ? true : false; };
  unsigned int len() const { return content_.size(); };

private:

  std::vector<RawData> content_;
  unsigned int start_id_;
  unsigned int new_from_;

};

#endif /* end of include guard: RAW_COLLECTOR_H */
