# autonomous-uav

### Prerequisites
Ensure that the following prerequisites are met:
1. Install ArduPilot:
    - [Set up your ArduPilot Build Environment](https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux)
      - **NOTE**: Select the correct autopilot board when building with waf. We are using **PIXHAWK1**
2. QGroundControl is already downloaded to the repository. To 

### Running the Simulator
1. Clone the repository
`git clone https://github.com/guchiyams/autonomous-uav.git`
2. In the root directory, run the command
`sim_vehicle.py -v ArduCopter --out="localhost:14550" --out="localhost:14551"`
3. Run QGroundControl
`./QGroundControl.AppImage`

### Running the auto-uav
1. Ensure prerequisites are met and Ground Control System (GCS) is running
2. Run auto-uav
`python main.py`
