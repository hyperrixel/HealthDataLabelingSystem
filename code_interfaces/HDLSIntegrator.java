package com.hyperrixel.hdls;

import com.hyperrixel.hdls.HDLSDataObject;


public class HDLSIntegrator {

  HDLSIntegrator();

  public HDLSIntegrator(string useCaseID) {

  }

  public bolean deleteData(string condition) {

  }

  public bolean match(string currentUseCaseID) {

  }

  public void send(string destinationID, string outputDataProfileID,
                   HDLSDataObject data) {

    send(destinationID, outputDataProfileID, data, false);

  }

  public void send(string destinationID, string outputDataProfileID,
                   HDLSDataObject data, boolean store) {

  }

}
