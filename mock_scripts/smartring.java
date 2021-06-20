package eu.smartringstartup.ring;

import android.support.annotation.NonNull;

import eu.healthdatalabellingsystem.api.endpoints.SendToHDLS;
import eu.healthdatalabellingsystem.api.TokenProvider;
import eu.healthdatalabellingsystem.foreign.ForeignCollector;
import eu.healthdatalabellingsystem.foreign.ForeignData;
import eu.healthdatalabellingsystem.raw.RawCollector;
import eu.healthdatalabellingsystem.raw.RawData;
import eu.healthdatalabellingsystem.service.GDPRDoctor;

import eu.smartringstartup.ai.HeartAttackPredictor;
import eu.smartringstartup.hdls.OurForeignCollector;
import eu.smartringstartup.hdls.OurRawCollector;
import eu.smartringstartup.sensor.SensorDescriptor;
import eu.smartringstartup.sensor.SensorHandler;

public class RingDataHandler extends OurDataHandler implements TokenProvider {

  // TODO: Implement senros data handling and AI prediction handling

  HeartAttackPredictor mPredictor;
  SensorHandler mSensor;
  ForeignCollector mForeignCollector;
  RawCollector mRawCollector;

  public RingDataHandler() {

    mPredictor = HeartAttackPredictor.getInstance();
    mSensor = SensorHandler.getInstance();
    mForeignCollector = (ForeignCollector) new OurForeignCollector();
    mRawCollector = (RawCollector) new OurRawCollector();

  }

  @Override
  void onSignal(@NonNull RawData data, @NonNull SensorDescriptor descriptor) {

    SendToHDLS endpointManager = new SendToHDLS(this.tokenInstance);
    RawData rawData = new RawData(descriptor.device.id, descriptor.sensor.id,
                                  data, descriptor.timestamp,
                                  descriptor.timeSection);
    endpointManager.sendInNewThread(rawData);
    ForeignData foreignData = mPredictor.predict(data);
    if (foreignData != null) endpointManager.sendInNewThread(foreignData);

  }

}
