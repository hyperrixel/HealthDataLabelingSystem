#pragma once
#ifndef RAW_STORAGE_H
#define RAW_STORAGE_H

#include <ctime>
#include <string>
#include <vector>

#include "raw_data.h"

template<typename SUBCLASS>

class RawStorage {

public:

  RawStorage(std::string &json_str);
  virtual std::string create_storage(const std::string &storage_name, const std::string &permissions_json, const std::string &properties_json) = 0;
  virtual std::string create_user(const std::string &user_name, const std::string &permissions_json, const std::string &properties_json) = 0;
  virtual bool delete_data(const std::string &staorage_id, const std::string &data_entry_id) = 0;
  virtual bool delete_storage(const std::string &staorage_id) = 0;
  virtual bool delete_user(const std::string &user_id) = 0;
  virtual SUBCLASS from_file(std::string &json_path) = 0;
  virtual RawData get(const std::string &staorage_id, const std::string &data_entry_id) = 0;
  virtual std::string[] get_storage(const std::string staorage_id) = 0;
  virtual std::string[] get_user(const std::string user_id) = 0;
  virtual std::string insert(const std::string staorage_id, const RawData &data) = 0;
  virtual bool login(const std::string &user_id, const std::string &user_name, const std::str &token) = 0;
  virtual bool logout() = 0;
  void update(const std::str &staorage_id, const std::string &data_entry_id, const RawData &data);
  virtual bool update_storage(const std::string &staorage_id, const std::string &storage_name, const std::string &permissions_json, const std::string &properties_json) = 0;
  virtual bool update_user(const std::string &user_id, const std::string &user_name, const std::string &permissions_json, const std::string &properties_json) = 0;

};

#endif /* end of include guard: RAW_STORAGE_H */
